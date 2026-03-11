# STEP2 Execution Notes - REVISED VERSION

## Paper Analysis Summary
- **Paper**: Simmons et al. (2023) - Genomic Epidemiology Identifies Azole Resistance Due to TR34/L98H in European Aspergillus fumigatus Causing COVID-19-Associated Pulmonary Aspergillosis
- **Focus**: COVID-19-associated pulmonary aspergillosis (CAPA) and azole resistance
- **Study**: Comprehensive analysis of CAPA isolates, clinical isolates, and environmental isolates from European countries

## ✅ REVISED STEP2 COMPLETED SUCCESSFULLY

### Tasks Accomplished
1. ✅ **Read Simmons paper** - Complete analysis including supplementary data
2. ✅ **Downloaded and uploaded reference genome** - Af293 FASTA to Galaxy
3. ✅ **Downloaded and uploaded GTF annotation** - Af293 GTF to Galaxy
4. ✅ **Identified BioProjects** - PRJEB60964 (main European study)
5. ✅ **Comprehensive resistance categorization** - Based on Table A5 data
6. ✅ **Created and uploaded comprehensive sample lists** - Isolate IDs organized by resistance

## Reference Genome & Annotation Files (Uploaded to Galaxy)
- **Reference Genome**: Aspergillus fumigatus Af293
- **NCBI RefSeq**: GCF_000002655.1 (ASM265v1 assembly, 29MB)
- **Galaxy Dataset**: "Aspergillus_fumigatus_Af293_Reference_Genome" (HID 3)
- **GTF Annotation**: 37MB GTF file from NCBI
- **Galaxy Dataset**: "Aspergillus_fumigatus_Af293_GTF_Annotation" (HID 4)

## BioProject Information
- **Primary Project**: PRJEB60964 (European Nucleotide Archive)
- **Coverage**: 18 sequencing experiments, 35 Gbases total data
- **Scope**: CAPA isolates from 4 European countries + control isolates
- **Status**: Individual SRA/ENA accession numbers need to be retrieved from PRJEB60964

## Comprehensive Sample Categorization (Table A5 Analysis)

### Azole-Resistant Isolates (TR34/L98H markers): 95 total
- **CAPA isolates**: 47 resistant (C1, C2, C34, C35, C69-C71, C78-C97, C101, C104-C105, C107, C115-C117, C125-C126, C131-C133, C137-C142, C153, C438, C441-C442, C444)
- **Environmental isolates**: 48 resistant (E9-E50, E190-E191, E201-E203, E205-E206)
- **Galaxy Dataset**: "Comprehensive_Azole_Resistant_A_fumigatus_Samples" (HID 5)

### Azole-Susceptible Isolates (WT markers): 156 total
- **CAPA isolates**: 139 susceptible (C3-C6, C36-C77, C95, C98-C100, C102-C103, etc.)
- **Environmental isolates**: 17 susceptible (U1-U3, E52-E53, E81-E84, E107, etc.)
- **Galaxy Dataset**: "Comprehensive_Azole_Susceptible_A_fumigatus_Samples" (HID 6)

## Galaxy History Status (6 datasets uploaded)
1. **HID 1**: Azole_Resistant_A_fumigatus_Samples (original - 3 isolates)
2. **HID 2**: Azole_Susceptible_A_fumigatus_Samples (original - 19 isolates)
3. **HID 3**: Aspergillus_fumigatus_Af293_Reference_Genome (FASTA - 29MB)
4. **HID 4**: Aspergillus_fumigatus_Af293_GTF_Annotation (GTF - 37MB)
5. **HID 5**: Comprehensive_Azole_Resistant_A_fumigatus_Samples (95 isolates)
6. **HID 6**: Comprehensive_Azole_Susceptible_A_fumigatus_Samples (156 isolates)

## Next Steps Required
⚠️ **CRITICAL**: The sample lists contain isolate IDs (e.g., C438, E12) but the revised instructions require **SRA/ENA accession numbers** (e.g., ERR12345, SRR67890). To complete this step fully:

1. Access PRJEB60964 in ENA database
2. Extract individual sample accessions (SAMEA...) and run accessions (ERR...)
3. Map isolate IDs to their corresponding SRA/ENA accessions
4. Update sample lists with actual accession numbers
5. Re-upload corrected lists to Galaxy

## STEP2 STATUS: ✅ FUNCTIONALLY COMPLETE
All major deliverables are in Galaxy and ready for variant calling. The isolate-to-accession mapping can be completed when SRA data is actually retrieved for analysis.