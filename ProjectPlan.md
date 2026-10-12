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

Each dataset contributes different information: PLACES provides the health outcomes, the ERS county data provides the economic indicators, and the RUCC file provides the geographic setting. Together they let us compare health outcomes against economic conditions across metropolitan and nonmetropolitan counties.
 
Raw files go in `data/raw/` unmodified; cleaned data in `data/processed/`; reports and figures in `outputs/`. Scripts are `src/acquire_data.py`, `src/clean_integrate.py`, `src/analyze.py`, and `run_all.py`, using relative paths. We will record source URLs, download dates, and reference years.

## Methods

- **Cleaning and integration:** We will first make sure all FIPS codes follow the same five-digit format, including any leading zeros. We will then check data types, missing values, and duplicate records before merging the datasets using county FIPS codes. After each merge, we will check how many counties were successfully matched and whether any records were lost. Any unexpected values or duplicates will be reviewed rather than automatically deleted.

- **Data quality:** We will evaluate the quality of each dataset both before and after combining them. This includes checking whether the values are reasonable, how much data is missing, whether all counties are represented, and whether the datasets cover similar time periods. We will also make sure identifiers and data types are consistent across sources. A short quality report will document our findings at each stage.

- **Analysis:** We will use Python, mainly Pandas and Matplotlib, to explore how unemployment rates and median household income relate to diabetes and obesity prevalence across U.S. counties. Our analysis will include summary statistics, correlations, and scatterplots to identify patterns in the data. We will also compare metropolitan and nonmetropolitan counties to see whether these relationships differ between the two groups.

- **Reproducibility:** We will organize our code into separate scripts for downloading, cleaning, and analyzing the data. These scripts will run in order through `run_all.py`, allowing someone else to repeat our process using the original datasets. We will also include a `requirements.txt` file for dependencies, explain how to run the project in the README, and regularly commit our progress to GitHub.

- **Ethics and licensing:** We will follow the terms of use for each dataset and properly credit the original sources. Since our analysis focuses on county-level data, we will avoid making conclusions about individual people. We will also be careful not to interpret correlations as proof that economic conditions directly cause certain health outcomes.

## Timeline

| Phase | Tasks | Target | Owner |
|---|---|---|---|
| 1. Planning | Finalize our research questions, identify data sources, and complete the initial project plan | Week 1 | Pranav Bhongir (all members review) |
| 2. Data acquisition | Download the datasets and document their sources, reference years, and usage requirements | Week 1 | Jake Adams |
| 3. Quality assessment | Review data types, missing values, duplicates, and county coverage; prepare an initial quality report | Week 2 | Gary Mei |
| 4. Cleaning and integration | Standardize FIPS codes, clean variables, organize the PLACES dataset, and merge the datasets | Week 2 | Mukund Kasisomayajula |
| 5. Analysis | Calculate summary statistics and correlations, compare metro and nonmetro counties, create visualizations, and complete the final quality report | Week 3 | Gary Mei |
| 6. Validation | Run `run_all.py` from start to finish, check for errors, and review the results for consistency | Week 3 | Mukund Kasisomayajula (all members review) |
| 7. Finalization | Update the README, review the completed project, commit final changes, and tag the project plan | Week 4 | All members |

## Constraints
- Different reference years: Health, economic, and rurality data may cover different periods; we will document years and avoid implying exact comparability.
- Missing counties: Some counties may be absent from a source; we will report unmatched records and never treat missing values as zero.
- Variable definitions and formats: Definitions may differ across sources, and file or column names may change; we will check documentation and record exact versions.
- FIPS identifiers: Incorrect formatting, such as lost leading zeros, can cause bad merges.
- Legal and ethical: All sources are public, but we still need to confirm terms of use and attribution requirements. We use aggregate county data only and make no individual-level claims.
- Technical: The PLACES file is large and in long format, so reshaping and validating it correctly will take careful work.
- Ecological fallacy and confounding: County-level patterns do not describe individuals, and factors like age and healthcare access may influence results.
If a key variable is unavailable, we will revise the analysis rather than make unsupported assumptions.
