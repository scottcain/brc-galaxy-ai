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
contents = await gxy.api(f"/api/histories/{history_id}/contents?v=dev&keys=type,name,collection_id,deleted")

mapping = {}
for item in contents:
    if item.get('history_content_type') == 'dataset_collection':
        hdca_id = item.get('id')
        try:
            col_data = await gxy.api(f"/api/histories/{history_id}/contents/dataset_collections/{hdca_id}")
            elements = col_data.get('elements', [])
            for el in elements:
                obj = el.get('object', {})
                ds_id = obj.get('id')
                hid = obj.get('hid')
                uuid_val = obj.get('uuid')
                identifier = el.get('element_identifier')
                if identifier:
                    if ds_id: mapping[ds_id] = identifier
                    if uuid_val: mapping[uuid_val] = identifier
                    if hid: mapping[f"Galaxy{hid}-"] = identifier
                    # gxy sometimes uses dataset_UUID or dataset_ID
                    if ds_id: mapping[f"dataset_{ds_id}"] = identifier
                    if uuid_val: mapping[f"dataset_{uuid_val}"] = identifier
        except Exception as e:
            pass

print(f"Built mapping for {len(mapping)} dataset elements.")

print("Processing SNPeff VCFs...")
snpeff_ids = [d['id'] for d in contents if d.get('history_content_type') == 'dataset' and not d.get('deleted') and 'SnpEff eff: on dataset' in d.get('name', '') and 'HTML' not in d.get('name', '')]
all_snpeff = []
for ds_id in snpeff_ids:
    try:
        p = await gxy.get(ds_id, identifier_type="id")
        if isinstance(p, list): all_snpeff.extend(p)
        else: all_snpeff.append(p)
    except Exception as e:
        print(f"Skipping SNPeff {ds_id}: {e}")

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
            if line.startswith('#'): continue
            vparts = line.split('\t')
            chrom = vparts[0]
            pos = int(vparts[1])
            ref = vparts[3]
            alt = vparts[4]
            info = vparts[7]
            
            if chrom == cyp51a_chr and cyp51a_start <= pos <= cyp51a_end:
                if any(kw in info for kw in ['missense_variant', 'nonsynonymous', 'NON_SYNONYMOUS']):
                    attr = f"ID=SNP_{sra_accession}_{pos};Name={ref}{pos}{alt};Note=Nonsynonymous_SNP"
                    gff_lines.append(f"{chrom}\t{sra_accession}\tSNP\t{pos}\t{pos}\t.\t.\t.\t{attr}\n")

print("Processing etandem outputs...")
etandem_ids = [d['id'] for d in contents if d.get('history_content_type') == 'dataset' and not d.get('deleted') and 'etandem on dataset' in d.get('name', '')]
all_etandem = []
for ds_id in etandem_ids:
    try:
        p = await gxy.get(ds_id, identifier_type="id")
        if isinstance(p, list): all_etandem.extend(p)
        else: all_etandem.append(p)
    except Exception as e:
        print(f"Skipping etandem {ds_id}: {e}")

if not isinstance(all_etandem, list): all_etandem = [all_etandem]

global_offset = 1777374 - 1

for p in all_etandem:
    is_tabular = False
    is_gff = False
    with open(p, 'r') as f:
        head = f.read(200)
        if "##gff-version" in head:
            is_gff = True
        elif len(head.strip()) > 0 and not head.startswith('#'):
            first_line = head.strip().split('\n')[0]
            parts = first_line.split()
            if len(parts) >= 6 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                is_tabular = True
                
    if not (is_gff or is_tabular):
        continue
    
    sra_accession = "Sample_Unknown"
    for ds_id, sra in mapping.items():
        if ds_id in p:
            sra_accession = sra
            break
    
    with open(p, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            
            if is_gff:
                vparts = line.split('\t')
                if len(vparts) >= 9:
                    if vparts[2] != 'tandem_repeat':
                        continue
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
            elif is_tabular:
                vparts = line.split()
                if len(vparts) >= 6:
                    local_start = int(vparts[1])
                    local_end = int(vparts[2])
                    
                    global_start = global_offset + local_start
                    global_end = global_offset + local_end
                    
                    if global_end >= 1781822:
                        repeat_seq = vparts[6] if len(vparts) > 6 else ""
                        attr = f"ID=TR_{sra_accession}_{global_start};Note=Promoter_Tandem_Repeat"
                        if repeat_seq:
                            attr += f";Repeat_Sequence={repeat_seq}"
                        gff_line = f"{cyp51a_chr}\t{sra_accession}\ttandem_repeat\t{global_start}\t{global_end}\t.\t.\t.\t{attr}\n"
                        gff_lines.append(gff_line)

out_file = "cyp51a_variants_by_sra.gff3"
with open(out_file, "w") as f:
    f.writelines(gff_lines)

print(f"Uploading GFF3 with {len(gff_lines)-1} features to Galaxy...")
await gxy.put(out_file, output="cyp51A Combined Variants (By SRA)", ext="gff3")
print("Done!")