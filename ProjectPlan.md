## Project Plan

### Overview
This project is going to examine how local economic conditions and rurality relate to health outcomes across U.S. counties. We will combine county-level health data from the CDC with economic and rural-urban data from the USDA Economic Research Service (ERS) and test whether counties with higher unemployment and lower median household income tend to have higher diabetes and obesity prevalence, and whether these patterns differ between metropolitan and nonmetropolitan counties.

We will use Python and Pandas to acquire, clean, validate, and integrate the datasets on county FIPS codes, assess data quality before and after integration, and produce summary statistics and visualizations. Separate scripts for acquisition, cleaning/integration, and analysis will be coordinated by a main script (run_all.py) so the workflow can be reproducible.

### Team
Pranav Bhongir (Planning and Documentation): Maintains the project plan and README; documents research questions, sources, constraints, and limitations.

Jake Adams (Data Acquisition): Downloads the datasets; documents source links, reference years, and data-use terms.

Mukund Kasisomayajula (Cleaning and Integration): Cleans and merges the data in Pandas; checks identifiers, missing values, and duplicates.

Gary Mei (Quality and Analysis): Runs quality checks; produces summary statistics and visualizations.

## Research Questions
 
1. Do counties with higher unemployment rates tend to have higher diabetes and obesity prevalence?
2. Is median household income associated with county-level diabetes and obesity prevalence?
3. Do these relationships differ between metropolitan and nonmetropolitan counties?
4. How do missing values and differences in dataset coverage affect the reliability of the integrated analysis?
