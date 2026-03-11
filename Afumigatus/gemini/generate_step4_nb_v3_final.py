import nbformat as nbf

nb = nbf.v4.new_notebook()

with open('step4_code.py', 'r') as f:
    code = f.read()

markdown_content = """# Step 4: Identifying Resistant-Specific SNPs (Iteration 2)

This notebook identifies SNPs specific to resistant samples by comparing SNP calls from SnpEff VCFs across both susceptible and resistant cohorts. 

### Methodology:
1. Identify all VCFs using regex matching.
2. Resolve dataset IDs to SRA accessions to categorize samples.
3. Compute the **union** of all SNPs observed in any susceptible sample.
4. Compute the **intersection** of SNPs present in *all* resistant samples.
5. Identify the resulting **resistant-specific SNPs** by removing the susceptible union set from the resistant intersection set.
6. Upload the final list of variants as a **VCF file** directly to the active Galaxy history for browser visualization.
"""

nb.cells.append(nbf.v4.new_markdown_cell(markdown_content))
nb.cells.append(nbf.v4.new_code_cell(code))

with open('resistant_specific_snps_v3.ipynb', 'w') as f:
    nbf.write(nb, f)

print("Created updated notebook: resistant_specific_snps_v3.ipynb")
