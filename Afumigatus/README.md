# Aspergillus fumigatus Antifungal Resistance Analysis

This project analyzes genomic data from *Aspergillus fumigatus* isolates to identify molecular mechanisms of azole antifungal resistance. The analysis leverages Galaxy workflows, variant calling pipelines, and custom data analysis notebooks to characterize SNPs and tandem repeat variations in the *cyp51A* gene, which is a primary determinant of azole resistance in this pathogenic fungus.

## Project Overview

The project implements a multi-step genomic analysis workflow based on the COVID-19-associated pulmonary aspergillosis (CAPA) study by Simmons et al. (2023). It retrieves sequencing data from two BioProjects with azole-resistant and azole-susceptible isolates, performs variant calling and tandem repeat analysis via BRC-Analytics, and uses AI-assisted analysis to extract and compare resistance-associated variants.

**Note on AI Implementation**: This analysis was performed using **Google's Gemini AI** rather than Claude, as Claude's usage policies restrict genomic analysis on pathogenic fungi. Gemini provided the comparative analysis and JupyterLite notebook generation for downstream processing of the variant data.

### Key Objectives

1. **Data Retrieval and Preparation**: Obtain SRA/ENA genomic sequencing data for azole-resistant and azole-susceptible *A. fumigatus* isolates (PRJEB60964 and PRJNA673120)
2. **Variant Calling and Tandem Repeat Detection**: Use BRC-Analytics.org workflows in Galaxy to perform quality control, read mapping, haploid variant calling, and tandem repeat finding via SPAdes and etandem
3. **Variant Annotation and Extraction**: Extract and compile variants in and around the *cyp51A* gene (Afu4g06890), including SNPEff annotations and promoter tandem repeats
4. **Comparative Analysis**: Identify SNPs that are specific to azole-resistant samples, contrasting with susceptible samples

## Directory Structure

### `/claude` - Claude AI Analysis (Alternative Approach)

This directory represents an attempted Claude-based analysis approach. Due to Claude's usage policies restricting genomic analysis on pathogenic fungi, the analysis could not be fully completed with Claude's primary models. The directory contains:

- **STEP files**: Task specifications for each analysis phase
- **Jupyter Notebooks**: Multiple iterations of analysis notebooks (`cyp51A_SNP_analysis*.ipynb` v1-v8)
- **Data Files**: Sample accession lists and metadata
- **Reference Material**: Local copy of Simmons et al. (2023) paper and supporting scripts

This represents preliminary exploration and is preserved for reference, but **the actual implemented analysis used Gemini (see below)**.

### `/gemini` - Gemini AI Analysis (Primary Implementation - Completed)

Contains the main analysis workflow completed using **Google's Gemini AI**, which provided the necessary capabilities for genomic analysis of *Aspergillus fumigatus* (a pathogenic fungus). This directory includes the end-to-end implementation from data retrieval through resistance-specific variant identification:

- **STEP files**: Detailed task specifications and execution notes for each analysis phase (STEP1-4)
- **Python Utilities**:
  - `check_collections.py`: Verify Galaxy dataset collections
  - `check_galaxy.py`: Galaxy instance connectivity checks
  - `check_gtf.py`: GTF file validation
  - `count_datasets.py`: Count available datasets
  - `count_org_contributors.py`: Organization contribution analysis
- **Dataset Metadata**:
  - `PRJEB60964.tsv` and `PRJEB60964_detailed.tsv`: BioProject metadata
  - `PRJNA673120.tsv`: Additional BioProject data
- **Galaxy Output**:
  - `Galaxy*-[etandem_*.table/gff`: Tandem repeat analysis results from Galaxy
- **Docker**:
  - `Dockerfile.gemini`: Container setup for Gemini CLI analysis
  - `README-docker.md`: Instructions for running analysis in Docker
- **Presentation**:
  - `presentation_markdown/`: Resources for conference presentation
  - `AsperFest_Presentation.pptx`: Presentation file for Aspergillus meeting

## Analysis Workflow

### Step 1: Galaxy Setup
- Connect to Galaxy instance and verify API access
- Set up Galaxy history for analysis
- Install and configure MCP (Model Context Protocol) server for AI agent integration with Galaxy

### Step 2: Data Retrieval, Variant Calling, and Tandem Repeat Detection
- Retrieve reads from SRA/ENA for PRJEB60964 and PRJNA673120 (associated with *A. fumigatus* Af293 reference)
- Use BRC-Analytics.org workflows in Galaxy to:
  - Run haploid variant calling pipeline for quality control and read mapping
  - Perform SNPEff annotation on identified variants
  - Extract reads around *cyp51A* from BAM files using Galaxy `slice` tool
  - Convert BAM to fastq using `bedtools bamtofastq`
  - Assemble extracted sequences using SPAdes (per-sample basis via `nest collection`)
  - Identify tandem repeats using `etandem` with max repeat size of 70
- Retrieve all variant call results, BAM files, and tandem repeat data from Galaxy history

### Step 3: Variant GFF3 Generation (Gemini AI-assisted)
- Create a GFF3 file capturing all variants in and around the *cyp51A* gene (Afu4g06890)
- Compile nonsynonymous SNPs from SNPEff annotations for each sample
- Include tandem repeats identified in the *cyp51A* promoter region from Step 2
- Use JupyterLite notebook (Gemini-generated) to:
  - Parse GTF annotation to identify *cyp51A* genomic coordinates
  - Process variant datasets from Step 2
  - Map local coordinates to reference genome (Af293) coordinates
  - Generate GFF3 format with sample accessions as identifiers
- Generate output suitable for genome browser visualization (used for JBrowse)

### Step 4: Resistance-Specific SNP Identification (Gemini AI-assisted)
- Compare SNP profiles between azole-resistant and azole-susceptible samples using JupyterLite notebook (Gemini-generated)
- Create union of all SNPs observed in susceptible samples
- Create intersection of SNPs common to all resistant samples (ERR14230100, ERR14230103, ERR14230105)
- Identify SNPs present in the resistant intersection but absent in the susceptible union
- Format results as VCF for visualization in genome browsers (JBrowse)
- Use composite keys (chromosome, position, alt allele) for precise SNP matching across samples

## Key Files and Data

| File | Purpose |
|------|---------|
| `jof-09-01104-v2.pdf` | Reference publication (Simmons et al., 2023) |
| `azole_resistant_*.txt` | Accession lists for resistant isolates |
| `azole_susceptible_*.txt` | Accession lists for susceptible isolates |
| `cyp51A_SNP_analysis*.ipynb` | Iterative SNP analysis and visualization |
| `vcf_datasets.json` | Galaxy VCF collection metadata |
| `STEP*-execution-notes.md` | Detailed progress and implementation notes |

## Prerequisites

- Galaxy account with API access (usegalaxy.org or local instance)
- Galaxy API key stored in `galaxy-key.txt`
- Python 3.x with pandas, matplotlib, seaborn, and numpy
- Access to MCP Server (https://github.com/galaxyproject/galaxy-skills)
- Docker (optional, for containerized analysis)

## Usage

### Run Analysis Steps

Each step directory contains:
1. A specification file (e.g., `STEP1-generic.md`) with task requirements
2. Execution notes documenting progress and findings
3. Supporting scripts and notebooks

Follow the numbered steps in sequence:
```bash
cd /claude  # or /gemini
cat STEP1-generic.md          # Read requirements
cat STEP1-execution-notes.md  # Check progress
# Execute Step 1 tasks...
```

### Working with Jupyter Notebooks

Upload updated notebooks to Galaxy:
```bash
python upload_notebook.py cyp51A_SNP_analysis.ipynb
```

Retrieve collection datasets:
```bash
python get_collection_datasets.py <collection_id>
```

### Docker-based Analysis (Gemini)

```bash
cd /gemini
docker build -t gemini-cli -f Dockerfile.gemini .
docker run -it -v $(pwd):/app -e GEMINI_API_KEY=YOUR_KEY gemini-cli
```

## Data Sources

- **Sequencing Data**: NCBI SRA/ENA databases
  - BioProject: PRJEB60964 (European samples with <100 runs)
  - BioProject: PRJNA673120 (Additional samples)
- **Reference Genome**: NCBI GenBank (*A. fumigatus* Af293 or A1163)
- **Annotations**: UCSC Genome Browser GTF files

## Gene of Interest

**cyp51A** (Afu4g06890): Cytochrome P450 monooxygenase involved in ergosterol biosynthesis. Mutations in this gene are the primary mechanism of azole resistance in *A. fumigatus*.

## Interactive Visualization and Galaxy History

View the analysis results and access the original Galaxy workflow:

**[JBrowse Visualization of cyp51A Region](https://jbrowse.org/code/jb2/latest/?config=%2Fhubs%2Fgenark%2FGCA%2F000%2F002%2F655%2FGCA_000002655.1%2Fconfig.json&session=share-A2MIcQ7aGz&password=ZYmi4)**

This JBrowse session displays:
- SNPs and tandem repeats identified around the *cyp51A* locus
- Resistant-specific SNPs identified in Step 4 analysis
- Reference annotations and genomic context
- Comparative data across resistant and susceptible samples

**[Galaxy History: Aspergillus fumigatus Variant Analysis](https://usegalaxy.org/u/scottcain/h/a-fumigatus-variants)**

Access the complete Galaxy workflow history containing:
- Variant call results from BRC-Analytics
- SNP annotations and tandem repeat data
- JupyterLite notebooks for Steps 3 and 4
- All intermediate datasets used in the analysis

## Analysis Outputs

- **GFF3 file** (*cyp51A* variants): Comprehensive annotation of SNPs (from SNPEff) and tandem repeats in and around the *cyp51A* locus (Step 3)
- **VCF file** (resistant-specific SNPs): Variants present in azole-resistant samples but absent in susceptible samples, formatted for genome browser visualization (Step 4)
- **JupyterLite notebooks**: Reproducible analysis notebooks uploaded to Galaxy for:
  - Variant extraction and GFF3 generation from GTF and variant datasets (Step 3)
  - Comparative SNP analysis identifying resistance-associated variants (Step 4)
- **Interactive JBrowse visualization**: Online genome browser session displaying SNPs, tandem repeats, and resistant-specific variants in genomic context
- **Accession classifications**: Lists of azole-resistant and azole-susceptible sample accessions

## Contributing

This is an active research project. Updates to analysis methods, additional sample processing, or alternative approaches should be documented in the STEP execution notes files.

## License

Project structure and custom scripts are provided as-is. Refer to original publications and data repositories for licensing terms on genomic data and external tools.

## Contact

For questions about analysis workflow or data interpretation, refer to the Simmons et al. (2023) publication and Galaxy skills documentation.

## References

Simmons, S., et al. (2023). COVID-19-associated pulmonary aspergillosis (CAPA): Genomic analysis of *Aspergillus fumigatus* isolates. Journal of Fungi.

Related Resources:
- Galaxy Skills: https://github.com/galaxyproject/galaxy-skills
- NCBI SRA Database: https://www.ncbi.nlm.nih.gov/sra
- ENA Browser: https://www.ebi.ac.uk/ena
- UCSC Genome Browser: https://genome.ucsc.edu
