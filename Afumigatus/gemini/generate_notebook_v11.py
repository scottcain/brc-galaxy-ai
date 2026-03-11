import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """import gxy
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
            parts = line.split('	')
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
contents = await gxy.api(f"/api/histories/{history_id}/contents?v=dev&keys=type,name,collection_id")

mapping = {}
for item in contents:
    if item.get('history_content_type') == 'dataset_collection':
        col_id = item.get('collection_id') or item.get('id')
        try:
            col_data = await gxy.api(f"/api/dataset_collections/{col_id}")
            elements = col_data.get('elements', [])
            for el in elements:
                obj = el.get('object', {})
                ds_id = obj.get('id')
                identifier = el.get('element_identifier')
                if ds_id and identifier:
                    mapping[ds_id] = identifier
        except Exception as e:
            # Silently skip if API fails for a collection
            pass

print(f"Built mapping for {len(mapping)} dataset elements.")

print("Processing SNPeff VCFs...")
all_snpeff = await gxy.get(".*SnpEff eff: on dataset.*", identifier_type="regex")
if not isinstance(all_snpeff, list): all_snpeff = [all_snpeff]

gff_lines = ["##gff-version 3
"]

for p in all_snpeff:
    with open(p, 'r') as f:
        head = f.read(50)
        if "##fileformat=VCF" not in head: continue
    
    parts = os.path.basename(p).split('.')
    ds_id = parts[-2] if len(parts) >= 2 else ""
    sra_accession = mapping.get(ds_id, f"Sample_{ds_id[:6]}")
    
    with open(p, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            vparts = line.split('	')
            chrom = vparts[0]
            pos = int(vparts[1])
            ref = vparts[3]
            alt = vparts[4]
            info = vparts[7]
            
            if chrom == cyp51a_chr and cyp51a_start <= pos <= cyp51a_end:
                if any(kw in info for kw in ['missense_variant', 'nonsynonymous', 'NON_SYNONYMOUS']):
                    attr = f"ID=SNP_{sra_accession}_{pos};Name={ref}{pos}{alt};Note=Nonsynonymous_SNP"
                    gff_lines.append(f"{chrom}	{sra_accession}	SNP	{pos}	{pos}	.	.	.	{attr}
")

print("Processing etandem outputs...")
all_etandem = await gxy.get(".*etandem on dataset.*", identifier_type="regex")
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
            first_line = head.strip().split('
')[0]
            parts = first_line.split()
            if len(parts) >= 6 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                is_tabular = True
                
    if not (is_gff or is_tabular):
        continue
    
    parts = os.path.basename(p).split('.')
    ds_id = parts[-2] if len(parts) >= 2 else ""
    sra_accession = mapping.get(ds_id, f"Sample_{ds_id[:6]}")
    
    with open(p, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            
            if is_gff:
                vparts = line.split('	')
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
                        gff_lines.append("	".join(vparts) + "
")
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
                        gff_line = f"{cyp51a_chr}	{sra_accession}	tandem_repeat	{global_start}	{global_end}	.	.	.	{attr}
"
                        gff_lines.append(gff_line)

out_file = "cyp51a_variants_by_sra.gff3"
with open(out_file, "w") as f:
    f.writelines(gff_lines)

print(f"Uploading GFF3 with {len(gff_lines)-1} features to Galaxy...")
await gxy.put(out_file, output="cyp51A Combined Variants (By SRA)", ext="gff3")
print("Done!")
"""

nb.cells.append(nbf.v4.new_markdown_cell("""# Multi-Sample Variant Assembly for cyp51A

This notebook creates a GFF3 file where **each sample's variants are on their own line** (using the Source column). It uses the SRA accession (e.g. ERR123456) for each line, retrieved via the dataset collections API. Supports both GFF and tabular etandem outputs."""))
nb.cells.append(nbf.v4.new_code_cell(code))

with open('variants_cyp51A_v11.ipynb', 'w') as f:
    nbf.write(nb, f)
