import nbformat as nbf

with open('notebook_source.py', 'r') as f:
    code = f.read()

nb = nbf.v4.new_notebook()

md_text = """# Multi-Sample Variant Assembly for cyp51A

This notebook creates a GFF3 file where **each sample's variants are on their own line** (using the Source column). It uses the SRA accession (e.g. ERR123456) for each line, retrieved via the dataset collections API. Supports both GFF and tabular etandem outputs."""

nb.cells.append(nbf.v4.new_markdown_cell(md_text))
nb.cells.append(nbf.v4.new_code_cell(code))

with open('variants_cyp51A_v21.ipynb', 'w') as f:
    nbf.write(nb, f)
