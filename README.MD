# LVS

This repository contains the code for the LVS project.

## Input data 
* We accept 2 types of csv : 
* 1. full - raw data 
For example : 

|Entity|Code|Year|Meningitis|Alzheimer|Parkinson|Malaria|HIV/AIDS|
|---|---|---|---|---|---|---|---| 
|Afghanistan|AFG|2007|2933|1402|450|2488|393| 
|Afghanistan|AFG|2008|2731|1424|455|2277|255|


The code is unpivotting the raw data and calculate frequencies per Year 

* 2.freq - half processed data with frequencies 
For example : 

| element | frequency_in_document| document | 
|---|---|---|
|fellow|1|1790|
|immediately|1|1790|
|impression|1|1790|
|receive|3|1790| 

## Configuration

The configuration for the LVS project is stored in the `config_xxx.toml` [ xxx is the dataset name] file. This file is written in TOML format and contains the following sections:

### `[data]`

This section contains the configuration for the database. The following keys are supported:

* `file_path`: The input file of the dataset in csv format  [ ex - data/cod/annual-number-of-deaths-by-cause.csv]
* `file_path2`: Optional : Additional input file with summary information [ None , or filename  ex - data/cod/population.csv]
* `dataset`: The dataset name [ex - cod] 
 
file_path = data/cod/annual-number-of-deaths-by-cause.csv
file_path2 = data/cod/population.csv
dataset = cod 

### `[proc]` 
This processing instructions
* `processing_type`: [full/freq] - should we calculate frequencies only [freq], or also unpivot the dataset [full]
* `agg_column`: Year 
* `var_name`= Cause
* `value_name`= Deaths  

### `[output]`
* `output_path` = data/cod/lvs.csv
* `output_dic` = data/cod/dic.csv 
* `sig_file` = data/cod/signatures.csv


Running full processing : lvs_data_processing.ipynb

| Parameter | Description |
|---|---|
| `file_path` | Path to the main CSV data file. |
| `file_path2` | Path to an optional secondary CSV file with summary information. |
| `dataset` | Name of the dataset. |
| `processing_type` | Specifies the type of processing: `full` for unpivoting and frequency calculation, or `freq` for frequency calculation only. |
| `agg_column` | Column used for aggregation (e.g., "Year"). |
| `var_name` | Name of the variable column (e.g., "Cause"). |
| `value_name` | Name of the value column (e.g., "Deaths"). |
| `output_path` | Path to the output CSV file containing processed data. |
| `output_dic` | Path to the output CSV file containing a dictionary or mapping. |
| `sig_file` | Path to the output CSV file for storing signatures. |
