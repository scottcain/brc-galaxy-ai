# Step 2: SRA/ENA Data Retrieval and SnpEff Analysis Plan

## Overview
This step focuses on retrieving Aspergillus fumigatus genomic data from SRA/ENA databases and preparing for (but not performing) SnpEff variant annotation, based on the COVID-19-associated pulmonary aspergillosis (CAPA) study by Simmons et al. (2023) (local copy of the paper: jof-09-01104-v2.pdf).

## Prerequisites

- MCP created in STEP1-generic.md
- Skills outlined in STEP1-generic.md.
- The Galaxy history defined in STEP1-generic.md

## Tasks 

- Read the Simmons paper in this directory (jof-09-01104-v2.pdf)
- Identify, obtain and upload the appropriate referernce genome from NCBI
- Identify, obtain and upload the appropriate GTF annotation file for this genome from UCSC (note that searching UCSC Genome Browser downloads generally works best if you use the NCBI RefSeq accession)
- Identify BioProjects in the paper, ignoring the one that has over 100 samples. 
- Create SRA accession lists for resistant/susceptible samples
  Method details:
    - Access ENA database directly for bioproject with <100 samples
    - Extract actual ERR/SRR accession numbers (NOT sample names)
    - Cross-reference with paper metadata to categorize resistance
    - Upload ONLY accession number lists to Galaxy and name them appropriately
 
