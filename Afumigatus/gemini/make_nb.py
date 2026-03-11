import nbformat as nbf

nb = nbf.v4.new_notebook()

with open('notebook_code.py', 'r') as f:
    code = f.read()

markdown_content = "# Multi-Sample Variant Assembly for cyp51A\\n\\nThis notebook creates a GFF3 file where **each sample's variants are on their own line** (using the Source column). It uses the SRA accession (e.g. ERR123456) for each line, retrieved via the dataset collections API."

nb.cells.append(nbf.v4.new_markdown_cell(markdown_content))
nb.cells.append(nbf.v4.new_code_cell(code))

with open('variants_cyp51A_v8.ipynb', 'w') as f:
    nbf.write(nb, f)
