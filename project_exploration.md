1.
Author : Ian Simmons-Thomas

Methodology Constructed : 30 September 2019

Date Updated: 29 September 2023

Description : 
 The dataset taken from the website is large(356 rows, 1157 columns). In the dataset there are cells with missing values and missing data. Normally these could be artificially produced if there is any correlation with other data but there are mass chunks of missing data before the year 1997. For example, in 1968, cells in the row are missing data in Food(eggs, meat, fish, etc. (column names)). These data cannot be correlated to other columns in the data set aand do not have any other resources to give values nor have any historical values(i.e. new inventions). Hence we are going to consider columns from 1997 Q1(Quarter-1) we are considering quarterly data.
 It is produced from surveys and Blue book, but there are some missing values which were filled by from other resources(not national surveys).

Records : 356 Rows Both Yearly and Quarterly for Every Year from 1948 to 2022 (2023 Didn't end so no Yearly Records). T

URL: https://www.ons.gov.uk/economy/nationalaccounts/satelliteaccounts/datasets/consumertrends

MD5 : cc2d7ef4377e20215daa993714db28f0

The data set is fairly new as it was last updated on September 2023. The dataset is not synthetic as all values are taken from National surveys or the Blue Book(UK's GDP probably) and uncertain values were filled from Other resources probably public studies or research.

2.
> Select 2 records...
 1>Row 251: 1997 Q1
 This row contains data primarily in integer(Pounds in millions) and float format(index). I'm considering 2 columns ("Households (S.14): Individual consumption expenditure (P.31) Uses: Current price: Â£m: SA" and "Household final consumption expenditure: National concept IDEF SA 2019=100"), provided values are 148521(Column B) and 70.9(Column D). Column D should be of the float format as it is a percentage based on an year(2019 as per Website), Column B shouls be an Integer showing total number of millions in Pounds(Consumption Expenditure). Hence, the values are reasonable for the meaning of data.
 2>Row 81: 2021
  This row contains data primarily in integer(Pounds in millions) and float format(index). I'm considering 2 columns ("Household final consumption expenditure: National concept IDEF NSA 2019=100" and "Household final consumption expenditure: Net tourist expenditure CP NSA Â£m"), provided values are 102.6(Column I) and 607(Column N). Column N should be of the float format as it is a percentage based on an year(2019 as per Website). The value for Column I is higher than the base year which should be expected as the household consumption price is steadily increasing every year. The value for Column N is 607 which really low compared to years above it(historically lowest) for Tourist expenditure, which is to be expected due to the prevalence of the glopal pandemic Covid-19. Hence, The values are reasonable for the meaning of data.

