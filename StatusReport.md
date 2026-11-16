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

Our project plan can be found in [ProjectPlan.md](ProjectPlan.md).

### 2. Data Acquisition
**Status: Completed**

We collected the three government datasets we need for our project. The CDC PLACES dataset gives us diabetes and obesity rates for each county. The USDA economic dataset gives us unemployment rates and median household income. The USDA Rural-Urban Continuum Codes help us separate counties into metropolitan and nonmetropolitan groups.

We also looked at the sources and years for each dataset to see if there were any differences. We have collected the original datasets and reviewed their sources and reference years. We are also working on organizing the files so they can be included in our GitHub repository. 

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
 
We are working on making sure our code runs correctly from start to finish. We plan to check that our Python scripts run correctly from start to finish. We will test the steps for collecting, cleaning, combining, and analyzing the data. We will also check the final results for errors to make sure our work can be repeated.
 
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

## Changes to Our Project Plan

After getting feedback on Milestone 2, we made two changes to our project plan.

The first change was to our fourth research question. Originally, we wanted to see how missing values and differences in dataset coverage affected the reliability of our analysis. Our professor suggested that we explain what we meant by reliability and how we would measure it. We changed the question to focus on data completeness instead. We also added a way to measure this by calculating the percentage of counties that have complete data across all three datasets.

The second change was to our timeline. Our original timeline only listed tasks by week. We updated it to include specific dates for each task so it is easier to track our progress and see when things need to be finished.

Other than these changes, we kept our original research questions, datasets, and methods the same because they still work for our project.

## Challenges and Solutions

### Different Data Formats

One challenge was that the datasets were organized differently. The CDC PLACES dataset had multiple rows for each county, while the USDA datasets were organized differently. We fixed this by making sure each county had one row in the PLACES dataset before combining everything.

### County FIPS Codes

Another challenge was making sure the county FIPS codes matched correctly. Some FIPS codes can lose their leading zeros when stored as numbers. We fixed this by making sure all the codes had five digits before combining the datasets.

### Missing Values and County Coverage

Some counties may not have complete information across all three datasets. We are keeping track of missing values and counties that did not match. During our analysis, we will calculate the percentage of counties with complete data and explain how missing information affects our results.

### Different Reference Years

Our datasets may cover different years, which can make comparisons harder. We will explain these differences in our final report. We will also be careful not to assume that one variable causes another just because they are related.

### Organizing Files in Github

Another challenge has been organizing all our project files in one place. Some of our datasets and Python scripts are currently saved on individual team members' computers. We plan to upload these files to our shared GitHub repository so everyone can access them. This will also make it easier to test our workflow and complete the remaining parts of the project.

## Individual Team Contributions

### Pranav Bhongir — Planning and Documentation

I worked on the planning and documentation for our project. I helped come up with our research questions, identify our goals, and decide on the methods we would use. I also updated our project plan based on the feedback from Milestone 2. For this milestone, I helped write the interim status report and update our timeline.

### Jake Adams — Data Acquisition
 
I worked on collecting the datasets for our project. I downloaded the CDC PLACES and USDA datasets and looked at their sources and reference years. I also made sure we had the information needed to combine the datasets using county FIPS codes. My work helped get the data ready for cleaning and integration.

### Mukund Kasisomayajula — Cleaning and Integration

I worked on cleaning and combining the datasets using Python and Pandas. I made sure all the county FIPS codes had five digits and checked for missing values and duplicates. I also organized the CDC PLACES data so each county had one row. After that, I combined the health, economic, and rural-urban data into one dataset for our analysis.

### Gary Mei — Quality and Analysis

I worked on checking the quality of our datasets before we combined them. I looked for missing values, duplicate records, different data types, and missing counties. I also checked for differences between the datasets that could affect our results. This helped us figure out what needed to be fixed before cleaning and combining the data.
 
## Next Steps

Our main goal now is to finish analyzing the combined dataset. We will calculate summary statistics and correlations, make graphs, and compare health outcomes between metropolitan and nonmetropolitan counties.
 
After that, we will check our workflow to make sure everything runs correctly. We will also review our results and finish explaining our methods and findings.
 
Overall, we have finished the first four parts of our project and are now working on completing the remaining tasks.
