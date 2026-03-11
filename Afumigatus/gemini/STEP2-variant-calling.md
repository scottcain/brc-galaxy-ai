# a Step 2: SRA/ENA Data Retrieval and SnpEff Analysis Plan

# Overview

Using BRC-Analytics.org, set up a Galaxy workflow to retrieve reads from SRA or ENA, run a haploid variant calling workflow, then do tandem repeat calling.

1. Get PRJEB60964 and PRJNA673120 associated with Af293, run haploid variant caller in Galaxy.

2. Use Galaxy tools to do tandem repeat finding:
   a. Use `slice` to extract reads around cyp51A from the BAMs that resulted from "realign reads" step of the variant calling workflow
   b. Use `bedtools bamtofastq` to convert BAM to fastq
   c. Use `nest collection` to make sure assembly happens on a 'per sample' basis
   d. Use SPAdes to assemble the sequence around cyp51A
   e. Use `etandem` with the max repeat size of 70.










# Old and unused/replaced by above

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
 
