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

## Iteration 7

- There is a problem with the tandem repeat section of the code. In the current dataset, there are 3 samples with a tandem repeat, so there should be 3 lines in the gff that correspond to them. There are actaully 9 gff lines, three of which (the "repeat_region" lines)  are not even valid GFF3. The script should be modified to only have one line of GFF per tandem repeat

## Iteration 8

- The notebook throws this error:
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
Cell In[1], line 91
     88                     gff_lines.append(f"{chrom}\t{sra_accession}\tSNP\t{pos}\t{pos}\t.\t.\t.\t{attr}\n")
     90 print("Processing etandem outputs...")
---> 91 all_etandem = await gxy.get(".*etandem on dataset.*", identifier_type="regex")
     92 if not isinstance(all_etandem, list): all_etandem = [all_etandem]
     94 global_offset = 1777374 - 1

File /lib/python3.12/site-packages/gxy/__init__.py:93, in get(datasets_identifiers, identifier_type, history_id, retrieve_datatype)
     91 datatypes_all = []
     92 for ds in datasets:
---> 93     path = await _download_dataset(ds)
     94     file_path_all.append(path)
     95     if retrieve_datatype:

File /lib/python3.12/site-packages/gxy/__init__.py:232, in _download_dataset(dataset)
    230 response = await fetch(url)
    231 if not response.ok:
--> 232     raise Exception(f"Failed to fetch dataset {dataset_id}: {response.status}")
    233 buffer = await response.arrayBuffer()
    234 data = bytes(bytearray(buffer.to_py()))

Exception: Failed to fetch dataset f9cad7b01a472135982e04d23fbd7161: 400

I suspect that is because of the regex looking for *etandem on dataset.* since etandem was run on a *collection* not a single dataset. 

## Iteration 10

- Fix this error:

KeyError                                  Traceback (most recent call last)
Cell In[1], line 59
     56 print(f"Built mapping for {len(mapping)} dataset elements.")
     58 print("Processing SNPeff VCFs...")
---> 59 all_snpeff = await gxy.get(".*SnpEff eff: on collection.*", identifier_type="regex")
     60 if not isinstance(all_snpeff, list): all_snpeff = [all_snpeff]
     62 gff_lines = ["##gff-version 3\n"]

File /lib/python3.12/site-packages/gxy/__init__.py:93, in get(datasets_identifiers, identifier_type, history_id, retrieve_datatype)
     91 datatypes_all = []
     92 for ds in datasets:
---> 93     path = await _download_dataset(ds)
     94     file_path_all.append(path)
     95     if retrieve_datatype:

File /lib/python3.12/site-packages/gxy/__init__.py:217, in _download_dataset(dataset)
    207 """
    208 Given a dataset object, its content is downloaded from Galaxy and stored in Pyodide’s virtual filesystem.
    209 
   (...)
    214     String path of stored file
    215 """
    216 dataset_id = dataset['id']
--> 217 extension = dataset['extension']
    218 hid = dataset['hid']
    219 history_content_type = dataset["history_content_type"]

KeyError: 'extension'
