---
{}
---

## What is Multicollinearity?

Multicollinearity refers to the existence of high correlation between two or more independent variables in a multiple regression model. When researchers or analysts attempt to determine the effect of each independent variable in predicting or understanding the dependent variable in a statistical model, multicollinearity can lead to distorted or misleading results.

Overall, multicollinearity leads to wider confidence intervals, resulting in less reliable probability estimates of independent variable effects.

In technical analysis, multicollinearity can lead to incorrect assumptions about investments. This typically occurs when analyzing a stock using multiple indicators of the same type.

### Key Points

- Multicollinearity is a statistical concept that refers to correlation between multiple independent variables in a model.
- Two variables are considered perfectly collinear if their correlation coefficient is +/- 1.0.
- Multicollinearity between independent variables will lead to reduced reliability of statistical inference.
- When analyzing investments, it's better to use indicators of different types rather than multiple indicators of the same type to avoid multicollinearity.
- Multicollinearity can lead to reduced reliability of results because the results you are comparing are typically similar.

## Understanding Multicollinearity

Statistical analysts use multiple regression models to predict the value of a specific dependent variable based on the values of two or more independent variables. The dependent variable is sometimes called the outcome, target, or criterion variable.

For example, a multiple regression model attempts to predict stock returns based on price-to-earnings (P/E ratio), market capitalization, or other data. Stock returns are the dependent variable (outcome), while various financial data serve as independent variables.

Multicollinearity in multiple regression models indicates that collinear independent variables are not truly independent. For instance, past performance may be related to market capitalization. Well-performing company stocks typically coincide with increased investor confidence, leading to higher demand for that company's stock, thus increasing its market value.

While multicollinearity doesn't affect regression estimates, it makes these estimates ambiguous, imprecise, and unreliable. Consequently, it becomes difficult to determine the individual effects of independent variables on the dependent variable. This inflates the standard errors of some or all regression coefficients.

A statistical technique called Variance Inflation Factor (VIF) can detect and measure collinearity in multiple regression models. VIF measures how much the variance of estimated regression coefficients is inflated compared to when the independent variables are not linearly related. A VIF of 1 means variables are uncorrelated; VIF between 1 and 5 indicates moderate correlation between variables; while VIF between 5 and 10 suggests high correlation between variables.

When analyzing stocks, you can detect multicollinearity by observing whether indicators plot the same pattern. For example, selecting two momentum indicators on a trading chart will typically generate trend lines showing the same momentum.

## Causes of Multicollinearity

Multicollinearity can occur when two independent variables are highly correlated. It can also arise when one independent variable is derived from calculations using other variables in the dataset, or when two independent variables provide similar and redundant results.

If you create two or three trading indicators of the same type using the same data, the result will be multicollinear because the data and the way they are manipulated are very similar.

**Important Note:** Statistical inferences from models containing multicollinearity may be unreliable.

## Types of Multicollinearity

Perfect multicollinearity refers to exact linear relationships between multiple independent variables, which can typically be observed in charts where data points fall exactly on the regression line. In technical analysis, this occurs when using two indicators that measure the same metric (such as volume) simultaneously. If one indicator is overlaid on another, there will be no difference between them.

High multicollinearity indicates that multiple independent variables have certain correlations, though not as tight as perfect multicollinearity. Not all data points fall on the regression line, but it still indicates that the correlations between data are too close to be useful.

In technical analysis, indicators with high multicollinearity typically produce very similar results.

Structural multicollinearity occurs when you create new features from data. For example, if you collect data and use it for other calculations, then perform regression analysis on the results, these results will be correlated because they are derived from each other.

This is a common type of multicollinearity in investment analysis, as the same data is used to create different indicators.

Poor experimental design or data collection processes, such as using observational data, typically lead to data-based multicollinearity, where some or all variables are correlated.

Stock data used to create indicators is typically collected from historical prices and trading volumes, so the possibility of multicollinearity due to improper data collection methods is relatively low.

## Multicollinearity in Investment

In investing, multicollinearity is a common consideration, especially when conducting technical analysis to predict future price movements of a security (such as stocks or commodity futures).

Market analysts aim to avoid using collinear technical indicators based on very similar or correlated inputs; these inputs refer not to the data itself, but rather how the data is manipulated to achieve results.

Therefore, analysis must be based on significantly different indicators to ensure the market is analyzed from independent analytical perspectives. For example, momentum indicators and trend indicators share the same data, but they are not completely collinear, and may not even have high collinearity. These two indicators produce different results based on how the data is manipulated.

**Note:** Most investors don't need to be overly concerned with the data and techniques behind indicator calculations—understanding what multicollinearity is and how it affects analysis is sufficient.

## How to Address Multicollinearity

One common method to eliminate multicollinearity problems is to first identify collinear independent variables, then remove one or more variables. In statistics, variance inflation factors are typically calculated to determine the degree of multicollinearity. Another approach to resolving multicollinearity is to collect more data under different conditions.

John Bollinger, the renowned technical analyst and creator of the Bollinger Bands indicator, wrote: "A fundamental rule for successful technical analysis requires avoiding multicollinearity between indicators." To address this issue, analysts avoid using two or more technical indicators of the same type. Instead, they use one type of indicator (such as momentum indicators) to analyze a security, then use another type of indicator (such as trend indicators) for separate analysis.

For example, the Stochastic Oscillator, Relative Strength Index (RSI), and Williams %R are all momentum indicators that rely on similar inputs and may produce similar results. In the above image, the Stochastic and Williams indicators are identical, so using both doesn't reveal much additional information. In this case, it's better to remove one of these indicators and use an indicator that doesn't track momentum. In the image below, the Stochastic Oscillator shows price momentum, while the Bollinger Bandwidth shows price consolidation before price movements.

## How to Handle Multicollinearity?

To reduce multicollinearity in statistical models, you can remove specific variables identified as the most collinear. You can also try combining or transforming problematic variables to reduce their correlation. If this is still not feasible, there are improved regression models that better handle multicollinearity, such as ridge regression, principal component regression, or partial least squares regression. In stock analysis, the best approach is to select indicators of different types.

## What is Multicollinearity in Regression?

Multicollinearity describes the relationship between variables where they are correlated with each other. Multicollinear data creates problems in analysis because the variables are not independent.

## How to Interpret Multicollinearity Results?

When the Variance Inflation Factor (VIF) exceeds five, the data will exhibit high multicollinearity. If the VIF is between 1 and 5, the variables are moderately correlated, and when it equals 1, it indicates no correlation. In technical analysis, indicators are often the same.

## What is Perfect Collinearity?

Perfect collinearity exists when there is an exact 1:1 relationship between two independent variables in a model. The correlation coefficient can be either +1.0 or -1.0.

## Why is Multicollinearity a Problem?

Multicollinearity is a problem because it produces regression model results that are not reliable enough. This is due to wider confidence intervals (increased standard errors) potentially reducing the statistical significance of regression coefficients. In stock analysis, it may lead to incorrect impressions or assumptions about investments.

## Summary

Multicollinearity exists in multiple regression equations where independent variables are highly correlated with multiple other independent variables. Multicollinearity is problematic because it makes statistical inference unreliable. However, the Variance Inflation Factor (VIF) can provide information about which variables are redundant, allowing for the removal of variables with high VIF values.

In technical analysis, multicollinearity becomes an issue because many indicators present data in similar ways. To avoid this, it's best to use indicators that don't measure the same trends.