---
{}
---

## What is Multiple Linear Regression (MLR)?

Multiple Linear Regression (MLR), also known as multivariate regression, is a statistical technique that uses multiple explanatory variables to predict the outcome of a response variable. The goal of MLR is to establish a linear relationship between explanatory variables (independent variables) and the response variable (dependent variable). In essence, multiple regression is an extension of ordinary least squares (OLS) regression as it involves multiple explanatory variables.

### Key Points

- Multiple Linear Regression (MLR) is a statistical technique that uses multiple explanatory variables to predict the outcome of a response variable.
- It is also known as multivariate regression.
- Multiple regression is an extension of linear (OLS) regression, which uses only one explanatory variable.
- MLR is widely used in econometrics and financial inference.
- Multiple regression is used for making predictions, explaining relationships between financial variables, and testing existing theories.

## Multivariate Linear Regression (MLR) Formula and Calculation

$$ \begin{aligned}&y_i = \beta_0 + \beta _1 x_{i1} + \beta _2 x_{i2} + ... + \beta _p x_{ip} + \epsilon\\&\textbf{其中，i = n \textbf{ 个观察值：}}\\&y_i=\text{因变量}\\&x_i=\text{解释变量}\\&\beta_0=\text{y截距（常数项）}\\&\beta_p=\text{每个解释变量的斜率系数}\\&\epsilon=\text{模型的误差项（也称为残差）}\end{aligned} $$

## What Multiple Linear Regression (MLR) Can Tell You

Simple linear regression is a function that allows analysts or statisticians to predict one variable based on known information about another variable. Linear regression can only be used when there are two continuous variables—one independent variable and one dependent variable. The independent variable is the parameter used to calculate the dependent variable or outcome. Multiple regression models extend to multiple explanatory variables.

MLR models are based on the following assumptions:

- There is a linear relationship between dependent and independent variables
- Independent variables should not be too strongly correlated with each other
- Selected observations are independently and randomly sampled from the population
- Residuals should be normally distributed with mean 0 and variance σ²

**Important Note:** MLR assumes linear relationships between dependent and independent variables, no strong correlation between independent variables, and constant variance of residuals.

The coefficient of determination (R-squared) is a statistical measure that indicates how much of the variation in the outcome can be explained by the variation in the independent variables. R² will increase when adding more predictors to an MLR model, even if the predictor variables are not related to the outcome variable.

Therefore, R² alone cannot be used to identify which predictors should be included in or excluded from the model. R² values range from 0 to 1, where 0 indicates that the outcome cannot be predicted by any independent variables, and 1 indicates that the outcome can be predicted by the independent variables without any error.

When interpreting multiple regression results, beta coefficients are valid while holding all other variables constant ("ceteris paribus"). Output from multiple regression can be presented as an equation or displayed vertically in tabular form.

## Multiple Linear Regression (MLR) Usage Example

For example, an analyst might want to know how market changes affect ExxonMobil (XOM)'s stock price. In this case, the linear equation would use the S&P 500 index value as the independent variable or predictor, with XOM's price as the dependent variable.

In reality, multiple factors can predict the outcome of an event. For instance, ExxonMobil's stock price changes depend on more than just overall market performance. Other predictors such as oil prices, interest rates, and crude oil futures prices also affect ExxonMobil (XOM)'s price and other oil companies' stock prices. To understand relationships involving more than two variables, MLR is used.

MLR is used to determine mathematical relationships between multiple random variables. In other words, MLR examines the relationship between multiple independent variables and one dependent variable. Once the predictive ability of each independent variable on the dependent variable is determined, information from these multiple variables can be used to accurately predict the degree of impact on the outcome variable. The model formally creates a best-fit linear relationship that comes as close as possible to all individual data points.

Referring to the MLR equation above, in our example:

- yi = dependent variable - XOM's price
- xi1 = interest rates
- xi2 = oil prices
- xi3 = S&P 500 index value
- xi4 = crude oil futures prices
- B0 = y-intercept when time is zero
- B1 = regression coefficient measuring unit change in dependent variable when xi1 changes - impact of interest rate changes on XOM price
- B2 = coefficient measuring unit change in dependent variable when xi2 changes - impact of oil price changes on XOM price

Least squares estimates - B0, B1, B2...Bp are typically calculated by statistical software. Multiple variables can be included in the regression model, with each independent variable distinguished by numbers - 1, 2, 3, 4...p.

**Note:** Multiple regression can also be non-linear, in which case the dependent and independent variables do not follow a straight-line relationship.

Multiple regression models allow analysts to predict an outcome based on information from multiple explanatory variables. However, since each data point may differ slightly from the model's predicted result, the model isn't always completely accurate. The residual value E, the difference between actual and predicted results, is incorporated into the model to account for these small variations.

We ran the XOM price regression model in statistical computing software. It returned the following output:

Based on this output, analysts would conclude that if other variables remain constant, when market oil prices increase by 1%, XOM's price will increase by 7.8%. The model also indicates that for every 1% increase in interest rates, XOM's price will decrease by 1.5%. The R² shows that 86.5% of ExxonMobil's stock price changes can be explained by changes in interest rates, oil prices, oil futures, and the S&P 500 index.

## Differences Between Linear Regression and Multiple Regression

Ordinary Least Squares (OLS) regression compares the response of the dependent variable when certain explanatory variables change. However, dependent variables are rarely explained by just one variable. In such cases, analysts use multiple regression to attempt to explain the dependent variable through multiple independent variables.

Multiple regression can be either linear or nonlinear. MLR is based on the assumption that there is a linear relationship between the dependent variable and independent variables. It also assumes that there is no significant correlation between the independent variables.

## What Makes Multiple Regression Multiple?

Multiple regression examines the influence of multiple explanatory variables on a single outcome of interest. It assesses the relative effects of these explanatory variables (independent variables) on the dependent variable while holding all other variables in the model constant.

## Why Choose Multiple Regression Instead of Simple OLS Regression?

Dependent variables are rarely explained by a single variable. In such cases, analysts use multiple regression to attempt to explain the dependent variable through multiple independent variables. This model assumes there is no significant correlation between the independent variables.

## Can I perform multiple regression manually?

This is unlikely, as multiple regression models are relatively complex, and the complexity increases significantly when the number of variables in the model increases or the volume of data to be analyzed grows. To run multiple regression, you would likely need to use specialized statistical software or functions in programs like Excel.

## What is the Linear Meaning in Multiple Regression?

In multiple linear regression, the model calculates the best-fit line that minimizes the variance for each variable related to the dependent variable. It is called a linear model because it fits a straight line. There are also nonlinear regression models involving multiple variables, such as logistic regression, quadratic regression, and probit models.

## How are Multivariate Regression Models Applied in Finance?

Any econometric model involving multiple variables can be considered multivariate regression. Factor models compare two or more factors to analyze relationships between variables and their resulting performance. The Fama-French three-factor model is one such model that extends the Capital Asset Pricing Model (CAPM) by adding size risk and value risk factors to the market risk factor. By incorporating these two additional factors, the model adjusts for excess returns, making it a better tool for evaluating manager performance.

## Conclusion

MLR is a statistical tool used to predict variable outcomes based on two or more explanatory variables. If only one variable influences the dependent variable, a simple linear regression model is sufficient; conversely, if multiple factors affect the variable, MLR needs to be used.

A classic example is the drivers affecting a company's valuation in the stock market. Typically, a company's stock price is influenced by multiple factors. In this case, the dependent variable would be the stock price, which is what we're trying to predict, while the independent variables, or explanatory variables, would be the factors affecting the stock price.

## References

[1] Yale University. "[Multiple Linear Regression](http://www.stat.yale.edu/Courses/1997-98/101/linmult.htm)."

[2] CFA Institute. "[Basics of Multiple Regression and Underlying Assumptions](https://www.cfainstitute.org/en/membership/professional-development/refresher-readings/multiple-regression#:~:text=Five%20main%20assumptions%20underlying%20multiple,5%29%20independence%20of%20independent%20variables.)."

[3] Boston University Medical Campus-School of Public Health. "[Multiple Linear Regression](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/PH717-QuantCore/PH717-Module12-MultipleRegression/PH717-Module12-MultipleRegression3.html)."