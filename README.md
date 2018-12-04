# Proba-V Hemispherical Analysis

## How to run:

### 1) Extract reflectance data, quality flags and various indices from satellite data
Run the script named `get_satellite_data_indices.py`to collect all measurements into a single CSV file.

### 2) Fit a polynomial to the satellite time series 
Time series filtering and interpolation are performed by the script `analyse_timeseries.py`.

### 3) Combine hemispherical data and interpolated satellite data for the same date
Run `output_hemis_ts.py` to perform this task.

### 4) Analyse correlation between the datasets and fit the function to it
Final step and actual analysis of the data is performed by the script `analyse_results.py`.

### Other scripts
`lai.py` - various functions used in the analysis
`lai.py` - LAI refression tree
`fapar.py` - fAPAR refression tree
`fcover.py` - fCOVER refression tree
