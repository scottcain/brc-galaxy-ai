# Step 4: Identifying a set of resistant-specific SNPs 

## Overview

In this task, the SNPs called by SNPeff are compared between the susceptible and resistant samples to identify a set of SNPs that are specific to the resistant samples.

## Tasks 

- Using the MCP server, Galaxy skills and Galaxy history set up in STEP 1, write a jupyterlite notebook that can be executed in the Galaxy history that will create two lists of SNPs (one for the suscptible ones, and one for the resistant ones).
  - From inspection of the GFF from STEP 3, the accessions of the resistant samples are ERR14230100, ERR14230103, and ERR14230105.
  - The susceptible list will be a union of all of the SNPs in any of the suscptible samples.
  - The resistant list will be an intersection of all of the resistant samples.
  - The the lists are compared and any SNPs that are in the resistant list but not in the susceptible list is the final result.
- Here are a few hints that might help:
  -There are collections of both SNP tables and SNP VCFs in the history; it shouldn't really matter which is used.
  - For creating lists, it might be helpful to create a composite key of a few fields so that they can be easily sorted and compared. I suspect the combination of chromosome, location and alt allele would do the trick.

## Iteration 1

- Format the result as VCF so that it can be visualized in a genome browser
- Fix this error:
```
Cell In[1], line 103
    f.write("Chromosome	Position	Ref_Allele	Alt_Allele
            ^
SyntaxError: unterminated string literal (detected at line 103)
```

## Iteration 2

- Fix this error:
```
Cell In[1], line 104
    f.write("##fileformat=VCFv4.2
            ^
SyntaxError: unterminated string literal (detected at line 104)
```

## Iteration 4

- Note that iteration 3 was interactive, addressing the fact that the notebook ran successfully but didn't find any samples which resulted in several logic fixes.
- Fix this error:
```
Cell In[1], line 106
    f.write("##fileformat=VCFv4.2
            ^
SyntaxError: unterminated string literal (detected at line 106)
```

## Iteration 5

The script has the same error that iterations 2 and 4 noted:
Cell In[1], line 112
    f.write("##fileformat=VCFv4.2
            ^
SyntaxError: unterminated string literal (detected at line 112)

