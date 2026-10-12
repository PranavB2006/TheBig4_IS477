## Project Plan

### Overview
This project is going to examine how local economic conditions and rurality relate to health outcomes across U.S. counties. We will combine county-level health data from the CDC with economic and rural-urban data from the USDA Economic Research Service (ERS) and test whether counties with higher unemployment and lower median household income tend to have higher diabetes and obesity prevalence, and whether these patterns differ between metropolitan and nonmetropolitan counties.

We will use Python and Pandas to acquire, clean, validate, and integrate the datasets on county FIPS codes, assess data quality before and after integration, and produce summary statistics and visualizations. Separate scripts for acquisition, cleaning/integration, and analysis will be coordinated by a main script (run_all.py) so the workflow can be reproducible.

### Team
Pranav Bhongir (Planning and Documentation): Maintains the project plan and README; documents research questions, sources, constraints, and limitations.

Jake Adams (Data Acquisition): Downloads the datasets; documents source links, reference years, and data-use terms.

Mukund Kasisomayajula (Cleaning and Integration): Cleans and merges the data in Pandas; checks identifiers, missing values, and duplicates.

Gary Mei (Quality and Analysis): Runs quality checks; produces summary statistics and visualizations.

### Research Questions
 
1. Do counties with higher unemployment rates tend to have higher diabetes and obesity prevalence?
2. Is median household income associated with county-level diabetes and obesity prevalence?
3. Do these relationships differ between metropolitan and nonmetropolitan counties?
4. How do missing values and differences in dataset coverage affect the reliability of the integrated analysis?

### Datasets
 
All three are public government datasets with well over 100 records each, linked by **county FIPS code**. No Kaggle data is used.
 
1. **CDC PLACES: County Data** ([link](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/fu4u-a9bh)). County-level diabetes and obesity prevalence. The file has multiple rows per county (one per measure), so we will filter and reshape to one row per county.
2. **USDA ERS County-Level Data Sets** ([link](https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data)). County unemployment rates and median household income. Exact files and columns will be confirmed at download.
3. **USDA ERS 2023 Rural-Urban Continuum Codes** ([link](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes)). RUCC codes 1–3 will be classified as metropolitan and 4–9 as nonmetropolitan, while preserving the original code.
