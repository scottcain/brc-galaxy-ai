import nbformat as nbf
import os
from bioblend.galaxy import GalaxyInstance

# 1. Generate the Notebook
nb = nbf.v4.new_notebook()

code_lines = [
    "import gxy",
    "import os",
    "import time",
    "",
    "susceptible_sras = [",
    "    'ERR14230090', 'ERR14230091', 'ERR14230092', 'ERR14230093', ",
    "    'ERR14230094', 'ERR14230095', 'ERR14230096', 'ERR14230097', ",
    "    'ERR14230098', 'ERR14230099', 'ERR14230101', 'ERR14230102', ",
    "    'ERR14230104', 'ERR14230106', 'ERR14230107', 'SRR12949926', ",
    "    'SRR12949927', 'SRR12949928', 'SRR12949929'",
    "]",
    "",
    "resistant_sras = [",
    "    'ERR14230100', 'ERR14230103', 'ERR14230105'",
    "]",
    "",
    "print(\"Building SRA accession mapping from dataset collections...\")",
    "history_id = await gxy.get_history_id()",
    "contents = await gxy.api(f\"/api/histories/{history_id}/contents?v=dev&keys=type,name,collection_id\")",
    "",
    "mapping = {}",
    "for item in contents:",
    "    if item.get('history_content_type') == 'dataset_collection':",
    "        hdca_id = item.get('id')",
    "        try:",
    "            col_data = await gxy.api(f\"/api/histories/{history_id}/contents/dataset_collections/{hdca_id}\")",
    "            elements = col_data.get('elements', [])",
    "            for el in elements:",
    "                obj = el.get('object', {})",
    "                ds_id = obj.get('id')",
    "                hid = obj.get('hid')",
    "                uuid_val = obj.get('uuid')",
    "                identifier = el.get('element_identifier')",
    "                if identifier:",
    "                    if ds_id: mapping[ds_id] = identifier",
    "                    if uuid_val: mapping[uuid_val] = identifier",
    "                    if hid: mapping[f\"Galaxy{hid}-\"] = identifier",
    "                    if ds_id: mapping[f\"dataset_{ds_id}\"] = identifier",
    "                    if uuid_val: mapping[f\"dataset_{uuid_val}\"] = identifier",
    "        except Exception as e:",
    "            pass",
    "",
    "print(f\"Built mapping for {len(mapping)} dataset elements.\")",
    "",
    "print(\"Fetching SnpEff VCFs...\")",
    "all_snpeff = await gxy.get(\".*SnpEff eff: on dataset.*\", identifier_type=\"regex\")",
    "if not isinstance(all_snpeff, list): ",
    "    all_snpeff = [all_snpeff]",
    "",
    "susceptible_snps = set()",
    "resistant_snps_per_sample = {sra: set() for sra in resistant_sras}",
    "",
    "print(\"Parsing VCFs to aggregate SNPs per sample...\")",
    "for p in all_snpeff:",
    "    with open(p, 'r') as f:",
    "        head = f.read(50)",
    "        if \"##fileformat=VCF\" not in head: continue",
    "    ",
    "    sra_accession = \"Sample_Unknown\"",
    "    for ds_id, sra in mapping.items():",
    "        if ds_id in p:",
    "            sra_accession = sra",
    "            break",
    "            ",
    "    if sra_accession not in susceptible_sras and sra_accession not in resistant_sras:",
    "        continue",
    "        ",
    "    with open(p, 'r') as f:",
    "        for line in f:",
    "            line = line.strip()",
    "            if not line or line.startswith('#'): continue",
    "            vparts = line.split('\\t')",
    "            if len(vparts) < 8: continue",
    "            ",
    "            chrom = vparts[0]",
    "            pos = vparts[1]",
    "            ref = vparts[3]",
    "            alt = vparts[4]",
    "            filter_val = vparts[6]",
    "            ",
    "            snp_key = (chrom, pos, ref, alt)",
    "            ",
    "            if sra_accession in susceptible_sras:",
    "                susceptible_snps.add(snp_key)",
    "            elif sra_accession in resistant_sras:",
    "                resistant_snps_per_sample[sra_accession].add(snp_key)",
    "",
    "print(f\"Total union SNPs in susceptible samples: {len(susceptible_snps)}\")",
    "",
    "if not resistant_sras:",
    "    resistant_intersection = set()",
    "else:",
    "    first_sample = resistant_sras[0]",
    "    resistant_intersection = resistant_snps_per_sample[first_sample]",
    "    for sra in resistant_sras[1:]:",
    "        resistant_intersection = resistant_intersection.intersection(resistant_snps_per_sample[sra])",
    "",
    "print(f\"Total intersecting SNPs in all resistant samples: {len(resistant_intersection)}\")",
    "",
    "resistant_specific_snps = resistant_intersection - susceptible_snps",
    "print(f\"Number of resistant-specific SNPs: {len(resistant_specific_snps)}\")",
    "",
    "out_file = \"resistant_specific_snps.vcf\"",
    "print(f\"Writing results to {out_file} in VCF format...\")",
    "",
    "with open(out_file, \"w\") as f:",
    "    f.write(\"##fileformat=VCFv4.2\\n\")",
    "    f.write(f\"##fileDate={time.strftime('%Y%m%d')}\\n\")",
    "    f.write(\"##source=JupyterLite_Step4_Iteration6\\n\")",
    "    f.write(f\"##SusceptibleUnionCount={len(susceptible_snps)}\\n\")",
    "    f.write(f\"##ResistantIntersectionCount={len(resistant_intersection)}\\n\")",
    "    f.write(\"##FILTER=<ID=PASS,Description=\\\"All filters passed\\\">\\n\")",
    "    f.write(\"##INFO=<ID=RS,Description=\\\"Resistant Specific\\\">\\n\")",
    "    f.write(\"#CHROM\\tPOS\\tID\\tREF\\tALT\\tQUAL\\tFILTER\\tINFO\\n\")",
    "    ",
    "    for snp in sorted(list(resistant_specific_snps), key=lambda x: (x[0], int(x[1]))):",
    "        f.write(f\"{snp[0]}\\t{snp[1]}\\t.\\t{snp[2]}\\t{snp[3]}\\t.\\tPASS\\tRS\\n\")",
    "",
    "print(\"Uploading VCF result to Galaxy...\")",
    "await gxy.put(out_file, output=\"Resistant Specific SNPs (VCF)\", ext=\"vcf\")",
    "print(\"Done!\")"
]

code = "\n".join(code_lines)

markdown_content = """# Step 4: Identifying Resistant-Specific SNPs (Iteration 6)

This notebook identifies SNPs specific to resistant samples by comparing SNP calls from SnpEff VCFs across both susceptible and resistant cohorts. 
It outputs the results as a VCF file, including counts of the susceptible union and resistant intersection.
"""

nb.cells.append(nbf.v4.new_markdown_cell(markdown_content))
nb.cells.append(nbf.v4.new_code_cell(code))

nb_filename = 'resistant_specific_snps_v8_final.ipynb'
with open(nb_filename, 'w') as f:
    nbf.write(nb, f)

print(f"Created updated notebook: {nb_filename}")

# 2. Upload the Notebook
api_key = os.environ.get("GALAXY_API_KEY")
if api_key:
    gi = GalaxyInstance(url='https://usegalaxy.org', key=api_key)
    history_id = "bbd44e69cb8906b5623ea083aa036a1d"
    print(f"Uploading to history: {history_id}")
    res = gi.tools.upload_file(
        nb_filename, 
        history_id, 
        file_name="Step 4: Resistant Specific SNPs Notebook (Iteration 6)", 
        file_type="ipynb"
    )
    print("Uploaded successfully!")
else:
    print("GALAXY_API_KEY not set, skipping upload.")
