---
{}
---

## What is Correlation Coefficient?

A correlation coefficient is a statistical measure that quantifies the strength of the linear relationship between two variables. Its values range from -1 to 1. A correlation coefficient of -1 indicates perfect negative correlation or inverse relationship, where values in one sequence increase while values in the other sequence decrease, and vice versa. A coefficient of 1 indicates perfect positive correlation or direct relationship. A correlation coefficient of 0 indicates no linear relationship.

Correlation coefficients are used in scientific and financial fields to evaluate the degree of association between two variables, factors, or datasets. For example, since high oil prices benefit crude oil producers, one might expect the correlation between oil prices and forward returns of oil stocks to be strongly positive.

However, calculating the correlation coefficient between these variables using market data shows that the correlation is moderate and inconsistent over longer periods. [1]

### Key Points

- Correlation coefficients are used to evaluate the strength of association between data variables.
- The most common is the Pearson correlation coefficient, which measures the strength and direction of the linear relationship between two variables.
- The value range is always from -1 (perfect inverse or negative correlation) to 1 (perfect positive correlation). Values close to or equal to zero indicate no linear relationship or very weak correlation.
- The coefficient value needed to indicate a meaningful association depends on the specific application. The statistical significance of correlation can be calculated using the correlation coefficient and the number of data points in the sample, assuming the population follows a normal distribution.

## Understanding Correlation Coefficients

Different types of correlation coefficients are used to evaluate correlations based on the properties of the data being compared. By far the most common is the Pearson coefficient, or Pearson's r, which measures the strength and direction of the linear relationship between two variables. The Pearson coefficient cannot evaluate nonlinear associations between variables, nor can it distinguish between dependent and independent variables.

The Pearson coefficient uses mathematical statistical formulas to measure how closely data points combining two variables (values from one data series plotted on the x-axis and corresponding values from another series plotted on the y-axis) align with a best-fit line. The best-fit line can be determined through regression analysis.

The further the coefficient is from zero, whether positive or negative, the better the fit and the stronger the correlation. Values of -1 (negative correlation) and 1 (positive correlation) describe perfect fits where all data points align on a straight line, indicating complete correlation between variables.

In other words, the relationship is so predictable that the value of one variable can be determined from the matching value of the other variable. The closer the correlation coefficient is to zero, the weaker the correlation, until at zero there is no linear relationship at all.

The assessment of correlation strength based on correlation coefficient values varies by application. In physics and chemistry, correlation coefficients should be below -0.9 or above 0.9 to be considered meaningful, while in social sciences, thresholds may be as high as -0.5 and as low as 0.5.

For correlation coefficients obtained from sampling, the determination of statistical significance depends on the p-value, which is calculated from the size of the data sample and the value of the coefficient.

## Correlation Coefficient Formula

To calculate the Pearson correlation coefficient, first determine the standard deviation of each variable and the covariance between them. The correlation coefficient is the covariance divided by the product of the standard deviations of the two variables.

$$ \begin{aligned} &\rho_{xy} = \frac { \text{Cov} ( x, y ) }{ \sigma_x \sigma_y } \\ &\textbf{其中:} \\ &\rho_{xy} = \text{皮尔逊积矩相关系数} \\ &\text{Cov} ( x, y ) = \text{变量 } x \text{ 和 } y \text{ 的协方差} \\ &\sigma_x = \text{变量 } x \text{ 的标准差} \\ &\sigma_y = \text{变量 } y \text{ 的标准差} \\ \end{aligned} $$

Standard deviation is a measure of how dispersed data points are from their mean value. Covariance indicates whether two variables tend to move in the same direction, while the correlation coefficient measures the strength of this relationship on a standardized scale (from -1 to 1).

The above formula can be further expanded as

$$ \begin{aligned}&r = \frac { n \times ( \sum (X, Y) - ( \sum (X) \times \sum (Y) ) ) }{ \sqrt { ( n \times \sum (X ^ 2) - \sum (X) ^ 2 ) \times ( n \times \sum( Y ^ 2 ) - \sum (Y) ^ 2 ) } } \\&\textbf{其中:}\\&r=\text{相关系数}\\&n=\text{观测数量}\end{aligned} $$

## Correlation Statistics and Investment

Correlation coefficients are particularly useful in evaluating and managing investment risks. For example, Modern Portfolio Theory suggests that diversification can reduce the volatility of portfolio returns, thereby reducing risk. The correlation coefficient between historical returns can indicate whether adding an investment to a portfolio will improve its diversification.

Correlation calculations are also a key component of factor investing, a strategy that constructs portfolios based on factors correlated with excess returns. Meanwhile, quantitative traders use historical correlations and correlation coefficients to predict near-term changes in security prices.

## Limitations of Pearson Correlation Coefficient

As commonly stated, correlation does not imply causation, and the Pearson coefficient cannot determine whether one of the correlated variables depends on the other.

The correlation coefficient also cannot show what proportion of the change in the dependent variable is attributable to the independent variable. This is represented by the coefficient of determination, also known as R-squared, which is simply the square of the correlation coefficient.

The correlation coefficient does not describe the slope of the best-fit line; the slope can be determined through least squares method in regression analysis.

The Pearson correlation coefficient cannot be used to evaluate non-linear associations or associations produced by sampling data that does not follow a normal distribution. It can also be distorted by outliers—data points that lie far from the distribution's scatter plot.

These relationships can be analyzed using non-parametric methods, such as Spearman's correlation coefficient, Kendall's rank correlation coefficient, or polychoric correlation coefficient.

## Finding Correlation Coefficients in Excel

The simplest way to calculate correlations in Excel is to enter two data series in adjacent columns and use the built-in correlation formula:

If you want to create a correlation matrix across a series of datasets, Excel has a "Data Analysis" add-in under "Analysis" on the "Data" tab.

Select the returns table. In this case, our columns have headers, so we want to check the "Labels in First Row" box so Excel knows to treat these as headers. Then you can choose to output on the same worksheet or a new worksheet.

Pressing enter will generate the correlation matrix. You can add some text and conditional formatting to clean up the results.

## Are R and R2 the same?

No, R and R2 are not the same when analyzing coefficients. R represents the value of the Pearson correlation coefficient, which is used to indicate the strength and direction between variables, while R2 represents the coefficient of determination, which is used to determine the strength of the model.

## How to Calculate the Correlation Coefficient?

The correlation coefficient is calculated by determining the covariance of variables, then dividing this number by the product of these variables' standard deviations.

## How is Correlation Coefficient Used in Investment?

Correlation coefficients play a crucial role in portfolio risk assessment and quantitative trading strategies. For example, some portfolio managers monitor the correlation coefficients of their holdings to limit portfolio volatility and risk.

## Conclusion

The correlation coefficient describes how one variable moves in relation to another variable. A positive correlation indicates that both move in the same direction, with a value of 1 indicating perfect positive correlation. A value of -1 indicates perfect negative correlation or inverse correlation, while zero indicates no linear correlation.

## References

[1] DataTrek Research. "[Oil Prices/Energy Stock Correlations, Rate Expectations](https://www.datatrekresearch.com/oil-prices-energy-stock-correlations-rate-expectations/)."