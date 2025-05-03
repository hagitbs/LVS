# LVS

This repository contains the code for the LVS project.

## Input data 
* We accept 2 types of csv : 
* 1. full - raw data 
For example : 

Entity,Code,Year,Meningitis,Alzheimer's disease and other dementias,Parkinson's disease,Nutritional deficiencies,Malaria,Drowning,Interpersonal violence,Maternal disorders,HIV/AIDS,Drug use disorders,Tuberculosis,Cardiovascular diseases,Lower respiratory infections,Neonatal disorders,Alcohol use disorders,Self-harm,Exposure to forces of nature,Diarrheal diseases,Environmental heat and cold exposure,Neoplasms,Conflict and terrorism,Diabetes mellitus,Chronic kidney disease,Poisonings,Protein-energy malnutrition,Road injuries ,Chronic respiratory diseases,Cirrhosis and other chronic liver diseases,Digestive diseases,"Fire, heat, and hot substances",Acute hepatitis
Afghanistan,AFG,2007,2933,1402,450,2488,393,2127,3657,4990,148,252,4995,53962,27672,23890,111,1310,296,9320,57,15925,8220,3189,4490,512,2439,7425,7222,3346,6458,481,3437
Afghanistan,AFG,2008,2731,1424,455,2277,255,1973,3785,5020,157,261,4790,54051,25800,23792,114,1330,1317,8275,57,16148,6895,3261,4534,495,2231,7355,7143,3316,6408,462,3005
Afghanistan,AFG,2009,2460,1449,460,2040,239,1852,3874,5013,167,270,4579,53964,24340,23672,115,1342,101,7359,57,16383,7617,3336,4597,483,1998,7290,7045,3291,6358,448,2663

The code is unpivot the raw data and calculate frequencies per Year 

* 2.freq - half processed data with frequencies 
For example : 

element,frequency_in_document,document
fellow,1,1790
immediately,1,1790
impression,1,1790
receive,1,1790
happiness,1,1790
basis,1,1790
surest,1,1790
knowledge,1,1790
literature,1,1790


## Configuration

The configuration for the LVS project is stored in the `config_xxx.toml` [ xxx is the dataset name] file. This file is written in TOML format and contains the following sections:

### `[data]`

This section contains the configuration for the database. The following keys are supported:

* `file_path`: The input file of the dataset in csv format  [ ex - data/cod/annual-number-of-deaths-by-cause.csv]
* `file_path2`: Optional : Additional input file with summary information [ None , or filename  ex - data/cod/population.csv]
* `dataset`: The dataset name [ex - cod] 

[data]
file_path = data/cod/annual-number-of-deaths-by-cause.csv
file_path2 = data/cod/population.csv
dataset = cod 

[proc]
### `[server]`

This processing instructions
* `processing_type`: [full/freq] - should we calculate frequencies only [freq], or also unpivot the dataset [full]
* `agg_column`: Year 
* `var_name`= Cause
* `value_name`= Deaths  

[output]
* `output_path` = data/cod/lvs.csv
* `output_dic` = data/cod/dic.csv 
* `sig_file` = data/cod/signatures.csv


Running full processing : lvs_data_processing.ipynb