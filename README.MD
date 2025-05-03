# LVS

This repository contains the code for the LVS project.

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
* `avar_name`= Cause
* `avalue_name`= Deaths  

[output]
* `output_path` = data/cod/lvs.csv
* `output_dic` = data/cod/dic.csv 
* `sig_file` = data/cod/signatures.csv


Running full processing : lvs_data_processing.ipynb