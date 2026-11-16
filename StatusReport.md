# Milestone 3: Interim Status Report

## Status Report
Our project looks at how economic conditions and rurality relate to health outcomes across U.S. counties. We are using data from the CDC and USDA to see if counties with higher unemployment rates and lower median household income also have higher diabetes and obesity rates. We also want to see if these relationships are different between metropolitan and nonmetropolitan counties.

We are using Python and Pandas to collect, clean, and combine three government datasets using county FIPS codes. We will then use summary statistics, correlations, and graphs to look at the results. We also want to see how missing values and differences between the datasets affect our final data.

So far, we have finished planning, collecting the data, checking data quality, and cleaning and combining the datasets. We are now working on the analysis and the remaining parts of the project.

## Progress on Project Tasks

### 1. Planning and Documentation
**Status: Completed**

We finished our project plan and decided on our research questions, datasets, methods, and team responsibilities. We also identified some possible challenges like missing values, different reference years, and issues with county FIPS codes.

We also updated our project plan based on the feedback we got for Milestone 2. We changed our fourth research question to focus on data completeness and added specific dates to our timeline.

Our project plan can be found in ProjectPlan.md.

### 2. Data Acquisition
**Status: Completed**

We collected the three government datasets we need for our project. The CDC PLACES dataset gives us diabetes and obesity rates for each county. The USDA economic dataset gives us unemployment rates and median household income. The USDA Rural-Urban Continuum Codes help us separate counties into metropolitan and nonmetropolitan groups.

We also looked at the sources and years for each dataset to see if there were any differences. We kept the original files in the `data/raw/` folder so we can go back to them if needed.

### 3. Initial Quality Assessment

**Status: Completed**

We checked the datasets for missing values, duplicate records, different data types, and missing counties. We also made sure the county identifiers were consistent and that the values made sense.

Since the datasets came from different sources, we also looked at differences in the years they covered. This helped us figure out what needed to be fixed before combining the data.
