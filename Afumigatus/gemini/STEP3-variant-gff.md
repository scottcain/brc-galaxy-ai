# Retrieve variants associated with the cyp51A gene. 

## Goal

Create GFF3 of variant data falling around the cyp51A gene. This gene is known by identifier Afu4g06890.

## Implementation

- Using GTF dataset (history dataset #1) to find coordinates of cyp51A, create a jupyterlite notebook that assembles variants identified in this workflow, mapping from local coordinates to Af293 genomic coordinates where necessary. Each sample's variants should be represented by it's own line in the GFF3. 

Here's the data that should be included in the GFF3:
  - Any SNP calls that are nonsynonomus (ie, from SNPeff runs)
  - Any tandem repeats identified in the promotor region of the gene (from etandem runs)

The jupyterlite notebook should then be uploaded to Galaxy so that it can run in the galaxy context.

## Iteration 1

- Instead of using the a hash for the source to keep the gff lines unique, use the SRA accession that the SNP is identfied in as the source. The element identifiers (ie, the names) of elements in the history are the SRA accessions.

## Iteration 2

- fix this error:
Cell In[1], line 56
    gff_lines = ["##gff-version 3
                 ^
SyntaxError: unterminated string literal (detected at line 56)

## Iteration 3

- Fix this error:
IndexError                                Traceback (most recent call last)
Cell In[1], line 71
     69 vparts = line.split('\\t')
     70 chrom = vparts[0]
---> 71 pos = int(vparts[1])
     72 ref = vparts[3]
     73 alt = vparts[4]

IndexError: list index out of range

## Iteration 4

- While the script executes without crashing (including writing out several progress messages that look promising), no GFF lines get printed out. The only thing that is in the GFF file is the header, including a literal backslash n (ie, "##gff-version 3\n")  

## Iteration 5

- While this now successfully writes GFF, the source of all of the lines is literally "Sample_" with no accession info

## Iteration 6

- fix this error:
Cell In[1], line 56
    gff_lines = ["##gff-version 3
                 ^
SyntaxError: unterminated string literal (detected at line 56)
