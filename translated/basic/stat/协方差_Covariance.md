---
{}
---

## What is Covariance?

Covariance is a statistical tool used to measure the directional relationship between the returns of two assets. A positive covariance indicates that asset returns fluctuate together, while a negative covariance implies they move in opposite directions.

Covariance can be calculated by analyzing the magnitude of return fluctuations (standard deviation from expected returns) or by multiplying the correlation between two random variables by their respective standard deviations.

### Key Points

- Covariance is a statistical tool used to determine the relationship between movements of two random variables.
- When two stocks trend in the same direction, their covariance is positive; when they move in opposite directions, the covariance is negative.
- Covariance differs from correlation coefficient, which measures the strength of the relationship.
- Covariance is an important tool in Modern Portfolio Theory (MPT) for determining which securities should be included in a portfolio.
- By combining assets with negative covariance, the risk and volatility in a portfolio can be reduced.

## Understanding Covariance

Covariance measures how two random variables' means change together. For example, if stock A's returns increase when stock B's returns increase, and the same relationship holds when both stocks' returns decrease, then these two stocks are said to have positive covariance. In finance, covariance is used to calculate diversification of security holdings.

When analysts obtain price information from selected stocks or funds, they can calculate covariance using the following formula:

$$ \begin{aligned}&\text{协方差} = \sum \frac{ ( \text{Return}_{abc} - \text{Average}_{abc} ) \times ( \text{Return}_{xyz} - \text{Average}_{xyz} ) }{ \text{样本数量} - 1 } \\&\textbf{其中:} \\&\text{Return}_{abc} = \text{ABC股票的日回报} \\&\text{Average}_{abc} = \text{ABC在此期间的平均回报} \\&\text{Return}_{xyz} = \text{XYZ股票的日回报} \\&\text{Average}_{xyz} = \text{XYZ在此期间的平均回报} \\&\text{样本数量} = \text{采样天数} \\\end{aligned} $$

## Types of Covariance

Covariance equations are used to determine the directional relationship between two variables, in other words, to determine whether they tend to move in the same direction or in opposite directions. Positive or negative covariance values can be used to determine this relationship.

A positive covariance between two variables indicates that these variables typically have high or low values at the same time. In other words, when stock one and stock two have a positive covariance, when stock one is above average, stock two is similarly above average, and vice versa. When plotted on a two-dimensional graph, the data points typically slope upward.

When the calculated covariance is negative, it indicates an inverse relationship between the two variables. That is, when stock one's value is below average, it tends to be accompanied by stock two's value being above average, and vice versa.

## Applications of Covariance

Covariance plays a crucial role in finance and Modern Portfolio Theory (MPT). For example, in the Capital Asset Pricing Model (CAPM), which is used to calculate expected returns on assets, covariance is used as a key variable in the formula - beta. Beta in CAPM measures the volatility or systematic risk of a security compared to the overall market; it's a practical indicator that uses covariance to assess an investor's risk exposure to a particular security.

Meanwhile, portfolio theory utilizes covariance to statistically reduce the overall risk of a portfolio through covariance-driven diversification, thereby protecting it against volatility.

**Note:** Financial assets with similar returns don't offer much diversification. Therefore, a diversified portfolio typically includes combinations of financial assets with different covariances.

## Covariance and Variance

Covariance is related to variance, which is a statistical measure of the distribution of points in a dataset. Both variance and covariance measure how data points are distributed around their calculated mean. However, variance measures data distribution along a single axis, while covariance examines the directional relationship between two variables.

In a financial context, covariance is used to study the performance relationship between different investments. A positive covariance indicates that two assets tend to perform well simultaneously, while a negative covariance suggests they tend to move in opposite directions. Investors may seek investments with negative covariance to help achieve asset diversification.

## Covariance and Correlation

Covariance and correlation are different concepts; the latter is another statistical measure commonly used to assess the relationship between two variables. While covariance measures the directional relationship between two variables, correlation measures the strength of that relationship. It is typically expressed through a correlation coefficient, ranging from -1 to +1.

**Important:** Although covariance does measure the directional relationship between two assets, it does not indicate the strength of their relationship; the correlation coefficient is a more appropriate measure of this strength.

If the correlation coefficient is close to +1 (positive correlation) or -1 (negative correlation), the correlation is considered strong. A coefficient close to zero indicates a weak relationship between the two variables.

## Covariance Calculation Example

The capital Greek letter σ (Σ) represents the sum of all calculations. Therefore, calculations need to be performed for each day and the results summed up. For example, to calculate the covariance between two stocks, assuming you have four days of stock price data and use the following formula:

$$ \begin{aligned}&\text{协方差} = \sum \frac{ ( \text{Ret}_{abc} - \text{Avg}_{abc} ) \times ( \text{Ret}_{xyz} - \text{Avg}_{xyz} ) }{ \text{样本数量} - 1 } \\\end{aligned} $$

|Day|ABC|XYZ|
|---|---|---|
|1|1.2%|3.1%|
|2|1.8%|4.2%|
|3|2.2%|5.0%|
|4|1.5%|4.2%|

You will find the average returns for ABC (1.675%) and XYZ (4.125%), subtract them from their respective values, and multiply them together. Perform the following calculation for each day:

$$ \begin{aligned}&\text{第1天} = (1.2\% - 1.675\%) \times (3.1\% - 4.125\%) = 0.487 \\\end{aligned} $$

$$ \begin{aligned}&\text{第2天} = (1.8\% - 1.675\%) * (4.2\% - 4.125\%) = 0.009 \\\end{aligned} $$

$$ \begin{aligned}&\text{第3天} = (2.2\% - 1.675\%) * (5.0\% - 4.125\%) = 0.459 \\\end{aligned} $$

$$ \begin{aligned}&\text{第4天} = (1.5\% - 1.675\%) * (4.2\% - 4.125\%) = -0.013 \\\end{aligned} $$

Add up the results from each day:

$$ \begin{aligned}&0.487 + 0.009 + 0.459 - 0.013 = 0.943 \\\end{aligned} $$

Your sample size is four, so subtract one from four and then divide the previous result by this number:

$$ \begin{aligned}&\frac{ 0.943 }{ 3 } = .314 \\\end{aligned} $$

The sample covariance is 0.314, with the positive value indicating that the returns of these two stocks move similarly.

## What Does Zero Covariance Mean?

Zero covariance indicates that there is no clear directional relationship between the measured variables. In other words, a high value of one stock is equally likely to be paired with either a high value or a low value of another stock.

## What is the difference between covariance and variance?

Covariance and variance are used to measure the distribution of points in a dataset. However, variance is typically used for datasets with only one variable and indicates how closely data points cluster around the mean. Covariance measures the directional relationship between two variables. A positive covariance indicates that both variables tend to be high or low together; a negative covariance suggests that when one variable is high, the other tends to be low.

## What is the difference between covariance and correlation?

Covariance measures the direction of the relationship between two variables, while correlation measures the strength of that relationship. When variables move in the same direction, both covariance and correlation are positive; when they move in opposite directions, both are negative. However, the correlation coefficient always ranges from -1 to +1, with extreme values indicating strong relationships.

## How is Covariance Calculated?

For a set of data points with two variables, covariance measures by taking the difference between each variable and its mean. These differences are then multiplied together and averaged across all data points. In mathematical notation:

Covariance = Σ [ (Returnabc - Averageabc) * (Returnxyz - Averagexyz) ] ÷ [Number of Samples - 1]

## Conclusion

Covariance is an important statistical indicator for comparing relationships between multiple variables. In investing, covariance is used to identify assets that can help diversify a portfolio.