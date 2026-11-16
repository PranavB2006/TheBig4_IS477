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

### 4. Cleaning and Integration
 
**Status: Completed**
 
We cleaned and combined the three datasets using county FIPS codes. We made sure all the FIPS codes had five digits and checked for missing values, duplicates, and different data types.
 
We also organized the CDC PLACES dataset so each county had one row with its health information. After that, we combined it with the economic data and rural-urban codes.
 
We checked for counties that did not match between the datasets. We also made sure not to replace missing values with zero since that could affect our results. We will use the cleaned dataset for the next part of our project.

### 5. Data Analysis
 
**Status: In Progress**
 
We are now starting to analyze the combined dataset using Python, Pandas, and Matplotlib. We will calculate summary statistics and correlations to see how unemployment and income relate to diabetes and obesity rates.
 
We will also make scatterplots and compare metropolitan counties (RUCC 1–3) with nonmetropolitan counties (RUCC 4–9). We will also calculate the percentage of counties that have complete data across all three datasets to see how missing values affect our results.

### 6. Workflow Validation
 
**Status: In Progress**
 
We are working on making sure our code runs correctly from start to finish. We plan to use `run_all.py` to run the scripts for collecting, cleaning, combining, and analyzing the data.
 
We will also check the final dataset and results for errors or values that do not make sense. This will help make sure someone else can run our code and get the same results.

### 7. Finalization and Documentation
 
**Status: In Progress**
 
We have already finished our initial documentation and updated our project plan based on the feedback from Milestone 2.
 
We still need to update the README, explain our results, organize the output files, and review the final project. We will also make sure all the required files are in our GitHub repository.

## Updated Project Timeline
 
| Phase | Status | Target Dates | Owner |
|---|---|---|---|
| Planning and documentation | Completed | Oct 5–12 | Pranav |
| Data acquisition | Completed | Oct 13–20 | Jake |
| Initial quality assessment | Completed | Oct 21–28 | Gary |
| Cleaning and integration | Completed | Oct 29–Nov 15 | Mukund |
| Data analysis | In progress | Nov 16–20 | Gary |
| Workflow validation | In progress | Dec 2–4 | Mukund and all members |
| Finalization and documentation | In progress | Dec 5–6 | All members |

## Individual Team Contributions

### Pranav Bhongir — Planning and Documentation

I worked on the planning and documentation for our project. I helped come up with our research questions, identify our goals, and decide on the methods we would use. I also updated our project plan based on the feedback from Milestone 2. For this milestone, I helped write the interim status report and update our timeline.

### Jake Adams — Data Acquisition
 
I worked on collecting the datasets for our project. I downloaded the CDC PLACES and USDA datasets and looked at their sources and reference years. I also made sure we had the information needed to combine the datasets using county FIPS codes. My work helped get the data ready for cleaning and integration.

### Gary Mei — Quality and Analysis

I worked on checking the quality of our datasets before we combined them. I looked for missing values, duplicate records, different data types, and missing counties. I also checked for differences between the datasets that could affect our results. This helped us figure out what needed to be fixed before cleaning and combining the data.
 
## Next Steps

Our main goal now is to finish analyzing the combined dataset. We will calculate summary statistics and correlations, make graphs, and compare health outcomes between metropolitan and nonmetropolitan counties.
 
After that, we will check our workflow to make sure everything runs correctly. We will also review our results and finish explaining our methods and findings.
 
Overall, we have finished the first four parts of our project and are now working on completing the remaining tasks.
