import nbformat as nbf

with open('step4_notebook_source.py', 'r') as f:
    code = f.read()

nb = nbf.v4.new_notebook()

md_text = """# Identifying Resistant-Specific SNPs

This notebook aggregates the SNP calls from SnpEff for both susceptible and resistant samples. It creates a union of SNPs across all susceptible samples, and an intersection of SNPs across all resistant samples. Finally, it identifies the resistant-specific SNPs (those in the intersection but not in the susceptible union) and outputs them as a VCF file."""

nb.cells.append(nbf.v4.new_markdown_cell(md_text))
nb.cells.append(nbf.v4.new_code_cell(code))

with open('resistant_specific_snps_v7.ipynb', 'w') as f:
    nbf.write(nb, f)
