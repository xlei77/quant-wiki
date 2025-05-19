---
{}
---

## What is Correlation?

In the finance and investment industry, correlation is a statistical measure used to gauge the degree to which two securities move in relation to each other. Correlation is used in advanced portfolio management and is calculated as a correlation coefficient, which must have a value between -1.0 and +1.0.

### Main Content

- Correlation is a statistical measure used to assess the degree to which two variables move in relation to each other.
- In finance, correlation can measure how a stock moves in relation to a benchmark index (such as the S&P 500).
- Correlation is closely related to diversification, which is the concept of mitigating certain types of risk by investing in uncorrelated assets.
- Correlation measures association but cannot indicate whether x causes y, vice versa, or whether the association is caused by a third factor.
- Correlation is most easily identified through scatter plots, especially when variables have nonlinear but still strong relationships.

## What Can Correlation Tell You

Correlation shows the strength of the relationship between two variables, expressed as a correlation coefficient. The correlation coefficient value ranges between -1.0 and 1.0.

Perfect positive correlation means the correlation coefficient is exactly 1. This means that when one security moves up or down, the other security moves in the same direction synchronously. Perfect negative correlation means the two assets move in opposite directions, while zero correlation means there is no linear relationship at all.

For example, large-cap mutual funds typically have a high positive correlation with the Standard & Poor's (S&P) 500 index, close to 1. Small-cap stocks tend to have a positive correlation with the S&P index, but not as high, around 0.8.

However, put option prices and their underlying stock prices tend to be negatively correlated. A put option gives the owner the right (but not the obligation) to sell a specific amount of the underlying security at a predetermined price within a specified time frame.

When the underlying stock price falls, put option contracts become more profitable. In other words, as the stock price rises, the put option price decreases, representing a direct and pronounced negative correlation.

## How to Calculate Correlation

There are several methods to calculate correlation. This article will further discuss the most commonly used method, namely Pearson product-moment correlation. Pearson product-moment correlation measures the linear relationship between two variables. It can be used for any dataset with a finite covariance matrix. Below are the steps to calculate correlation.

**Important Note:** To avoid complex manual calculations, consider using the CORREL function in Excel.

Using the Pearson product-moment correlation method, the correlation coefficient r can be found using the following formula:

$$\begin{aligned}
&r = \frac { n \times ( \sum (X, Y) - ( \sum (X) \times \sum (Y) ) ) }{ \sqrt { ( n \times \sum (X ^ 2) - \sum (X) ^ 2 ) \times ( n \times \sum( Y ^ 2 ) - \sum (Y) ^ 2 ) } } \\
&\textbf{其中：}\\
&r=\text{相关系数}\\
&n=\text{观测值的数量}
\end{aligned}$$

## Correlation Example

Investment managers, traders, and analysts find calculating correlation very important because the risk reduction benefits of diversification depend on this statistic. Financial spreadsheets and software can quickly calculate correlation values.

As a hypothetical example, suppose an analyst needs to calculate the correlation between the following two datasets:

X: (41, 19, 23, 40, 55, 57, 33)

Y: (94, 60, 74, 71, 82, 76, 61)

Finding the correlation involves three steps. First is summing all X values to find SUM(X), summing all Y values to find SUM(Y), and multiplying each X value by its corresponding Y value and adding them together to find SUM(X,Y):

SUM(X) = (41 + 19 + 23 + 40 + 55 + 57 + 33) = 268

SUM(Y) = (94 + 60 + 74 + 71 + 82 + 76 + 61) = 518

SUM(X,Y) = (41 x 94) + (19 x 60) + (23 x 74) + ... (33 x 61) = 20,391

The next step is to take each X value, square it, and add all these values together to find SUM(X^2). This must also be done for Y values:

SUM(X^2) = (41^2) + (19^2) + (23^2) + ... (33^2) = 11,534

SUM(Y^2) = (94^2) + (60^2) + (74^2) + ... (61^2) = 39,174

Noting that there are seven observations n, the correlation coefficient r can be found using the following formula:

$$ \begin{aligned}&r = \frac { n \times ( \sum (X, Y) - ( \sum (X) \times \sum (Y) ) ) }{ \sqrt { ( n \times \sum (X ^ 2) - \sum (X) ^ 2 ) \times ( n \times \sum( Y ^ 2 ) - \sum (Y) ^ 2 ) } } &\textbf{其中：}\\
&r=\text{相关系数}\\
&n=\text{观测值的数量}\end{aligned} $$

In this example, the correlation will be:

r = 0.54

## Correlation and Portfolio Diversification

In investing, correlation is most important when it comes to diversified portfolios. Investors looking to reduce risk can do so by investing in uncorrelated assets. For example, consider an investor who owns airline stocks. If they discover that the airline industry has low correlation with the social media industry, they might choose to invest in social media stocks, knowing that negative impacts affecting one industry may not affect the other.

This is typically the approach when considering investments across asset classes. Stocks, bonds, precious metals, real estate, cryptocurrencies, commodities, and other types of investments have different relationships with each other. While some may be highly correlated, others might serve as hedges to diversify risk if they are uncorrelated.

**Note:** The risk that can be diversified away is called unsystematic risk. This type of risk is specific to companies, industries, or asset classes. Investing in different assets can reduce the correlation in your portfolio and decrease the unsystematic risk you face.

## Special Considerations

Correlation is typically determined by and related to other statistical considerations. When using statistics to analyze variables, correlation is commonly referenced.

In statistics, p-values are used to indicate whether research findings are statistically significant. Two variables can be determined to be correlated, but there may not be enough evidence to make it a strong claim. A high p-value indicates there is sufficient evidence to meaningfully conclude that the population correlation coefficient is different from zero.

The simplest way to visualize whether two variables are correlated is to graphically depict them using a scatter plot. Each point on a scatter plot represents a sample item. The x-axis of the scatter plot represents one of the variables being tested, while the y-axis of the scatter plot represents the other variable.

The correlation between two variables is often graphically represented as a linear line to show the relationship between the two variables. If two variables are positively correlated, an increasing linear line can be drawn on the scatter plot. If two variables are negatively correlated, a decreasing linear line can be drawn. The stronger the relationship between data points, the closer each data point will be to this line.

Scatter plots may be more useful when analyzing more complex data that might have varying relationships. For example, two variables might be positively correlated before a certain point, after which their relationship becomes negative. Such non-linear relationships might be harder to identify using formulas but are easier to spot when plotted on a scatter plot.

Finally, correlation can be easily depicted when scatter plots include density shading. Density shading or density ellipses are shaded areas on scatter plots that visually show where data points are most concentrated on the scatter plot. If variables are correlated, the density ellipse typically reflects the direction of the linear correlation line. Otherwise, a more circular density ellipse with no clear direction indicates lower correlation.

Another inherent difficulty in statistics is determining whether a relationship between two variables is caused by these variables. Consider the following statement:

"Most basketball players are tall. Therefore, if you play basketball, you will become tall."

Obviously, the statement above is incorrect. Individuals who are tall and aware of this advantage might be attracted to basketball because their natural physical abilities are best suited for the sport. However, since height and basketball playing might be positively correlated, statisticians and data scientists must be aware that a strong relationship between two variables could be caused by either variable.

## Limitations of Correlation

As with other aspects of statistical analysis, correlation can be misinterpreted. Even when the correlation between two variables appears strong, small sample sizes can produce unreliable results. Conversely, when two variables are actually correlated, small sample sizes might produce uncorrelated results.

Correlation typically becomes biased when outliers are present. Correlation only shows how one variable relates to another, and may not clearly identify how individual instances or results affect the correlation coefficient.

Correlation can also be misinterpreted if the relationship between two variables is non-linear. It is much easier to identify two variables that have either positive or negative correlation. However, two variables may still be correlated in more complex relationships.

## What is Correlation?

Correlation is a statistical term that describes the degree to which two variables move in coordination with each other. If two variables move in the same direction, these variables are said to have positive correlation. If they move in opposite directions, they have negative correlation.

## Why is Correlation Important in Finance?

Correlation plays a crucial role in finance as it is used to predict future trends and manage risks within investment portfolios. Today, correlations between assets can be easily calculated using various software programs and online services. Correlation, along with other statistical concepts, plays a vital role in the creation and pricing of derivatives and other complex financial instruments.

## What is an example of how correlation is used?

Correlation is a widely used concept in modern finance. For example, traders might use historical correlations to predict whether a company's stock will rise or fall in response to changes in interest rates or commodity prices. Similarly, portfolio managers may reduce their risk by ensuring that the individual assets in their portfolio are not overly correlated with each other.

## Are Higher Correlations Better?

Investors may have preferences regarding correlation levels in their portfolios. Generally, most investors prefer lower correlations as this can reduce the risk of their different assets or securities being affected by similar market conditions across their portfolio. However, risk-seeking investors or those looking to concentrate their funds in very specific types of industries or companies might be willing to accept higher correlations in their portfolio in exchange for greater potential returns.