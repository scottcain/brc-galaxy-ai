import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """import gxy
import gzip
import re
import os

# 1. Coordinate Discovery for cyp51A (Afu4g06890)
# The gene is on the reverse strand of Chromosome 4 (NC_007197.1)
# Standard Af293 Coordinates: Gene (1,777,374-1,781,821), Promoter (1,781,822-1,782,821)
print("Fetching GTF (Dataset #1)...")
gtf_paths = await gxy.get(1) # Using HID 1 as requested
gtf_path = gtf_paths[0] if isinstance(gtf_paths, list) else gtf_paths

# Default to known Af293 coordinates if GTF parsing fails
cyp51a_chr = "NC_007197.1"
cyp51a_start = 1777374
cyp51a_end = 1781821

try:
    with (gzip.open(gtf_path, 'rt') if gtf_path.endswith('.gz') else open(gtf_path, 'r')) as f:
        for line in f:
            if line.startswith('#'): continue
            parts = line.split('\\t')
            if len(parts) > 8 and parts[2] == 'gene' and 'Afu4g06890' in parts[8]:
                cyp51a_chr = parts[0]
                cyp51a_start = int(parts[3])
                cyp51a_end = int(parts[4])
                break
except Exception as e:
    print(f"Note: Could not parse GTF precisely ({e}), using default Af293 coordinates.")

print(f"Target Gene cyp51A: {cyp51a_chr}:{cyp51a_start}-{cyp51a_end}")

# 2. Extract SNPeff Nonsynonymous Calls
# Mapping each sample to its own 'source' line in the GFF3
print("Processing SNPeff VCFs...")
all_snpeff = await gxy.get(".*SnpEff eff: on dataset.*", identifier_type="regex")
if not isinstance(all_snpeff, list): all_snpeff = [all_snpeff]

gff_lines = ["##gff-version 3\\n"]

for p in all_snpeff:
    # Basic check for VCF format
    with open(p, 'r') as f:
        head = f.read(50)
        if "##fileformat=VCF" not in head: continue
    
    # Extract Sample ID from filename (e.g., 'SnpEff eff: on dataset 66' -> 'Sample_66')
    match = re.search(r"dataset (\d+)", p)
    sample_label = f"Sample_{match.group(1)}" if match else os.path.basename(p)
    
    with open(p, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            parts = line.split('\\t')
            chrom = parts[0]
            pos = int(parts[1])
            ref = parts[3]
            alt = parts[4]
            info = parts[7]
            
            # Filter for gene region and nonsynonymous mutations
            if chrom == cyp51a_chr and cyp51a_start <= pos <= cyp51a_end:
                if any(kw in info for kw in ['missense_variant', 'nonsynonymous', 'NON_SYNONYMOUS']):
                    # Using sample_label as SOURCE (col 2) so they appear on separate lines
                    attr = f"ID=SNP_{sample_label}_{pos};Name={ref}{pos}{alt};Note=Nonsynonymous_SNP"
                    gff_lines.append(f"{chrom}\\t{sample_label}\\tSNP\\t{pos}\\t{pos}\\t.\\t.\\t.\\t{attr}\\n")

# 3. Extract etandem Promoter Repeats
# Local coordinates from etandem must be mapped back to genomic coordinates
print("Processing etandem GFFs...")
all_etandem = await gxy.get(".*etandem on dataset.*", identifier_type="regex")
if not isinstance(all_etandem, list): all_etandem = [all_etandem]

# Offset calculation: assuming extraction was Gene + 1000bp Promoter (1,777,374 to 1,782,821)
# Local index 1 = Genomic 1,777,374
global_offset = 1777374 - 1

for p in all_etandem:
    with open(p, 'r') as f:
        head = f.read(50)
        if "##gff-version" not in head: continue
    
    match = re.search(r"dataset (\d+)", p)
    sample_label = f"Sample_{match.group(1)}" if match else os.path.basename(p)
    
    with open(p, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            parts = line.split('\\t')
            if len(parts) >= 9:
                local_start = int(parts[3])
                local_end = int(parts[4])
                
                # Convert to Af293 Genomic Coordinates
                global_start = global_offset + local_start
                global_end = global_offset + local_end
                
                # Check if repeat is in the promoter region (1,781,822-1,782,821)
                if global_end >= 1781822:
                    parts[0] = cyp51a_chr
                    parts[1] = sample_label # Set source to Sample ID
                    parts[3] = str(global_start)
                    parts[4] = str(global_end)
                    parts[8] = f"Note=Promoter_Tandem_Repeat;{parts[8].strip()}"
                    gff_lines.append("\\t".join(parts) + "\\n")

# 4. Finalize and Upload
out_file = "cyp51a_variants_by_sample.gff3"
with open(out_file, "w") as f:
    f.writelines(gff_lines)

print(f"Uploading GFF3 with {len(gff_lines)-1} features to Galaxy...")
await gxy.put(out_file, output="cyp51A Combined Variants (By Sample)", ext="gff3")
print("Done!")
"""

nb.cells.append(nbf.v4.new_markdown_cell("# Multi-Sample Variant Assembly for cyp51A\\n\\nThis notebook creates a GFF3 file where **each sample's variants are on their own line** (using the Source column). It combines nonsynonymous SNPs from SnpEff and promoter tandem repeats from etandem, mapped to Af293 coordinates."))
nb.cells.append(nbf.v4.new_code_cell(code))

with open('variants_cyp51A_v2.ipynb', 'w') as f:
    nbf.write(nb, f)
