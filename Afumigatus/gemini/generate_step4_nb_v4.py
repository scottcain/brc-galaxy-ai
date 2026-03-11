import nbformat as nbf

nb = nbf.v4.new_notebook()

with open('step4_code_fixed.py', 'r') as f:
    code = f.read()

markdown_content = """# Step 4: Identifying Resistant-Specific SNPs (Fixed Dataset Mapping)

This notebook identifies SNPs specific to resistant samples by comparing SNP calls from SnpEff VCFs across both susceptible and resistant cohorts. 

### Fixes Applied:
- **Dataset Collection Mapping**: Fixed the Galaxy API endpoint to correctly resolve HDCAs (`/api/histories/{history_id}/contents/dataset_collections/{hdca_id}`). This resolves the issue where the sample names were previously unmatched, causing the analysis to skip all files.
- **SRA Matching Strategy**: Modified to match the SRA identifier using direct string inclusion (`if ds_id in p`), successfully utilized in earlier steps.
- **PASS Filter Check**: Ensured only confident calls (`PASS` or `.`) are considered to prevent low-confidence variants in susceptible samples from accidentally excluding legitimate resistant variants.
"""

nb.cells.append(nbf.v4.new_markdown_cell(markdown_content))
nb.cells.append(nbf.v4.new_code_cell(code))

with open('resistant_specific_snps_v4_fixed.ipynb', 'w') as f:
    nbf.write(nb, f)

print("Created updated notebook: resistant_specific_snps_v4_fixed.ipynb")
