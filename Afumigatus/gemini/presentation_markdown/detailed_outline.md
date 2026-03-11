# Detailed Outline: AsperFest Slide Presentation

## 1. Introduction
*   **Speaker Introduction**: Brief background about yourself.
*   **Talk Objective**: Reproducing the computational analysis of the paper *jof-09-01104-v2.pdf*. When mentioning the paper, create a graphic which is the screenshot of the top of the paper. (I can't refer to it using the file name--nobody would know what that is.)
*   **Scope**: Focus on variant calling and identifying specific mutations related to Azole resistance in *Aspergillus fumigatus*.

## 2. Platforms Overview
*   **BRC-Analytics**: Introduction to the platform, its purpose, and how it links to Galaxy.
*   **Galaxy Platform**: Brief overview of Galaxy as a reproducible bioinformatics workflow environment.

## 3. Setting Up Analysis in BRC-Analytics
*   **Navigating the Portal**: Go to [brc-analytics.org](https://brc-analytics.org/).
*   **Locating the Organism**: 
    *   Navigate to "Organisms".
    *   Filter and search for "Aspergillus fumigatus".
*   **Configuring the Analysis**:
    *   Select "Aspergillus fumigatus" and click "Analyze".
    *   Choose "Variant calling".
    *   Configure inputs by entering the SRA/ENA Accessions from two BioProjects (demonstrate pasting the two BioProject accessions).
    *   *[Insert Screenshot]* Show clicking the "select all" checkbox to easily select all 22 corresponding sequencing runs (18 from one project, 4 from the other).
    *   Click "Launch In Galaxy" to seamlessly transfer the context.

## 4. Running the Haploid Variant Caller in Galaxy
*   **Workflow Initialization**:
    *   Once in Galaxy, open the pre-configured workflow for "Paired End Reads".
    *   Select the collection containing the 22 paired-end datasets.
    *   Execute the "Run Workflow" command to initiate the standard variant calling steps (e.g., fastp quality control, mapping, variant calling).

## 5. Extracting and Processing cyp51A Reads
*   **Slicing BAM Files**:
    *   Use the "BAM by genomic regions" tool (slice).
    *   Input target coordinates for *cyp51A* (e.g., `NC_007197.1` / `NC_007196.1`).
    *   Run on the 22 BAM datasets and rename the output collection to "cyp51A-associated reads".
*   **Conversion and Assembly**:
    *   Convert sliced BAMs to FASTQ using "bedtools Convert from BAM to FastQ" (set datatype to `fastqsanger`).
    *   Nest the collection ("preassembly data reorg").
    *   Run "SPAdes" (genome assembler) on the paired/interlaced reads to assemble scaffolds.
*   **Finding Tandem Repeats**:
    *   Run "etandem" on the SPAdes scaffolds collection to identify tandem repeats in the promoter regions.
*   **Visual Check**: *[Insert Screenshot]* JBrowse visualization showing the variants in the *cyp51A* region.

## 6. AI-Assisted Scripting: cyp51A Variants GFF3
*   **Using Gemini**: Explain how Gemini CLI was used to iteratively build a JupyterLite notebook (`variants_cyp51A.ipynb`).
*   **Notebook Execution**:
    *   Run the notebook within Galaxy's JupyterLite interactive environment.
    *   The notebook dynamically extracts variants and tandem repeats and maps them back to their specific SRA accessions.
*   **Output**: Generates a combined GFF3 file (e.g., `cyp51A Combined Variants (By SRA)`). Rename for clarity ("cyp51A variant script output (GFF)").

## 7. AI-Assisted Scripting: Finding Resistant-Specific SNPs
*   **Identifying Phenotypes**: Show the GFF output to identify the specific accessions for resistant samples (e.g., ERR14230100, ERR14230103, ERR14230105).
*   **Using Gemini**: Explain how Gemini was used to write a second JupyterLite script.
*   **Set Operations**:
    *   Script performs a *union* of all SNPs in susceptible samples.
    *   Script performs an *intersection* of SNPs across the resistant samples.
    *   Calculates the set difference to find mutations uniquely present in the resistant strains.
*   **Output & Visualization**: 
    *   Notebook outputs the `Resistant Specific SNPs (VCF)`.
    *   *[Insert Screenshot]* JBrowse visualization highlighting these resistant-specific SNPs.

## 8. Conclusion
*   **Summary of Findings**: Briefly recap the identified mutations and their correlation with the original paper.
*   **The Power of AI + Galaxy**: Final thoughts on how integrating AI tools like Gemini with platforms like BRC-Analytics and Galaxy drastically accelerates reproducible research.
