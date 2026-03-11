# STEP 4 Execution Notes

- **Goal Verification**: The objective is to identify a set of resistant-specific SNPs by comparing SnpEff VCF outputs between susceptible and resistant samples.
- **Mixed Samples Handling**: Similar to Step 3, the History contains all susceptible and resistant samples mixed in a single dataset collection. The notebook utilizes the robust multi-ID string matching fallback mapping logic developed in Step 3 (unpacking datasets via `/api/histories/{history_id}/contents/dataset_collections/{hdca_id}`) to accurately determine the SRA accession corresponding to each SnpEff file. 
- **Sample Classification**: The script explicitly splits the identified SRA accessions into the resistant list (`ERR14230100`, `ERR14230103`, `ERR14230105`) and the susceptible list (the remaining 19 `ERR`/`SRR` accessions).
- **Variant Processing**: 
  - The script extracts high-quality (where FILTER is `PASS` or `.`) SNPs (`CHROM`, `POS`, `REF`, `ALT`) from each mapped VCF.
  - A union of all SNPs is aggregated for the susceptible samples.
  - An intersection of SNPs is aggregated for the resistant samples.
  - Resistant-specific SNPs are then computed as the set difference between the resistant intersection and the susceptible union.
- **Output & Error Avoidance (Iteration 5 Fix)**: The resulting resistant-specific SNPs are written to a valid VCF v4.2 file. The notebook code is injected cleanly by reading raw python source directly. Furthermore, to specifically address the Iteration 5 note about the `SyntaxError: unterminated string literal` on line 112, the VCF file string writes within the notebook source were rewritten to properly use python string escaping for line breaks (`\n`) and nested double quotes (`\"`), preventing actual line breaks from appearing inside the JSON notebook code string literal.
- **Notebook Upload**: The newly crafted JupyterLite notebook (`resistant_specific_snps_v7.ipynb`) has been uploaded to the Galaxy history (`bbd44e69cb8906b5623ea083aa036a1d`) and is ready to be executed.
