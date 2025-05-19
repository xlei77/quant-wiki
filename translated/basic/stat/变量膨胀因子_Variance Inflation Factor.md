---
{}
---

## What is the Variance Inflation Factor (VIF)?

The Variance Inflation Factor (VIF) is a measure of the degree of multicollinearity in regression analysis. Multicollinearity occurs when there are correlations among multiple independent variables in a multivariate regression model, which can adversely affect regression results. Therefore, the Variance Inflation Factor estimates the degree to which the variance of regression coefficients is inflated due to multicollinearity.

### Key Points

- Variance Inflation Factor (VIF) provides a measure of multicollinearity among independent variables in multiple regression models.
- Identifying multicollinearity is crucial because, although it doesn't reduce the model's explanatory power, it decreases the statistical significance of independent variables.
- A high VIF value for an independent variable indicates strong collinearity with other variables, which needs to be considered or adjusted in model structure and variable selection.

## Understanding the Variance Inflation Factor (VIF)

The Variance Inflation Factor is a tool for identifying the degree of multicollinearity. Multiple regression is used when researchers want to test the impact of multiple variables on a specific outcome. The dependent variable is the result influenced by independent variables. Multicollinearity occurs when there is a linear relationship or correlation between one or more independent variables.

Multicollinearity creates problems in multiple regression models because independent variables influence each other, making them not truly independent, which makes it difficult to test how combinations of independent variables affect the dependent variable in the regression model.

Although multicollinearity does not reduce the overall predictive power of the model, it may lead to regression coefficient estimates that lack statistical significance. In a sense, this can be viewed as a form of double-counting in the model.

In statistics, multiple regression models with high multicollinearity make it more difficult to estimate the relationship between each independent variable and the dependent variable. In other words, when two or more independent variables are closely related or measure almost the same thing, their potential effects are counted repeatedly across variables. When independent variables are highly correlated, it becomes difficult to determine which variable is influencing the dependent variable.

Small changes in data or adjustments to the model equation structure can lead to large and unstable changes in the estimated coefficients of independent variables. This is problematic because the goal of many econometric models is precisely to test these statistical relationships between independent and dependent variables accurately.

To ensure proper model specification and functioning, multicollinearity tests can be conducted. The Variance Inflation Factor is one such measurement tool. Using the Variance Inflation Factor helps identify the severity of any multicollinearity problems for model adjustment. The VIF measures the degree to which the behavior (variance) of an independent variable is affected by interactions or correlations with other independent variables.

The Variance Inflation Factor provides a quick measure for evaluating variables' contribution to standard errors in regression. When significant multicollinearity problems exist, the VIF for the related variables will be very large. Once these variables are identified, various methods can be used to eliminate or combine collinear variables to address the multicollinearity problem.

## VIF Formula and Calculation

The VIF formula is:

$$ \begin{aligned}&\text{VIF}_i = \frac{ 1 }{ 1 - R_i^2 } \\&\textbf{其中:} \\&R_i^2 = \text{在剩余的自变量上回归第} i \text{个自变量的未调整决定系数} \\\end{aligned} $$

## What can VIF tell you?

When $R_i^2$ equals 0, the VIF or tolerance equals 1, meaning that the $i$ independent variable is uncorrelated with the remaining independent variables, indicating no multicollinearity.

Generally speaking:

- VIF equals 1 = independent variables are uncorrelated
- VIF between 1 and 5 = independent variables are moderately correlated
- VIF greater than 5 = independent variables are highly correlated

The higher the VIF, the more likely multicollinearity exists and requires further investigation. When VIF exceeds 10, there is significant multicollinearity that needs to be corrected.

## Example of Using VIF

For example, suppose an economist wants to test whether there is a statistically significant relationship between unemployment rate (independent variable) and inflation rate (dependent variable). If other independent variables related to unemployment, such as initial jobless claims, are included in the model, multicollinearity may be introduced.

The overall model might show strong statistical explanatory power, but it becomes impossible to determine whether the effect is primarily due to the unemployment rate or initial jobless claims. This is precisely the type of problem that VIF can detect, and it might suggest either removing one of the variables from the model or finding a way to combine them to capture their joint effect, depending on the hypothesis the researcher wants to test.

## What is a good VIF value?

As a rule of thumb, VIF values below 3 are not cause for concern. As VIF increases, the reliability of your regression results will decrease.

## What does a VIF of 1 mean?

A VIF of 1 means that the independent variables are uncorrelated and there is no multicollinearity in the regression model.

## What is VIF used for?

VIF is used to measure the strength of correlation between independent variables in regression analysis. This correlation is known as multicollinearity, which can cause problems in regression models.

## Summary

While moderate multicollinearity in regression models is acceptable, high multicollinearity may raise concerns.

Two measures can be taken to correct high multicollinearity. First, one or more highly correlated variables can be removed since they provide redundant information. The second approach is to use Principal Component Analysis or Partial Least Squares Regression instead of Ordinary Least Squares regression, which can either reduce variables to a smaller uncorrelated set or create new uncorrelated variables. This will improve the model's predictability.

## References

[1] CFI. "[Variance Inflation Factor](https://corporatefinanceinstitute.com/resources/knowledge/other/variance-inflation-factor-vif/)."

[2] Isixsigma. "[Variance Inflation Factor (VIF)](https://www.isixsigma.com/dictionary/variance-inflation-factor-vif/)."