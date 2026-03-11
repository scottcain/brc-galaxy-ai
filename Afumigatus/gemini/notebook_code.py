import gxy
import gzip
import re
import os

print("Fetching GTF (Dataset #1)...")
gtf_paths = await gxy.get(1)
gtf_path = gtf_paths[0] if isinstance(gtf_paths, list) else gtf_paths

cyp51a_chr = "NC_007197.1"
cyp51a_start = 1777374
cyp51a_end = 1781821

try:
    with (gzip.open(gtf_path, 'rt') if gtf_path.endswith('.gz') else open(gtf_path, 'r')) as f:
        for line in f:
            if line.startswith('#'): continue
            parts = line.split('\t')
            if len(parts) > 8 and parts[2] == 'gene' and 'Afu4g06890' in parts[8]:
                cyp51a_chr = parts[0]
                cyp51a_start = int(parts[3])
                cyp51a_end = int(parts[4])
                break
except Exception as e:
    print(f"Note: Could not parse GTF precisely ({e}), using default Af293 coordinates.")

print(f"Target Gene cyp51A: {cyp51a_chr}:{cyp51a_start}-{cyp51a_end}")

print("Building SRA accession mapping from dataset collections...")
history_id = await gxy.get_history_id()
contents = await gxy.api(f"/api/histories/{history_id}/contents?v=dev&keys=type,name")

mapping = {}
for item in contents:
    if item.get('history_content_type') == 'dataset_collection':
        try:
            hdca_id = item['id']
            col_data = await gxy.api(f"/api/histories/{history_id}/contents/dataset_collections/{hdca_id}")
            elements = col_data.get('elements', [])
            for el in elements:
                obj = el.get('object', {})
                ds_id = obj.get('id')
                identifier = el.get('element_identifier')
                if ds_id and identifier:
                    mapping[ds_id] = identifier
        except Exception as e:
            pass

print(f"Built mapping for {len(mapping)} dataset elements.")

print("Processing SNPeff VCFs...")
all_snpeff = await gxy.get(".*SnpEff eff: on dataset.*", identifier_type="regex")
if not isinstance(all_snpeff, list): all_snpeff = [all_snpeff]

gff_lines = ["##gff-version 3\n"]

for p in all_snpeff:
    with open(p, 'r') as f:
        head = f.read(50)
        if "##fileformat=VCF" not in head: continue
    
    sra_accession = "Sample_Unknown"
    for ds_id, sra in mapping.items():
        if ds_id in p:
            sra_accession = sra
            break
    
    with open(p, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            vparts = line.split('\t')
            if len(vparts) < 8: continue
            chrom = vparts[0]
            pos = int(vparts[1])
            ref = vparts[3]
            alt = vparts[4]
            info = vparts[7]
            
            if chrom == cyp51a_chr and cyp51a_start <= pos <= cyp51a_end:
                if any(kw in info for kw in ['missense_variant', 'nonsynonymous', 'NON_SYNONYMOUS']):
                    attr = f"ID=SNP_{sra_accession}_{pos};Name={ref}{pos}{alt};Note=Nonsynonymous_SNP"
                    gff_lines.append(f"{chrom}\t{sra_accession}\tSNP\t{pos}\t{pos}\t.\t.\t.\t{attr}\n")

print("Processing etandem GFFs...")
all_etandem = await gxy.get(".*etandem on dataset.*", identifier_type="regex")
if not isinstance(all_etandem, list): all_etandem = [all_etandem]

global_offset = 1777374 - 1

for p in all_etandem:
    with open(p, 'r') as f:
        head = f.read(50)
        if "##gff-version" not in head: continue
    
    sra_accession = "Sample_Unknown"
    for ds_id, sra in mapping.items():
        if ds_id in p:
            sra_accession = sra
            break
    
    with open(p, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            vparts = line.split('\t')
            if len(vparts) >= 9:
                local_start = int(vparts[3])
                local_end = int(vparts[4])
                
                global_start = global_offset + local_start
                global_end = global_offset + local_end
                
                if global_end >= 1781822:
                    vparts[0] = cyp51a_chr
                    vparts[1] = sra_accession
                    vparts[3] = str(global_start)
                    vparts[4] = str(global_end)
                    vparts[8] = f"Note=Promoter_Tandem_Repeat;{vparts[8].strip()}"
                    gff_lines.append("\t".join(vparts) + "\n")

out_file = "cyp51a_variants_by_sra.gff3"
with open(out_file, "w") as f:
    f.writelines(gff_lines)

print(f"Uploading GFF3 with {len(gff_lines)-1} features to Galaxy...")
await gxy.put(out_file, output="cyp51A Combined Variants (By SRA)", ext="gff3")
print("Done!")