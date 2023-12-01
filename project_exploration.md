#### SERX94: Exploratory Data Munging and Visualization

#### Title: Consumer Trends Data Cleaning

#### Author: Sri Vikas Ganugu

#### Date: 18-10=2023

## Basic Questions

**Dataset Author(s):** Ian Simmons-Thomas

**Dataset Construction Date:** 30 September 2019

**Dataset Record Count:** 356

**Dataset Field Meanings:** Different Consumer Expenditures

**Dataset File Hash(es):** cc2d7ef4377e20215daa993714db28f0

**Description :**

The dataset taken from the URL is large(356 rows, 1157 columns). In the dataset there are cells with missing values and missing data. Normally these could be artificially produced if there is any correlation with other data but there are mass chunks of missing data before the year 1997. For example, in 1968, cells in the row are missing data in Food(eggs, meat, fish, etc. (column names)). These data cannot be correlated to other columns in the data set aand do not have any other resources to give values nor have any historical values(i.e. new inventions). Hence we are going to consider columns from 1997 Q1(Quarter-1) we are considering quarterly data.

It is produced from surveys and Blue book, but there are some missing values which were filled by from other resources(not national surveys).

Records : 356 Rows Both Yearly and Quarterly for Every Year from 1948 to 2022 (2023 Didn't end so no Yearly Records). T

URL: https://www.ons.gov.uk/economy/nationalaccounts/satelliteaccounts/datasets/consumertrends

MD5 : cc2d7ef4377e20215daa993714db28f0

The data set is fairly new as it was last updated on September 2023. The dataset is not synthetic as all values are taken from National surveys or the Blue Book(UK's GDP probably) and uncertain values were filled from Other resources probably public studies or research.

## Interpretable Records

### Record 1

**Raw Data:** Row 251: 1997 Q1

**Interpretation:** This row contains data primarily in integer(Pounds in millions) and float format(index). I'm considering 2 columns ("Households (S.14): Individual consumption expenditure (P.31) Uses: Current price: Â£m: SA" and "Household final consumption expenditure: National concept IDEF SA 2019=100"), provided values are 148521(Column B) and 70.9(Column D). Column D should be of the float format as it is a percentage based on an year(2019 as per Website), Column B shouls be an Integer showing total number of millions in Pounds(Consumption Expenditure). Hence, the values are reasonable for the meaning of data.

### Record 2

**Raw Data:** Row 81: 2021

**Interpretation:** This row contains data primarily in integer(Pounds in millions) and float format(index). I'm considering 2 columns ("Household final consumption expenditure: National concept IDEF NSA 2019=100" and "Household final consumption expenditure: Net tourist expenditure CP NSA Â£m"), provided values are 102.6(Column I) and 607(Column N). Column N should be of the float format as it is a percentage based on an year(2019 as per Website). The value for Column I is higher than the base year which should be expected as the household consumption price is steadily increasing every year. The value for Column N is 607 which really low compared to years above it(historically lowest) for Tourist expenditure, which is to be expected due to the prevalence of the glopal pandemic Covid-19. Hence, The values are reasonable for the meaning of data.

## Background Domain Knowledge

The project is based on consumer trends in the UK. The dataset includes data on consumer expenditure in a vast feild of areas(like house hold, car, home, etc). Most of the data does not require domain knowledge to understand. The data has been cleaned before uploading by the author. To better understand the domain, I looked at different datasets and codes which use this dataset.

To understand the columns in the dataset, I used a kaggle dataset ("https://www.kaggle.com/datasets/matarrgaye/uk-consumer-trends-current-price/data"). The kaggle dataset is cleaner than UK dataset, it has understandable and better defined categories. Those categories are converted to different csv files which would help in performing trend analysis in particulart category(Household, tourist, etc).

For little insight on cleaning of data for consumer trends, I used "https://www.kaggle.com/code/waikityeung/uk-consumer-trends" which is based on the kaggle dataset and is very different from what I did in this milestone. Taking a look at different graphs in this code, makes us understand the dataset better.

The code and data in Kaggle is based on the quarterly consumer expenditure per year(that is,Jan to March, April to June, July to September, October to December).

## Data Transformation

### Transformation 1

**Description:**
The dataset downloaded from the website is unclean. It has several missing values which cannot be computed (synthesised) or filled with a random value. Record until 1996 in both yearly and quarterly data contain missing values which cannot be determined(filled) because they are not recorded until 1997(Cars, Food(meat, alcohol),etc). I removed all records with missing chunks of values to not affect the whole model.

After Data cleaning, I split the data set into three, Yearly, Quarterly and entire. For further training this would be helpful.

**Soundness Justification:**
The dataset downloaded from the website is unclean. It has several missing values which cannot be computed (synthesised) or filled with a random value. Record until 1996 in both yearly and quarterly data contain missing values which cannot be determined(filled) because they are not recorded until 1997(Cars, Food(meat, alcohol),etc). I removed all records with missing chunks of values to not affect the whole model. Since, industrial revolution there has been a huge leap in technology. We have been using new technology every decade and so out expenditure on various miscellaneous stuff has increased, so have the categories.

After Data cleaning, I split the data set into three, Yearly, Quarterly and entire. Yearly has less number of columns than Quarterly and Enitre data set. Entire is a dataset which contains values from both yearly and quarterly. Having values from both datasets would be beneficial for finding relations hidden inside the data. We use the Quarterly Dataset for visualisation. For further training this would be helpful.

## Visualization

### Visual 1

**Analysis:**
Min vs Max:
This graph is a scatter plot of all datapoints in which shows, min_array(Minimu value in every row of the column and Maximum value in every row of the column). This graph shows us that with increase in time there has been a steady or consistent increase in expenditure with time.

Min vs Median
This graph is a scatter plot of all datapoints in which shows, min_array and median_array(Minimu value in every row of the column and Median value in every row of the column). This graph shows us that with increase in time there has been a steady or consistent increase in expenditure with time.

Median vs Max:
This graph is a scatter plot of all datapoints in which shows, median_array and Maximum array(Median value in every row of the column and Maxium value in every row of the column). This graph shows us that with increase in time there has been a steady or consistent increase in expenditure with time.

High Expenditure Histogram:
This graph is a histogram of all data points which show the highest expenditure in all categories for a year. Unexpectedly the histogram shows a sharp increase and decrese in expenditure with time. Which means in the last few years(quarterly) expenditure has dropped.

Low Expenditure Histogram:
This graph is a histogram of all data points(most are negative) which show the lowest expenditure in all categories for a year. Unexpectedly the histogram shows a sharp increase and decrese in expenditure with time. Which means in the last few years(quarterly) expenditure has increased (i.e. debts have decreased).
