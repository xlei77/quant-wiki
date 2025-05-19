---
{}
---

## What is Correlation Coefficient?

The correlation coefficient is a statistical measure that quantifies the strength of the linear relationship between two variables. Its values range from -1 to 1. A correlation coefficient of -1 indicates a perfect negative correlation, meaning that when values in one series increase, values in the other series decrease, and vice versa. A correlation coefficient of 1 indicates a perfect positive correlation, or direct relationship. A correlation coefficient of 0 indicates no linear relationship.

Correlation coefficients are widely used in scientific and financial fields to evaluate the degree of association between two variables, factors, or datasets. For example, since high oil prices benefit oil producers, one might assume that the correlation between oil prices and future returns of oil stocks would be highly positive. However, the correlation coefficient calculated from market data for these variables shows moderate and inconsistent correlation over longer periods.

### Key Points

- Correlation coefficients are used to evaluate the strength of association between data variables.
- The most common correlation coefficient is called the "Pearson correlation coefficient," which measures the strength and direction of linear relationships between two variables.
- Values always range between -1 (perfect negative correlation) and 1 (perfect positive correlation).
- Values close to zero indicate no linear relationship or very weak correlation.
- The coefficient value needed to determine meaningful correlations varies by application. The statistical significance of correlations can be calculated using the correlation coefficient and the number of data points in the sample, assuming the sample follows a normal distribution.

## Understanding Correlation Coefficients

Different types of correlation coefficients are used to evaluate correlations based on the characteristics of the data being compared. Among these, the most commonly used is the Pearson coefficient, also known as "Pearson's R," which measures the strength and direction of the linear relationship between two variables.

The Pearson coefficient uses a mathematical statistical formula to measure how closely data points combining two variables (plotting values from one data series on the x-axis and corresponding values from the other series on the y-axis) align with the best-fit line. The best-fit line can be determined through regression analysis.

**Important Note:** The most common Pearson coefficient cannot evaluate non-linear associations between variables, nor can it distinguish between dependent and independent variables.

The further the coefficient is from zero, whether positive or negative, the better the fit and the stronger the correlation. Values of -1 (negative correlation) and 1 (positive correlation) describe a perfect fit, where all data points align along a straight line, indicating perfect correlation between variables.

In other words, the relationship is so predictable that the matching value of one variable can be determined from the value of the other variable. The closer the correlation coefficient is to zero, the weaker the correlation, until zero indicates no linear relationship at all.

The assessment of correlation strength based on correlation coefficient values varies across different applications. In physics and chemistry, correlation coefficients need to be below -0.9 or above 0.9 to be considered meaningful, while in social sciences, this threshold might be just -0.5 or 0.5.

For correlation coefficients derived from sampling, the determination of statistical significance depends on the p-value, which is calculated based on the size of the data sample and the value of the coefficient.

## Correlation Coefficient Formula

To calculate the Pearson correlation coefficient, you first need to determine the standard deviation of each variable and the covariance between them. The correlation coefficient is the covariance divided by the product of the standard deviations of these two variables.

$$ \begin{aligned} &\rho_{xy} = \frac { \text{Cov} ( x, y ) }{ \sigma_x \sigma_y } \\ &\textbf{其中：} \\ &\rho_{xy} = \text{皮尔逊积矩相关系数} \\ &\text{Cov} ( x, y ) = \text{变量 } x \text{ 和 } y \text{ 的协方差} \\ &\sigma_x = \text{变量 } x \text{ 的标准差} \\ &\sigma_y = \text{变量 } y \text{ 的标准差} \\ \end{aligned} $$

Standard deviation measures how dispersed the data is from its mean value. Covariance shows whether two variables tend to move in the same direction, while the correlation coefficient measures the strength of this relationship on a normalized scale (-1 to 1).

The above formula can be further detailed as:

$$ \begin{aligned}&r = \frac { n \times ( \sum (X, Y) - ( \sum (X) \times \sum (Y) ) ) }{ \sqrt { ( n \times \sum (X ^ 2) - \sum (X) ^ 2 ) \times ( n \times \sum( Y ^ 2 ) - \sum (Y) ^ 2 ) } } \\&\textbf{其中：}\\&r=\text{相关系数}\\&n=\text{观察数}\end{aligned} $$

## Correlation Statistics and Investment

Correlation coefficients are particularly useful in evaluating and managing investment risks. For example, Modern Portfolio Theory suggests that diversification can reduce the volatility of portfolio returns, thereby reducing risk. The correlation coefficient between historical returns can indicate whether adding a particular investment to a portfolio will improve its degree of diversification.

Correlation calculations are also fundamental to factor investing, a strategy that constructs portfolios based on factors correlated with excess returns. Meanwhile, quantitative traders use historical correlations and correlation coefficients to predict short-term changes in security prices.

## Limitations of Pearson Correlation Coefficient

As the saying goes, correlation does not imply causation, and the Pearson coefficient cannot determine whether there is a dependency relationship between correlated variables.

Furthermore, the correlation coefficient cannot show how much of the variation in the dependent variable can be attributed to the independent variable. This is shown by the coefficient of determination (also known as "R-squared"), which is simply the square of the correlation coefficient.

The correlation coefficient also does not describe the slope of the best-fit line; this slope can be determined through least squares method in regression analysis.

The Pearson correlation coefficient cannot be used to evaluate non-linear associations or associations derived from sampling data that does not follow normal distribution. It can also be distorted by outliers—data points that are far from the scatter plot's distribution.

These relationships can be analyzed using non-parametric methods, such as Spearman's correlation coefficient, Kendall's rank correlation coefficient, or multiple correlation coefficient.

## Finding Correlation Coefficients in Excel

There are several ways to calculate correlations in Excel. The simplest method is to input two data series into adjacent columns and use the built-in correlation formula:

If you want to create a correlation matrix between multiple datasets, Excel provides a Data Analysis add-in. Before using this add-in, you need to enable the Data Analysis Toolpack first. To do this, click "Options" in "File," which will open the Excel Options dialog box. In this box, click "Add-ins," then select "Excel Add-ins" from the "Manage" dropdown menu, and click "Go." This will bring up the Add-ins box. Check the "Analysis ToolPak" checkbox and click "OK." This completes the enabling process.

When using the Data Analysis add-in, click the "Data" tab and select "Data Analysis," which will open a box. In the box, click "Correlation" and then "OK." The Correlation box will now open, where you can manually enter the input range or select the relevant cells.

In this case, since our columns have headers, we need to check the "Labels in First Row" box so Excel knows to treat them as headers. Then, you can choose to output the results on the same worksheet or a new worksheet.

Pressing Enter will generate the correlation matrix. You can add some text and conditional formatting to organize the results.

## Are R and R2 the same?

No, R and R2 are not the same when analyzing coefficients. R represents the value of the Pearson correlation coefficient, used to indicate the strength and direction between variables, while R2 represents the coefficient of determination, used to determine the strength of the model.

## How to Calculate the Correlation Coefficient?

The correlation coefficient is calculated by determining the covariance of variables and dividing that number by the product of these variables' standard deviations.

## What is the Role of Correlation Coefficients in Investment?

Correlation coefficients play a crucial role in portfolio risk assessment and quantitative trading strategies. For example, some portfolio managers monitor the correlation coefficients of their held assets to limit portfolio volatility and risk.

## Summary

Correlation coefficient describes how one variable moves in relation to another variable. Positive correlation indicates that two variables move in the same direction, with a value of 1 indicating perfect positive correlation. A value of -1 indicates perfect negative correlation, while 0 indicates no linear correlation exists.

## References

[1] DataTrek Research. "[Oil Prices/Energy Stock Correlations, Rate Expectations](https://www.datatrekresearch.com/oil-prices-energy-stock-correlations-rate-expectations/)."