#### SER594: Machine Learning Evaluation

#### Consumer Trend Analysis (title)

#### Sri Vikas Ganugu (author)

#### 20-11-2023 (date)

## Evaluation Metrics

### Metric 1

**Name:** Mean Squared Error (MSE)

**Choice Justification:** MSE is chosen as it provides a measure of the average squared difference between predicted and actual values, giving an indication of the model's accuracy.

**Interpretation:** Lower MSE values indicate better model performance.

### Metric 2

**Name:** R-squared (R2)

**Choice Justification:** R-squared is selected to measure the proportion of the variance in the dependent variable that is predictable from the independent variables. It's values are between 0 and 1.

**Interpretation:** Higher R-squared values suggest better goodness of fit.

## Alternative Models

### Alternative 1

### Lasso Regression (Alternate Version)

**Construction:** Lasso regression was constructed by applying L1 regularization to the linear regression model.

**Evaluation:**
Model Evaluation: Lasso_Regression(Alternate Version)
MSE: 2.1570735173872255
R-squared: 0.9963019135372025

### Alternative 2

### Ridge Regression (Alternate Version)

**Construction:** Ridge regression was constructed by applying L2 regularization to the linear regression model.

**Evaluation:**
Model Evaluation: Ridge_Regression(Alternate Version)
MSE: 1.8729758429930674
R-squared: 0.9967889705407403

### Alternative 3

### Decision Tree

**Construction:** Decision Tree was constructed by recursively partitioning the data based on feature values.

**Evaluation:**
Model Evaluation: Decision_Tree
MSE: 2.2398125
R-squared: 0.9961600658398109

### Alternative 4

### Random Forest

**Construction:** Random Forest was constructed as an ensemble of decision trees.

**Evaluation:**
Model Evaluation: Random_Forest
MSE: 1.4766976375000003
R-squared: 0.997468349827270

## Best Model

**Model:** Ridge Regression

**Reasoning:** It achieved the lowest MSE and highest R-squared, indicating superior performance compared to other models.
