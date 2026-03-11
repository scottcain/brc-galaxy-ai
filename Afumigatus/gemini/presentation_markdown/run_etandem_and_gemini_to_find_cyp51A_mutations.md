# Process Fungal Genome Data and Identify Tandem Repeats
#### [Made by Scott Cain with Scribe](https://scribehow.com/shared/Process_Fungal_Genome_Data_and_Identify_Tandem_Repeats__Rik2faHXTMSbBO9rs_Pf4w)
Learn how to process fungal genome data using Galaxy. This guide walks you through assembling genomes with SPAdes, converting BAM to FASTQ, and identifying tandem repeats with eTandem to generate variant data.

1\. Navigate to [https://usegalaxy.org/workflows/invocations/385aebf4459522ba?success=true](https://usegalaxy.org/workflows/invocations/385aebf4459522ba?success=true)

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/8d9882bc-6741-4af0-960c-83990d408007/ascreenshot_0147956823cb4d13b1841c275b5b1a4a_text_export.jpeg)


2\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/8d9882bc-6741-4af0-960c-83990d408007/ascreenshot_910128be79b64c32bc39a4487e5a8ae9_text_export.jpeg)


3\. Click the "search tools" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/ea7244d2-961b-4fd5-b5fb-c13cd7c88406/ascreenshot_9062151ce6e842ca86bfea273e8784a5_text_export.jpeg)


4\. Type "slice"


5\. Click "BAM by genomic regions"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/c751fefd-6382-4406-8ac0-0528e512409b/ascreenshot_41c3c8f386df449992cb5f0833e3e1e9_text_export.jpeg)


6\. Click "using a list of intervals from a BED dataset"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/f54c4815-76f4-4671-ad3c-48f427b2d95f/ascreenshot_d2bbde3aef4a4317a485d1908df7b778_text_export.jpeg)


7\. Click "by chromosomes/contigs and coordinates"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/fcb4375c-715a-4bc6-a0ed-b93c0f4b8aaf/ascreenshot_9d28240d026a488c9d7d5ffd1f21caac_text_export.jpeg)


8\. Click "Insert Regions"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/8bbbb99f-6647-4d4f-a47f-6ec80db84771/ascreenshot_bff61d290289476c9598572c3fb72ef0_text_export.jpeg)


9\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/8e30811f-08b7-48bb-a7b1-f83cddb272c2/ascreenshot_7cfbdc7549a94a1ba5fe9cc1e3a2b0c1_text_export.jpeg)


10\. Click "NC_007196.1"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/957d3977-0b75-483c-852e-69880c70e1c0/ascreenshot_5c90339f382c4dc9a4e73380ce53ff57_text_export.jpeg)


11\. Click "NC_007197.1"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/dbfdc11d-e3c7-41b4-8dbe-3961521faa3b/ascreenshot_fa586da803b54e6e8f1a59558ada0037_text_export.jpeg)


12\. Double-click this number field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/99926e38-e9f5-4af5-bed1-211d7b1b3a34/ascreenshot_396fe77107cc4e70b53a3e4c26fd7f18_text_export.jpeg)


13\. Press [[cmd]] + [[v]]

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/42a10875-e1ec-40f8-8d33-5f1619a9ac31/ascreenshot_005500558c404407bc11e59f3cdeeea1_text_export.jpeg)


14\. Double-click this number field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e4e4a24e-8bf2-4f87-b4c4-53840d0dbd2f/ascreenshot_a7705b9577f44ebc93a670541c926bbe_text_export.jpeg)


15\. Press [[cmd]] + [[v]]

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/96ed6b1a-7a13-4cd0-a35c-a8c2006d46fd/ascreenshot_20779b21c131450ea0cd89f2f067c94d_text_export.jpeg)


16\. Click "Regions move up move down Minimum number of Regions fields reached 1: Regions Select references (chromosomes and contigs) you would like to rest..."

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/087e2232-2503-48fa-b06d-3b8538e0386f/ascreenshot_5f2a14662687485a8a6f68e4ffef5d38_text_export.jpeg)


17\. Click "Run Tool"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/1e047cb7-8e47-4095-9ad4-c1a139ad88cd/ascreenshot_436623a3fa614f29a0548e1c53d74b03_text_export.jpeg)


18\. Click "a list with 22 bam datasets"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/b4eec853-6c3a-45d8-aea9-46157d109edc/ascreenshot_eb81549c387c4b788f118f921f17643b_text_export.jpeg)


19\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/09e4eaab-2cf4-4b09-8107-64145d2e716d/ascreenshot_fa0796e0f18041f7b9c51c9b9f829959_text_export.jpeg)


20\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/11c04475-ca92-4645-88a7-15d011b50619/ascreenshot_3c7c5b2b87634db9a704b1d9763f7531_text_export.jpeg)


21\. Double-click the "Name" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/b9cb2084-e7e9-499d-a677-50ee136d269b/ascreenshot_b48c3f917adc4be28b26e79bb1a059cc_text_export.jpeg)


22\. Type "cyp51A-associated reads"


23\. Click "Save"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/75a745aa-889c-4288-9556-6e98977715c2/ascreenshot_afa440f0fa9f42018779d35926efbcc7_text_export.jpeg)


24\. Double-click the "search tools" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/34a360f7-05fb-43f3-843b-284b7bf01a77/ascreenshot_330231abf1f04c51a3eb5ebe55b5c59a_text_export.jpeg)


25\. Type "spades"


26\. Click "SPAdes"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/54086788-48e6-4862-b518-aed6c2fe2490/ascreenshot_023022b79d5449e8a4610ba4a23c0e21_text_export.jpeg)


27\. Double-click the "search tools" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/b7150ae6-15ed-46c8-9d16-35fbe526f836/ascreenshot_4dc6dfae729345749444bfdf030d8f65_text_export.jpeg)


28\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/2915ed8a-54c1-4ca4-866c-b688405a83b9/ascreenshot_96567bcb66084db48455ddee55bc3d08_text_export.jpeg)


29\. Click "Collection Operations"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/f4c68222-0b8e-4f78-8255-319acaee21ab/ascreenshot_29b769e365cd41b68f85bcc81bb9d7ab_text_export.jpeg)


30\. Click "Nest collection"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/0aacf963-a7e1-4b2c-ad62-d06e9d6eb5af/ascreenshot_8f26b0d7c2174e45b62b21126b91ebcc_text_export.jpeg)


31\. Click "Run Tool"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/cad9c3bd-37cd-40bc-a916-35822cdedcc9/ascreenshot_bfacb317a5994fd7be4b79cae6a77f7a_text_export.jpeg)


32\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/50a057a5-b4ea-411d-95bf-201f826d3960/ascreenshot_03b0aedbce7341fe94b71988804e976e_text_export.jpeg)


33\. Double-click the "Name" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/23f73f36-c267-444b-960d-026f2c45079e/ascreenshot_cc3f7c76634342babb0118978ea6b1f7_text_export.jpeg)


34\. Type "preassembly data reorg"


35\. Click "Save"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/fb0a8ddc-13b1-43ec-8900-972d8f813274/ascreenshot_730b4ebca3c84decbb86c97aefafae72_text_export.jpeg)


36\. Double-click the "search tools" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/502da4a1-b8f3-4434-bbb1-0b64298991d5/ascreenshot_004463456a5d4f1993eefcc410a6f0b8_text_export.jpeg)


37\. Type "spades"


38\. Click "genome assembler for genomes of regular and single-cell projects"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e065c42a-c0bc-4b78-a95d-7f1e5be9be5c/ascreenshot_1a94270d1d3e4a099e9b9f0b0133bb57_text_export.jpeg)


39\. Click "48: fastp on collection 47: Paired-end output"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/062adcae-b2a0-43c1-b349-a902c0d77740/ascreenshot_4b79717e95994341b245f67c395ef6cd_text_export.jpeg)


40\. Click "It assumes that all samples belong to the same library. If you want to use samples from two different libraries, include the second library as a..."

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/b8f37206-5a86-4aa8-b586-b0ba8ce49143/ascreenshot_dfaf104f394a414990c48d870311ff44_text_export.jpeg)


41\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/003b32f2-b845-401a-a4f5-488ff8b021dd/ascreenshot_38bf84b43e674b34a1ce253851540089_text_export.jpeg)


42\. Click "FASTA/FASTQ file(s): collection * accepted formats 48: fastp on collection 47: Paired-end output Type of paired-reads * Default (--pe) In paired..."

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/41c98698-2959-411f-8f6a-5203e0b3e856/ascreenshot_db97236ca45444fe827f59d05abf333b_text_export.jpeg)


43\. Double-click the "search tools" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/af17a7bd-a788-4358-9d2c-cdd665dc2f89/ascreenshot_93ab580547c44141b15649d232535b0e_text_export.jpeg)


44\. Type "bedtools convert"


45\. Click "bedtools Convert from BAM to FastQ"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/947df579-44d7-4fe7-b78d-9bdc4e1c7e0b/ascreenshot_327e800a79c741d8ab0a725805788e99_text_export.jpeg)


46\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/d2768660-ff1f-4882-91a1-e121703260c4/ascreenshot_61246cd1bddf408e9018291addd5470a_text_export.jpeg)


47\. Click "Run Tool"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/09d88a4a-b46f-4875-b485-7650b17f5f3c/ascreenshot_f7d9469ceedf4482af5e9261aa0d6b03_text_export.jpeg)


48\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/acc5b0be-4591-464b-b509-8dd0ab17b5a3/ascreenshot_be74a7bb927b438facd4b706a5f0f597_text_export.jpeg)


49\. Click "Datatypes"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/4ef2c543-04aa-47d0-945f-d2c8a2da2fd1/ascreenshot_89e805a512c2497a8d67352c7ea5b5af_text_export.jpeg)


50\. Click "fastq"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/948fac6a-d769-46cd-85f5-dee2e3365ed2/ascreenshot_758adbab27ee43cb8f7ccf3120dbfd23_text_export.jpeg)


51\. Type "sanger"


52\. Click "fastqsanger"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/d020a150-1e07-42ef-a1d6-963e48e6ca96/ascreenshot_f0c395880c9b4bb283f4c52790d08f86_text_export.jpeg)


53\. Click "Save"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/98e4ffa7-e30b-483f-93c3-d895be82f0c4/ascreenshot_fba81df74f1342ac87d255ab0dcc1559_text_export.jpeg)


54\. Double-click the "search tools" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/6e2418d7-72bf-4e86-b399-492234324959/ascreenshot_677082d173864c9ab7d910cca064fac5_text_export.jpeg)


55\. Type "spa"


56\. Click "genome assembler for genomes of regular and single-cell projects"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/8aa053ff-2864-4ec4-8733-379b9a1f126a/ascreenshot_850b8dc2af1946a3811bba47a22bb1f5_text_export.jpeg)


57\. Click "48: fastp on collection 47: Paired-end output"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/c408f67f-e7c7-412f-bb60-686ab73a71c9/ascreenshot_ccbf01d0b4c54eeea3f8c3743a21775c_text_export.jpeg)


58\. Click "Type of paired-reads *"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/7ce5b5b5-0369-4a36-9d2e-39033d82bdf0/ascreenshot_57bba1d4b8964340984c1ef63b840b6f_text_export.jpeg)


59\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/61c8dbbc-4a6b-4072-abae-468f7430dc44/ascreenshot_279ddcf87dbe44c68be9390951eb114b_text_export.jpeg)


60\. Click "Single-end or paired-end short-reads"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/ac548351-ab9b-470f-bb75-396ae3cadcf4/ascreenshot_28037f46fbcb43648bfd4ba90cf1f4f6_text_export.jpeg)


61\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/06f93693-09ce-4f2b-a273-79cf842eb732/ascreenshot_989c7c3fbce040fb875f2b701c87ce49_text_export.jpeg)


62\. Click "Add to Favorites Versions Options Copy Link Copy Tool ID View Tool source See in Tool Shed Generate Tour Run Tool Run tool: SPAdes (4.2.0+galaxy..."

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/1dc5e5ee-6be1-46ce-9777-5b76b0974980/ascreenshot_1706b3de35da472e9b933689912700cf_text_export.jpeg)


63\. Click "Paired-end: list of dataset pairs"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e453bd31-4add-40b4-b586-e45a2d565e85/ascreenshot_1d73fc724e6e4633939ff3c237db9ece_text_export.jpeg)


64\. Click "Paired-end: interlaced reads"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/0a5b29a4-28f2-4d03-9c37-fb4adaa47375/ascreenshot_31a5fc593d34422b913fbbafadf32b66_text_export.jpeg)


65\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/2dfc91f2-7eb6-4fa7-ad92-259c45949196/ascreenshot_3acf3f3b67994c1d87b078051a3e20f0_text_export.jpeg)


66\. Click "It assumes that all samples belong to the same library. If you want to use samples from two different libraries, include the second library as a..."

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/cd8f751f-0677-42c6-9de3-a7e2d51643d2/ascreenshot_3c06345f473d4067844579c9cc9895a9_text_export.jpeg)


67\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/2a971500-68fa-4012-9051-de4126c47c17/ascreenshot_dcf6195af80d4961903741a8d83c53e6_text_export.jpeg)


68\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e8a81768-6e33-4bd2-9075-b3e0c9cf3e6d/ascreenshot_7ebde74798a64023ae38e4e040c9fd74_text_export.jpeg)


69\. Click "447: preassembly data reorg (as FASTQ)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/caa03a3a-ead5-4b5f-9abe-6638bf470694/ascreenshot_c0c561d3215b4ef897ec88ade1eac15b_text_export.jpeg)


70\. Click "FASTA/FASTQ file(s): interlaced * ... accepted formats 447: preassembly data reorg (as FASTQ) 447: preassembly data reorg (as FASTQ) switch to c..."

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/62348314-1adb-4335-916a-74a05ca0213e/ascreenshot_f8f7c7058fe7477783ac51b8933c9132_text_export.jpeg)


71\. Click "Run Tool"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/5946a081-fb10-4d67-8974-d1caa0df91e4/ascreenshot_4ed481cc63844d4ca85b9a96fbb4bbeb_text_export.jpeg)


72\. Click "SPAdes on collection 447: Scaffolds"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/98b3d5cb-5229-49f7-aa31-b02b517a70b4/ascreenshot_984e725506cb438d86afc52de9d607a9_text_export.jpeg)


73\. Click "An error occurred with this dataset. 18: ERR14230093"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/d9a21a7d-45d5-4642-9b25-6d6d4f16524a/ascreenshot_cf9985fe12d04359b139a40068c36573_text_export.jpeg)


74\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/363f93c9-adc2-425f-9575-780c597092d2/ascreenshot_c99c3a47fb8945c4bb805ef430effa15_text_export.jpeg)


75\. Click "An error occurred with this dataset. 470: SPAdes on collection 447: Assembly graph"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/27c4cd5b-e009-4077-b76b-85b0476a148e/ascreenshot_14c262a22e034fc29a5ed4f53883ef16_text_export.jpeg)


76\. Click "An error occurred with this dataset. 7: ERR14230096"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/70f09f84-7e9d-46f2-aa85-316a92764406/ascreenshot_417df404767a44afa5ab8e7fc5b74536_text_export.jpeg)


77\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/53851a58-f07b-4e51-bf4b-8f618a8177f5/ascreenshot_7d54445c6b444efba344aca3c9e1868f_text_export.jpeg)


78\. Click "1: ERR14230090"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/f327f52d-0f7b-4ede-b8f4-878227e9f7b1/ascreenshot_bcd7c2ae992a4371aa3850f82a7b344b_text_export.jpeg)


79\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/1b7e9ba5-32d1-4daf-afaf-140e170f43c7/ascreenshot_625caa08c51d47abad7d0663e80c9686_text_export.jpeg)


80\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/80ba8901-e0f2-480b-814c-8677125ccd1a/ascreenshot_4af081725d354489b05ab4c1ef1f4b73_text_export.jpeg)


81\. Click "Collection and elements"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/f6b085b4-dbcd-4473-92d0-5ff6aa411c85/ascreenshot_1691df91c9774ab59811f9280794c1d3_text_export.jpeg)


82\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/6b081fdf-3341-4f98-8c0e-a9fd5f079cd3/ascreenshot_8881aef1d4c74436ac0330fa5bbaac0a_text_export.jpeg)


83\. Click "a list with 22 txt datasets"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/f2f217d0-bd35-4ea6-b52e-8fd7ea5977eb/ascreenshot_582d4f7eefeb4d9898f08852e4c3f752_text_export.jpeg)


84\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/85458848-953e-48f0-ae6f-44dd757f4859/ascreenshot_f61b27a2c5b84a24a1058c2cb399ed99_text_export.jpeg)


85\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/15f12b3d-6e49-4ad7-87ae-76bc56134b19/ascreenshot_17eefec2b9294d09a0662cb85513cde0_text_export.jpeg)


86\. Click "Collection and elements"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/5b66677b-1a7c-489a-ac77-028c2e169830/ascreenshot_6ade1ec9b0474fb7a62955b6b29632a6_text_export.jpeg)


87\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/4bbe57f8-391b-43db-a0de-03694f24cc8c/ascreenshot_ba5de75743fa491e91b9a0f7dacf26ea_text_export.jpeg)


88\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/c116aad3-e210-4ee6-a7f7-45847b3fea48/ascreenshot_c0e8ff47246d4e3ab614f1fef2611edd_text_export.jpeg)


89\. Click "Collection and elements"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/7155c7af-cf25-45b9-8dda-af6299cea779/ascreenshot_7c96ba9137024db5b0ec05f49602045d_text_export.jpeg)


90\. Click this button.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/ec558667-794c-4a85-9e93-8c8fa8b94aae/ascreenshot_e81cc23cab7a475392402f38f06f57b0_text_export.jpeg)


91\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/6414d4e6-3bfd-4b78-a950-bacc0585c2bd/ascreenshot_63a87290c0b54ca8a56af87e58bf6b43_text_export.jpeg)


92\. Click "Collection and elements"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/709fbb73-47a6-4049-b790-e84047a6afef/ascreenshot_d2f4bf98439b4eec9b379baa0f4dceb2_text_export.jpeg)


93\. Click "genome assembler for genomes of regular and single-cell projects"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/2b432183-89b1-4a00-a4ad-004997ac0a0d/ascreenshot_94c013c2808a46fdaffc5a0379693ce6_text_export.jpeg)


94\. Click "48: fastp on collection 47: Paired-end output"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/91404c4a-6307-4402-95d4-5625215908ec/ascreenshot_227fa259a6f34705822ed74bfc0e8692_text_export.jpeg)


95\. Click the "Select a dataset collection" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/6da68fdc-e5dd-4c37-a205-d9acb5c596e8/ascreenshot_7ad8a571907c4d59973dc43c708850ac_text_export.jpeg)


96\. Click "It assumes that all samples belong to the same library. If you want to use samples from two different libraries, include the second library as a..."

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/a555ecdb-d10b-47a7-98eb-1968e5ce7ea4/ascreenshot_cc53fe2079fe44c5881f9177b6bc3e84_text_export.jpeg)


97\. Click "Assembly and error correction"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/55170c6e-1c75-4fc8-a8d4-4a7ee706e2e5/ascreenshot_b67b2fa21f5946969697ee7caf7bd67a_text_export.jpeg)


98\. Click "Assembly and error correction"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e2c778b7-002a-47ac-898d-f96bdf7619a7/ascreenshot_3b99c3240c494ab3bee8a41572f7fa39_text_export.jpeg)


99\. Click "Paired-end: list of dataset pairs"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/f9aeaa79-872a-4891-87ba-adccd1044878/ascreenshot_bd01624539624e49b1ffda691728bac6_text_export.jpeg)


100\. Click the "Select Value" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/97c4c869-f313-41ac-8a38-a8dfcd9b6a76/ascreenshot_da8f490604f3433ca09b1b0f385c3aad_text_export.jpeg)


101\. Click "Type of paired-reads"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/b5547f6d-4785-4955-836a-3356b66f0e52/ascreenshot_c2092590ec904eb3b75bac3e18dd4a18_text_export.jpeg)


102\. Click "48: fastp on collection 47: Paired-end output"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/40e45587-1e2b-4d67-a582-a7ed39d69968/ascreenshot_51daabec97d248fc8ab6c574cddc502e_text_export.jpeg)


103\. Click "Type of paired-reads *"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/558b058f-c21a-4b86-9816-d143375d95da/ascreenshot_663e78c1b85749739ce815ac78410942_text_export.jpeg)


104\. Click "Paired-end: list of dataset pairs"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/dbc7c790-b4e6-426b-bfd2-2ba1bcc7128f/ascreenshot_ed566f9551e54ce0a4e93a21d129309a_text_export.jpeg)


105\. Click "Single-end"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/a83ba21e-7aa7-409d-b56e-10f97de9ac88/ascreenshot_8ee3fa903e6c45fc8491951351974486_text_export.jpeg)


106\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/c6782616-7de2-44b7-953f-6387087ec11e/ascreenshot_eb1dee8e22884f99807d94a03230cd6b_text_export.jpeg)


107\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/30e4372e-ad44-445a-ac17-664797507c5c/ascreenshot_423908ca468543eb801a896dcd3097e4_text_export.jpeg)


108\. Click "447: preassembly data reorg (as FASTQ)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e612e905-2a1c-4736-bbbc-ee0d795d07bd/ascreenshot_b1e2a1c8f0e34cb2bb424a92c4796c9f_text_export.jpeg)


109\. Click "... accepted formats"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/7002b8c1-75a0-47e2-92f2-967b7908b8c2/ascreenshot_39d41fd390544033bef279fce04ae65f_text_export.jpeg)


110\. Click "Run Tool"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/c3d03eed-410e-4e70-864f-4ae1433fac5b/ascreenshot_ee09723bac9d4e25ae588f3af48b62e7_text_export.jpeg)


111\. Click "565: SPAdes on collection 447: Scaffolds"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/f2d088a8-fd51-444f-848a-5d49bc58ebfc/ascreenshot_7a235c255e87442dac1ea23a7c9d6e70_text_export.jpeg)


112\. Click "ERR14230090"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/f8bcf5dd-db45-4b12-9135-cff094a8992c/ascreenshot_b260e924e71346268120887708c122a8_text_export.jpeg)


113\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/929a38d4-0586-493a-afd2-a5f2f2a77ea2/ascreenshot_132257da6a544753bf1dc8e4b3c8481d_text_export.jpeg)


114\. Click "History: A. fumigatus variants"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e36ede00-e3b3-482d-ad22-f568637a1377/ascreenshot_7215b3fdef414b64afdbfee82bb761c6_text_export.jpeg)


115\. Double-click the "search tools" field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/35a0cc25-eca1-43a7-886b-d5d9d280b4fc/ascreenshot_f7fc6948092d4da9bc4390b74de125d3_text_export.jpeg)


116\. Type "etandem"


117\. Click "Looks for tandem repeats in a nucleotide sequence"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/6ff36d57-15b0-474b-91c7-34bfc6e6edef/ascreenshot_2bab4715ce3c4a0dac558ecf2f2ccb95_text_export.jpeg)


118\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/2c0ae37b-28fa-4ea7-893c-ac73932807bd/ascreenshot_66c095d5ac674689b2d5612a8eb020c1_text_export.jpeg)


119\. Click this number field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/02d3f274-ca14-4bc7-8e4c-a24de2abb81b/ascreenshot_2b321fc30689411790d9ce7f828374a2_text_export.jpeg)


120\. Type "70"


121\. Click "Run Tool"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/56b23d34-699c-40ff-8da3-cd16f37ced23/ascreenshot_4b78632638bd4f029e47e14543bde4a1_text_export.jpeg)


122\. Click "variants_cyp51A_v8.ipynb"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/d0dabe6c-1ace-4dab-ba23-10fccc58b770/ascreenshot_a25c4182d3c94191bebcebba03b1d0e7_text_export.jpeg)


123\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/a2498947-6055-4326-8794-23842d12e2b5/ascreenshot_9174c13590e64c209ebadba7f9a3e71e_text_export.jpeg)


124\. Click "Select"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/5c4c1fd6-4a0d-4ffa-bda8-b96170e46b8f/ascreenshot_a27f86fa2c3d4b09a0eb09e9bf42e6c0_text_export.jpeg)


125\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/bafe186c-f95b-4461-8c24-6ccce346f74f/ascreenshot_b6ccf1cd39694d52a67d7b39fae9fab0_text_export.jpeg)


126\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/725dee48-b912-45c0-ab78-35523cb4f650/ascreenshot_347cd312df43484587f4d4522751f73b_text_export.jpeg)


127\. Click "Multi-Sample Variant Assembly for cyp51A\n\nThis notebook creates a GFF3 file where each sample's variants are on their own line (using the Sour..."

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e96a6527-0217-43eb-9b22-7f956ff9b66b/ascreenshot_c90e0c61c11a4a07a60acf81e394b458_text_export.jpeg)


128\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/03925c72-61a4-4e64-97fe-c9ae89c81ae5/ascreenshot_198e267f97be45efbc869dc51dd404a6_text_export.jpeg)


129\. Click "Restart the kernel"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/641181ac-556b-464f-9990-ef4ff42a174a/ascreenshot_27cb096e35714aab9524f7657311ded1_text_export.jpeg)


130\. Click "Restart"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/d4ae8a79-045b-4b4f-9b8d-b0c1e1bc5e93/ascreenshot_9e0c29c2e9cf4343b11ed3a594415462_text_export.jpeg)


131\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/db80572f-1460-44dc-ab92-6fc2d0ea3686/ascreenshot_cd37127ce14e4e8fb576f0e65c4d8861_text_export.jpeg)


132\. Click "More commands"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e04a729b-d8aa-4ac4-bbc2-3e4f427554a0/ascreenshot_21fc036492eb42638a0af3206ed30013_text_export.jpeg)


133\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/9b17ad4f-47c3-43db-8ff9-ecbfb34af371/ascreenshot_1a33eaf49f334326865dc7ace54cf305_text_export.jpeg)


134\. Click "Restart the kernel and run all cells"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/a0c8715b-cbb6-4600-badf-292cccb12ccb/ascreenshot_40683875689c4481ac11be604e97e626_text_export.jpeg)


135\. Click "Do not ask me again.CancelRestart"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/27d12ec8-46d0-4ea9-98a7-cfbf18a47c61/ascreenshot_29da6f35e0b64e148641550acc841329_text_export.jpeg)


136\. Click "Restart"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/1bdae7ed-d166-48a3-982c-85d368746812/ascreenshot_3014a7901735420d895688d14a976255_text_export.jpeg)


137\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/fe61224a-6794-4358-9cc4-30166a02c5b9/ascreenshot_a6a14f3e44ac42b2bb9242e0f4cae3c2_text_export.jpeg)


138\. Click "701: cyp51A Combined Variants (By SRA)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/21a47c09-9509-4367-acbf-241ad65688f2/ascreenshot_18db078af2754438a3a71eae9e500b09_text_export.jpeg)


139\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/abdc00ea-ae93-431c-9dac-f26ed812d156/ascreenshot_4e70b5a2e27e41aaa86b2ab71a5031d9_text_export.jpeg)


140\. Click "etandem on collection 565"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e73d7dc5-d5b4-4ce5-87f1-5be0354e11d3/ascreenshot_46e24183f21443128e022f8a72afcce7_text_export.jpeg)


141\. Click "ERR14230090"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/ae88cca0-41c9-46f5-85ef-bf0df61ed344/ascreenshot_4d399ba2457e4058a896d6107e7be5ba_text_export.jpeg)


142\. Click "ERR14230094"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/62b89984-39b2-4f35-b715-9f40af025db0/ascreenshot_e123779de1b54ea4b006c687497a967a_text_export.jpeg)


143\. Click "ERR14230102"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/7c4c1c84-f8a3-4a14-9254-6f23c7cea829/ascreenshot_d0583ee713974195b0978749340403de_text_export.jpeg)


144\. Click "ERR14230106"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/304e9a69-fdbb-4c9c-bedc-fc998a35ad0a/ascreenshot_38d4982b82344bf6ad5d2abb61d8c102_text_export.jpeg)


145\. Click "ERR14230091"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/0e322c31-537e-4855-bb90-a001421daa8a/ascreenshot_fd4e0cd314f541e394ad2fda29ab15f6_text_export.jpeg)


146\. Click "ERR14230095"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/c225e1cd-64fb-4a70-b75f-e148b6dae2b7/ascreenshot_1fc49deb68784a2fb26ece4deefb1ba5_text_export.jpeg)


147\. Click "ERR14230096"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/ecaf22a3-937a-4827-b2e3-a65e0d4839b1/ascreenshot_af83756febd443a29e24a078233d00f7_text_export.jpeg)


148\. Click "ERR14230097"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/bb6e64fa-3649-4f39-9224-37d22e3b8ad0/ascreenshot_d2b13a5e3cc9453aaeaa0a7dd660e54f_text_export.jpeg)


149\. Click "ERR14230098"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/9597b236-a6d4-4237-b0b8-cb09e4422e65/ascreenshot_9794f1b12afc480fa3e8834008ce0c5b_text_export.jpeg)


150\. Click "ERR14230099"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/3f477fe0-1c59-4f16-8a82-824ae57cc722/ascreenshot_22dcfc5fd8104e1b87b509895ab14015_text_export.jpeg)


151\. Click "ERR14230100"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/50e091e4-94aa-4e00-82e4-4d83bb561b93/ascreenshot_44f9f522937b42c1b1a9468049cdeb30_text_export.jpeg)


152\. Click "ERR14230104"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/80f06708-5da9-4c1b-bb75-9cfbc58210fb/ascreenshot_42290c44853b440e84e376e71afc4118_text_export.jpeg)


153\. Click "ERR14230105"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/77199ea1-bb37-48b5-a58b-c7644607f3b7/ascreenshot_a67c5a8b34fb4fc98840fdf31a7c4341_text_export.jpeg)


154\. Click "SRR12949926"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/51431780-b448-445a-8e61-35bd880b1196/ascreenshot_bf46990d9b114505bcf2aa7a34bedc0e_text_export.jpeg)


155\. Click "SRR12949928"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/3662e15b-4583-4a84-bef9-a807e73d4c66/ascreenshot_07edbcc075d946e2bd515246aa42b444_text_export.jpeg)


156\. Click "SRR12949929"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/7db7f6ec-2b7f-41dc-a4b3-a1a9946bc4dd/ascreenshot_e4fdfa50c00d4f9faf9556c712ee4491_text_export.jpeg)


157\. Click "ERR14230092"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/bdb37c4a-1e92-40d1-937d-a1b8c1c64b02/ascreenshot_99bf4a4bf017430bbb33e1f6484e6847_text_export.jpeg)


158\. Click "ERR14230093"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/84baf18e-aadf-44fa-be4b-1f7fefda8e1a/ascreenshot_1f7115a15b344249b82c2f1f724b7127_text_export.jpeg)


159\. Click "ERR14230101"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/5a3414a6-e934-4725-8721-f25a10b9e76d/ascreenshot_d5ea487ab9fd4eb2a05a7ef21f3eb7a3_text_export.jpeg)


160\. Click "ERR14230103"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/be72b9d9-757b-4b69-8e64-7b9a0c43f1dd/ascreenshot_d0e88d34cba1415b9f86948d8e9b3eca_text_export.jpeg)


161\. Click "ERR14230107"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/276c2f23-55ae-4032-ba3b-784fd833b18e/ascreenshot_1879a92e98194e759fe1b9749854ca92_text_export.jpeg)


162\. Click "SRR12949927"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/0265c975-0708-4e9e-bb64-018c75ac0610/ascreenshot_fbc1d6da1a634dc4b8e63ca078a9ba5d_text_export.jpeg)


163\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/61fd5905-ceca-4150-b96a-af6b378c345a/ascreenshot_d8779e4f0ab84482a7790bfa150100a6_text_export.jpeg)


164\. Click "etandem on collection 565"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/cb3d2ea6-c86f-47ba-8e72-270ef293a149/ascreenshot_b8ef657b2b6b4afb944bb1fcd5f51876_text_export.jpeg)


165\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/12876a50-3e1e-42db-add9-2c345fe7705b/ascreenshot_b57a08f76b574d1c8340f83aed5a4ec5_text_export.jpeg)


166\. Click "History: A. fumigatus variants"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e57f6bbd-2211-4e15-9679-aa49d2f99a34/ascreenshot_6c614929c8e047e78b059c535f060f8e_text_export.jpeg)


167\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/6f61cc61-cf6b-4383-84ab-5477439cbb9e/ascreenshot_4c12ca85181146b6afd8f2242464bf7f_text_export.jpeg)


168\. Click "Collection and elements"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/17c9c8e8-a1f5-4fa0-9e40-51481b682d24/ascreenshot_f51b62a4f991409ca966aa81968217f6_text_export.jpeg)


169\. Click this button.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e1c4ebdb-2772-4adb-9602-b87d622eb990/ascreenshot_abab6521d9dd4b5a866f9ed838a36ccf_text_export.jpeg)


170\. Click "Collection and elements"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/16f2bb0d-1152-4256-9a23-9fe267160d08/ascreenshot_63a70e5758654673b02f8bd5ec6078b1_text_export.jpeg)


171\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/6dd8e5f6-7773-4eca-a548-02279e053950/ascreenshot_df0f29aa12a6425083acd91d6c0fce41_text_export.jpeg)


172\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/d2d0acb5-a32d-45a5-8aed-23d401651197/ascreenshot_71b26609dc89488fa381c9a71ce6d5de_text_export.jpeg)


173\. Click "etandem"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/af2def28-f567-4b4f-ab2f-fc5698060711/ascreenshot_a68790e042a648adbeda7f9cd89d00b8_text_export.jpeg)


174\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/1dfa4bfc-b7a9-4440-a3eb-71aa8f1459b7/ascreenshot_208457267d694236938ff858ed7d2c9a_text_export.jpeg)


175\. Click "Table"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/c5a24c5d-222e-4c3c-b59a-d8eeb80804cd/ascreenshot_f6f5508b8a0e45a6b1bad70ab952247c_text_export.jpeg)


176\. Click "GFF"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/25ca46f6-7dae-4cfe-ae3e-b6209843e45f/ascreenshot_48f90508f4dd4458acfb6b2709269851_text_export.jpeg)


177\. Click this number field.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/da930905-7ccf-4d3a-aadf-74738dd0faa6/ascreenshot_602bb840e47a43b9b24c53cf72231e77_text_export.jpeg)


178\. Type "7"


179\. Click "Run Tool"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/4a733c68-e805-4b05-a15b-214ed4c0635e/ascreenshot_52c656307e7e4c18b02ea2d24c6b5d20_text_export.jpeg)


180\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e1a791e4-12ad-47cc-9f12-0ff57976e749/ascreenshot_9ea55e2e47e54047808d29d67ee8c436_text_export.jpeg)


181\. Click "Select"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e81bf4ce-8c06-4318-9381-911a9fe8be47/ascreenshot_9821d64cdd724d379f4de143a3c9e9e3_text_export.jpeg)


182\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/3b202abd-342d-4b4d-9bac-77e66452a1bb/ascreenshot_aa4ca944cad042678843788c09065b68_text_export.jpeg)


183\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/3dce8935-b2b7-4dfb-ad2d-cac96c7cbf20/ascreenshot_f7d6792e026a41e39305ac83381f729d_text_export.jpeg)


184\. Click "Cell"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/3abfb7ef-7cbf-4ebb-b741-afd5c0bcc533/ascreenshot_6de20969cd7f4c849586d25064b34c88_text_export.jpeg)


185\. Press [[cmd]] + [[c]]

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/c274ed7d-62b7-4784-aee4-daedc00aae08/ascreenshot_0795e1e84fb34ec8ba25ca948b4c4a15_text_export.jpeg)


186\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/665ccecc-d449-4f2a-a9bd-6d709b0f856d/ascreenshot_d7690f89fe7b4d67bcadd395a751391a_text_export.jpeg)


187\. Click "Select"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/04c6abd5-506a-4273-8250-cfcf96935536/ascreenshot_002b285f66774e24984835ab25248111_text_export.jpeg)


188\. Click "Restart the kernel and run all cells"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/7067e789-97bf-4f79-850c-f7e56c203281/ascreenshot_f97d9b290d944ab6bb974c211025d71c_text_export.jpeg)


189\. Click "Restart"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/b5d96534-45a5-453a-83b2-ca565635f9d6/ascreenshot_db605e9994724869a832be316ed5ebbc_text_export.jpeg)


190\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/db892c4f-00f5-4eec-95e7-77626eb6cdd6/ascreenshot_bf0f73a9de734d9a89b07e856c534dd3_text_export.jpeg)


191\. Click "Select"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/21a4eb49-195c-49eb-9446-e63b440c329e/ascreenshot_66c296e10e974519a7c5469767327bef_text_export.jpeg)


192\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/b52a1b20-b641-40b5-b054-c9da96090d53/ascreenshot_8b7900b3da7e4456a6a0aff77fb43590_text_export.jpeg)


193\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/70e60d02-2803-4752-a22c-a369f0ec3eea/ascreenshot_f6f1c2876e8d45f1bb91d93c0ec9ae6d_text_export.jpeg)


194\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e8619c95-2406-4498-86c5-b63e5095aec8/ascreenshot_36d5050873a7421dbfe7494e41f2bd3e_text_export.jpeg)


195\. Click "Select"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/39cc69ab-6f3a-401d-8f03-d3df3d64ccd4/ascreenshot_c39216feabd84e0f9e4f0e8fa208e9d1_text_export.jpeg)


196\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/ca4ee817-7e06-4dad-ac52-78909178f5a6/ascreenshot_e52f1275a96d481499262ab79c516ea5_text_export.jpeg)


197\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/10e7e0f4-5dc1-4b0c-8f58-eec42eb5d220/ascreenshot_bfa1ab0cea1847b28c901b3b518fe15a_text_export.jpeg)


198\. Click "with open(out_file, "w") as f:"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/de2b46d0-4d9a-4844-b834-27c8b6c99397/ascreenshot_00641b171537419c95bbf9f4da25c5ce_text_export.jpeg)


199\. Click "Restart the kernel and run all cells"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/24bebcaf-a2a2-44bf-bfed-7c3760c822ce/ascreenshot_90219ffb7efc4e50922eacb50a4d7dd1_text_export.jpeg)


200\. Click "Restart"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/bc0b0927-e86a-4122-a953-14f6b30cd4f7/ascreenshot_e050249fd1c7466f8f44d274008b0787_text_export.jpeg)


201\. Click this icon.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/7aef70e6-d7f3-4246-9c17-9be604b04eb1/ascreenshot_93d1b484216341728c8478bf87d3d52a_text_export.jpeg)


202\. Click "Select"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/428dbe31-b58c-461f-a56c-8d5880530392/ascreenshot_4ffa07a251e346f086a87db9bffe32bd_text_export.jpeg)


203\. Click "Restart the kernel and run all cells"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/90b295a9-e1fc-4a3b-9fc8-dc3a5cbd2c7b/ascreenshot_9750120ac2ec4d9e918666938ee53d42_text_export.jpeg)


204\. Click "Restart"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/dd1bc4c6-7257-4c04-9878-4b1bfc6a4166/ascreenshot_88e2c76bbfd5482fba43cdd6ee3bb980_text_export.jpeg)


205\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/5db7f8d7-110e-4350-b5de-3e200d659f06/ascreenshot_fc74a396b4ad46b9adca6389ceba2d7a_text_export.jpeg)


206\. Click "etandem on collection 565"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/e32e80ab-19d8-4134-84fd-187ba5e1f53f/ascreenshot_b7240b5360044f7b89376fb9848a8ea5_text_export.jpeg)


207\. Click "ERR14230103"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/ae44c9c6-d842-489d-87da-2ac4fbd0ffda/ascreenshot_0994dd4af4be452c937fefaf3b9762af_text_export.jpeg)


208\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/42b81e91-a4e9-4406-a89f-274c9175cecd/ascreenshot_a31f541fbf4b47cb9f74a59e95e681aa_text_export.jpeg)


209\. Click "History: A. fumigatus variants"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/b7ca4bad-1faa-48fd-a269-622f9b9a7661/ascreenshot_9c70bccd34c343aaba5c1bff46295451_text_export.jpeg)


210\. Click here.

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/afefded7-9dee-40fb-ab59-dbe10a54a9cd/ascreenshot_0d223146e64648e1bd2cbba8d112bbe4_text_export.jpeg)


211\. Click "Select"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/358103cc-3773-43de-86f6-60e09486c92f/ascreenshot_5333b2d82c8f4ba5b68711ea8ceb036c_text_export.jpeg)


212\. Click "Run this cell and advance (⇧ ⏎)"

![](https://colony-recorder.s3.amazonaws.com/files/2026-03-09/3b895bbc-c338-45de-b00e-25eb41581394/ascreenshot_bbedf496e6494799a0e8bd0decb7acf3_text_export.jpeg)
#### [Made with Scribe](https://scribehow.com/shared/Process_Fungal_Genome_Data_and_Identify_Tandem_Repeats__Rik2faHXTMSbBO9rs_Pf4w)



