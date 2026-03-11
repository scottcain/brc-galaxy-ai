# Retrieve variants associated with the cyp51A gene. 

## Goal

Identify variants falling within the cyp51A gene. This gene is known by identifier Afu4g06890.

## Implementation

- Using GTF dataset (history dataset #4) create a jupyterlite notebook That shows the genomic neighborhood of this gene. 
- It should look like a heat
## Iteration 1

- VCF files for the samplesmap where on the x-axis there are genomic coordinates, and squares of the heat map represent individual  nucleotides of coding regions of the gene numbered as local coordinates, starting with the first nucleotide of the coding region of the gene. 
- Upload notebook, I will check it and will iterate. 

## Iteration 1

- VCF file collections for the samples are in history #450 and #351; these should be used for generating the heatmap

## Iteration 2

- This module not found error occurred; what can I do to rectify it:
```
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 3
      1 import pandas as pd
      2 import matplotlib.pyplot as plt
----> 3 import seaborn as sns
      4 import numpy as np
      5 from matplotlib.patches import Rectangle

ModuleNotFoundError: No module named 'seaborn'
```

## Iteration 3

- the notebook is giving this error: `⚠️ GTF file not found. Available files:
[]
✗ No GTF file available`. Check the syntax for accessing data in previous history steps.

## Iteration 4

- This path isn't working. Consider the notebook at https://raw.githubusercontent.com/nekrut/agenticGxy-ms/refs/heads/main/Cauris/var/SCF1_heatmap.ipynb and extract useful patterns. The most obvious of which is the `gxy` library.

## Iteration 5

- The notebook errors when trying to access collections; perhaps that isn't supported. Use the MPC server to get history items for the VCF elements of the collections to access them directly in the notebook.

## Iteration 6

- The VCF loading is limited to 1000 variants, however most of these VCF files have over 100,000 variants. Fix this so that the gene region of interest can be found.

## Iteration 7

- Filter out SYNONYMOUS_CODING variants
- Analyze all 18 VCF files
- Generate an actual graphical heatmap

## Iteration 8

- In iteration 1, the history IDs containing VCFs were identified, from which individual VCF files were identified. Those IDs found are the wrong ones. The members of the #450 and #351 collections are the result of running SNPeff and therefore have EFF annotations. The VCFs from the history IDs that have been used up to now are for the VCFs before SNPeff was run.
