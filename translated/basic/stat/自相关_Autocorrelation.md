---
{}
---

## What is Autocorrelation?

Autocorrelation is a mathematical representation of the similarity between a given time series and its delayed version across continuous time intervals. It is conceptually similar to correlation between two different time series, but autocorrelation uses the same time series twice: once in its original form and once in a form delayed by one or more time periods.

For example, if it rains today, data shows that it's more likely to rain tomorrow compared to if today was sunny. In investment terms, a stock's returns might exhibit strong positive autocorrelation, meaning that if it "goes up" today, it's more likely to go up tomorrow as well.

Naturally, autocorrelation can be a useful tool for traders, especially technical analysts.

### Key Points

- Autocorrelation represents the similarity between a given time series and its lagged version over continuous time intervals.
- Autocorrelation measures the relationship between a variable's current values and its past values.
- An autocorrelation of +1 indicates perfect positive correlation, while -1 indicates perfect negative correlation.
- Technical analysts can use autocorrelation to measure the impact of past prices on a security's future prices.

## Understanding Autocorrelation

Autocorrelation can also be called lagged correlation or serial correlation, as it measures the relationship between a variable's current values and its past values.

Let's look at a very simple example. The table below shows five percentage values. We compare these values with the same data on the right, where the values are simply shifted up by one row.

| Day | % Profit/Loss | Next Day % Profit/Loss |
|-----|---------------|----------------------|
| Monday | 10%         | 5%                  |
| Tuesday | 5%         | -2%                 |
| Wednesday | -2%      | -8%                 |
| Thursday | -8%       | -5%                 |
| Friday | -5%         |                     |

The results of calculating autocorrelation can fluctuate between -1 and +1.

An autocorrelation of +1 indicates perfect positive correlation (an increase observed in one time series leads to a corresponding increase in another time series).

On the other hand, an autocorrelation of -1 indicates perfect negative correlation (an increase observed in one time series leads to a corresponding decrease in another time series).

Autocorrelation measures linear relationships. Even when autocorrelation values are small, non-linear relationships may still exist between a time series and its lagged version.

The most commonly used method for testing autocorrelation is the Durbin-Watson test. Simply put, Durbin-Watson is a statistic used to detect autocorrelation through regression analysis.

The Durbin-Watson test results always range from 0 to 4. Values closer to 0 indicate stronger positive correlation, values closer to 4 indicate stronger negative autocorrelation, while values near the middle suggest little autocorrelation.

**Difference between Correlation and Autocorrelation:** Correlation measures the relationship between two variables, while autocorrelation measures the relationship between a variable and its lagged values.

So, why is autocorrelation important in financial markets? The reason is simple. Autocorrelation can be used for in-depth analysis of historical price movements, allowing investors to predict future price movements. Specifically, autocorrelation can be used to determine whether momentum trading strategies make sense.

## Application of Autocorrelation in Technical Analysis

Autocorrelation is particularly useful for technical analysis, as technical analysis primarily focuses on security price trends and their relationships using charting techniques. This contrasts with fundamental analysis, which focuses on a company's financial health and management.

Technical analysts can use autocorrelation to evaluate how past security prices influence future prices.

Autocorrelation can help determine whether a stock exhibits momentum factors. For example, if a stock with high positive autocorrelation shows significant gains for two consecutive days, it would be reasonable to expect that the stock will continue to rise over the next two days.

## Autocorrelation Example

Suppose Rain wants to determine if returns from a stock in their portfolio exhibit autocorrelation; that is, whether the stock's returns are correlated with returns from previous trading periods.

If returns show autocorrelation, Rain can treat it as a momentum stock, since past returns appear to influence future returns. Rain performs regression analysis using the previous period's returns as the independent variable and current returns as the dependent variable. They find that the previous day's returns have a positive autocorrelation of 0.8.

Since 0.8 is close to +1, past returns appear to be a very good positive predictor of future returns for this stock.

Therefore, Rain can adjust their portfolio to take advantage of the autocorrelation or momentum by continuing to hold the stock or adding more shares.

## What is the difference between autocorrelation and multicollinearity?

Autocorrelation refers to the degree of correlation between values of a variable over time. Multicollinearity occurs when there is correlation between independent variables, where one variable can be predicted by another variable. An example of autocorrelation would be measuring a city's weather on June 1st compared to the same city's weather on June 5th. Multicollinearity, on the other hand, measures the correlation between two independent variables, such as a person's height and weight.

## Why is Autocorrelation a Problem?

Most statistical tests assume that observations are independent of each other. In other words, the occurrence of one observation does not indicate anything about the occurrence of another observation. Autocorrelation is a problem for most statistical tests because it involves a lack of independence between values.

## What are the applications of autocorrelation?

Autocorrelation can be applied in many disciplines but is commonly seen in technical analysis. Technical analysts evaluate securities to identify trends and predict their future performance.

## Summary

Autocorrelation is the correlation between a time series and its lagged version over time. Although similar to correlation, autocorrelation uses the same time series twice. Financial analysts and traders use autocorrelation to study historical price movements and predict future trends. Technical analysts use autocorrelation to determine how historical security prices influence future prices. While autocorrelation is a very useful tool, it typically needs to be used in conjunction with other statistical indicators in financial analysis.