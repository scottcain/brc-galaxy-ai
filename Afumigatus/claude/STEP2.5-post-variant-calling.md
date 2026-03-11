# Step 2: SRA/ENA Data Retrieval and SnpEff Analysis Plan

## Overview
This step focuses on retrieving Aspergillus fumigatus genomic data from SRA/ENA databases and preparing for (but not performing) SnpEff variant annotation, based on the COVID-19-associated pulmonary aspergillosis (CAPA) study by Simmons et al. (2023) (local copy of the paper: jof-09-01104-v2.pdf).

## Prerequisites

- MCP created in STEP1-generic.md
- Skills outlined in STEP1-generic.md.
- The Galaxy history defined in STEP1-generic.md

## Tasks 

- Read the Simmons paper in this directory (jof-09-01104-v2.pdf)
- Identify and obtain the appropriate referernce genome from NCBI
- Identify and obtain the appropriate GTF annotation file for this genome from UCSC (note that searching UCSC Genome Browser downloads generally works best if you use the NCBI RefSeq accession)
- Identify BioProjects in the paper, ignoring the one that has over 100 samples. 
- Use the BioProjects to identify the SRA accessions of individual samples.
- Using the metadata for the samples, combined with information in the paper, categorize the samples that are either resistant or susceptible to Azole.
- Fetch the sequences to the history defined in Step 1 from either SRA or ENA, verify successful download, and create two collections for the reads, one for resistant, one for susceptible.  Likely the best way to achieve download would be with a workflow that allows parallel downloads from ENA. The workflow is called "Parallel accession download ENA" and takes a parameter for number accessions for a single download job--that number can be kept at 1.
- Run the Galaxy IWC Haploid Variant Calling Workflow on both collections.
 
## Iteration 1

- Added notes to make download from ENA more likely to be successful.
