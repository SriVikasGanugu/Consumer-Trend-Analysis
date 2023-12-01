#### SERX94: Experimentation

#### Consumer Trend Analysis (title)

#### Sri Vikas Ganugu (author)

#### 20-11-2023 (date)

## Explainable Records

1>Row 251: 1997 Q1

This row contains data primarily in integer(Pounds in millions) and float format(index). I'm considering 2 columns ("Households (S.14): Individual consumption expenditure (P.31) Uses: Current price: Â£m: SA" and "Household final consumption expenditure: National concept IDEF SA 2019=100"), provided values are 148521(Column B) and 70.9(Column D). Column D should be of the float format as it is a percentage based on an year(2019 as per Website), Column B shouls be an Integer showing total number of millions in Pounds(Consumption Expenditure). Hence, the values are reasonable for the meaning of data.

2>Row 81: 2021

This row contains data primarily in integer(Pounds in millions) and float format(index). I'm considering 2 columns ("Household final consumption expenditure: National concept IDEF NSA 2019=100" and "Household final consumption expenditure: Net tourist expenditure CP NSA Â£m"), provided values are 102.6(Column I) and 607(Column N). Column N should be of the float format as it is a percentage based on an year(2019 as per Website). The value for Column I is higher than the base year which should be expected as the household consumption price is steadily increasing every year. The value for Column N is 607 which really low compared to years above it(historically lowest) for Tourist expenditure, which is to be expected due to the prevalence of the glopal pandemic Covid-19. Hence, The values are reasonable for the meaning of data.

## Interesting Features

### Feature A

**Feature:** Household final consumption expenditure: National concept IDEF NSA 2019=100

**Justification:**
HFCE is a key economic indicator that reflects the total expenditure made by households on goods and services. Changes in HFCE often correlate with broader economic trends, making it an important variable for predicting consumer behavior. Businesses and policymakers use HFCE data to plan and strategize. For businesses, understanding when consumer demand is likely to peak or dip can inform inventory management, marketing strategies, and sales forecasts.

### Feature B

**Feature:** Household final consumption expenditure: UK tourist expenditure abroad CVM NSA £m

**Justification:**
The expenditure by UK tourists abroad reflects the spending habits of UK households when traveling internationally. An increase in tourist expenditure abroad may indicate a robust economy, potentially influencing domestic spending habits. It can provide insights into the economic health of a country. Tourist expenditure abroad might exhibit seasonal patterns, influencing the overall consumption behavior.

## Experiments

### Varying A

**Prediction Trend Seen:**
There is no continuity between data or trends. There is no trend in the visualisation of Semi Durable Goods. The features chosen for the model are highly unrelated hence there is always an discontinuity.

### Varying B

**Prediction Trend Seen:**
The Prediction Trend for Tourist Expenditure in UK and Household final consumption expenditure: NSA is non existent. Which means that there is no significant upward or downward moment with increase in HFCE. The features chosen for the model are highly unrelated.

### Varying A and B together

**Prediction Trend Seen:**
There is no Correlation between the features A and B. Both features were selected from a correlation matrix with constraints that they have their coefficiend near 0. Hence there would not be any relation between the both features.

### Varying A and B inversely

**Prediction Trend Seen:**
There is no Inverse relation between the features A and B. Both features were selected from a correlation matrix with constraints that they have their coefficient near 0. Hence there would not be any relation between the both features.
