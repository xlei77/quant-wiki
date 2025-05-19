---
{}
---

## What is the Empirical Rule?

The Empirical Rule, also known as the Three-Sigma Rule or the 68-95-99.7 Rule, is a statistical rule stating that in a normal distribution, almost all observed data falls within three standard deviations (denoted by the Greek letter σ) of the mean (denoted by the Greek letter μ).

Specifically, the Empirical Rule predicts that in a normal distribution, 68% of observations will fall within the first standard deviation (μ ± σ), 95% will fall within the first two standard deviations (μ ± 2σ), and 99.7% will fall within the first three standard deviations (μ ± 3σ).

### Key Points

- The empirical rule states that in a normal distribution, almost all observations will fall within three standard deviations of the mean.
- According to this rule, 68% of the data will fall within one standard deviation, 95% within two standard deviations, and 99.7% within three standard deviations.
- The three-sigma limits following the empirical rule are used to set upper and lower control limits in statistical quality control charts and risk analysis.

## Understanding the Empirical Rule

The empirical rule is commonly used in statistics to predict final results. After calculating the standard deviation, this rule can serve as a rough estimate of the results for data that is yet to be collected and analyzed, before complete data collection.

This probability distribution can serve as an evaluation technique because in some cases, collecting appropriate data may be time-consuming or even impossible. Such considerations are particularly important when companies review their quality control measures or assess risk exposure. For example, the commonly used risk tool "Value at Risk (VaR)" assumes that the probability distribution of risk events follows a normal distribution.

The empirical rule is also used as a rough method for testing the "normality" of a distribution. If too many data points fall outside the boundaries of three standard deviations, it indicates that the distribution is not normal and may be skewed or follow another distribution.

The empirical rule is also known as the three-sigma rule, as "three sigma" refers to the statistical distribution of data within plus or minus three standard deviations from the mean in a normal distribution (bell curve), as shown in the figure below.

## Rule of Thumb Example

Suppose the lifespan of animals in a zoo follows a normal distribution. Each animal has an average lifespan of 13.1 years (mean), with a standard deviation of 1.5 years. If someone wants to know the probability of an animal living beyond 14.6 years, they can use the rule of thumb. Given that the distribution's mean is 13.1 years, here are the age ranges for each standard deviation:

- One standard deviation (μ ± σ): (13.1 - 1.5) to (13.1 + 1.5), i.e., 11.6 to 14.6
- Two standard deviations (μ ± 2σ): 13.1 - (2 × 1.5) to 13.1 + (2 × 1.5), i.e., 10.1 to 16.1
- Three standard deviations (μ ± 3σ): 13.1 - (3 × 1.5) to 13.1 + (3 × 1.5), i.e., 8.6 to 17.6

To solve this problem, one needs to calculate the total probability of an animal living to 14.6 years or longer. The rule of thumb shows that 68% of the distribution falls within one standard deviation, which is between 11.6 and 14.6 years. Therefore, the remaining 32% of the distribution lies outside this range. Half of this is above 14.6 years, and half is below 11.6 years. Thus, the probability of an animal living beyond 14.6 years is 16% (calculated as 32% divided by 2).

## Application of Empirical Rules in Investment

Most market data does not follow a normal distribution, so the 68-95-99.7 rule generally doesn't apply to investments. However, many analysts still use some aspects—such as standard deviation—to estimate volatility.

You can calculate the standard deviation of portfolios, indices, or other investments and use it to evaluate volatility. If you have access to a spreadsheet and prices or returns for your chosen investment, calculating the standard deviation of an investment is straightforward.

Market analysts typically express standard deviation as a percentage. For example, from May 2, 2023, to June 2, 2023, the daily standard deviation (annualized) of the S&P 500 index (using daily closing prices) was 13.29%.

In a spreadsheet, you can paste returns, prices, or values, calculate the percentage change from the previous trading day, and use the standard deviation function: 1

**Important Note:** Using trading data from more than one month, such as three years or more, will yield more accurate results. The example below uses daily values for the index over one month and annualizes the standard deviation to limit the table size.

To annualize the standard deviation, multiply it by the square root of the number of trading days in a year—typically 252.

| S&P 500 Standard Deviation (Annualized)
|---|---|---|---|
||A|B|C|D
|1|Date|Close|Daily Change|Formula
|2|05/02/23|4119.58|-|-
|3|05/03/23|4090.75|-0.70%|-
|4|05/04/23|4061.22|-0.72%|-
|5|05/05/23|4136.25|1.85%|-
|6|05/08/23|4138.12|0.05%|-
|7|05/09/23|4119.17|-0.46%|-
|8|05/10/23|4137.64|0.45%|-
|9|05/11/23|4130.62|-0.17%|-
|10|05/12/23|4124.08|-0.16%|-
|11|05/15/23|4136.28|0.30%|-
|12|05/16/23|4109.9|-0.64%|-
|13|05/17/23|4158.77|1.19%|-
|14|05/18/23|4198.05|0.94%|-
|15|05/19/23|4191.98|-0.14%|-
|16|05/22/23|4192.63|0.02%|-
|17|05/23/23|4145.58|-1.12%|-
|18|05/24/23|4115.24|-0.73%|-
|19|05/25/23|4151.28|0.88%|-
|20|05/26/23|4205.45|1.30%|-
|21|05/30/23|4205.52|0.00%|-
|22|05/31/23|4179.83|-0.61%|-
|23|06/01/23|4221.02|0.99%|-
|24|06/02/23|4282.37|1.45%|-
|25|-|Daily StDev|0.84%|=stdev(B2:B24)
|26|-|Annualized StDev|13.29%|=sqrt(252)*C25

Thus, based on the data in the table, the annualized volatility is 13.29%. The higher the standard deviation, the riskier analysts consider the investment to be.

Additionally, you can find the standard deviation of an investment on popular investment websites. For example, Morningstar displays the three-year, five-year, and ten-year standard deviations for the S&P 500. [2]

## What is the Empirical Rule?

In statistics, the Empirical Rule states that in a normal distribution, 99.7% of observations will fall within three standard deviations (±3σ) of the mean. Specifically, 68% of observations will fall within one standard deviation, 95% within two standard deviations, and 97.5% within three standard deviations.

## How to Use the Empirical Rule?

The empirical rule is applied to predict possible outcomes in a normal distribution. For example, statisticians can use it to estimate the percentage of cases within each standard deviation range. Suppose the standard deviation is 3.1 and the mean is 10. In this case, the first standard deviation range will be between (10+3.2)=13.2 and (10-3.2)=6.8. The second standard deviation will be between 10 + (2 × 3.2)=16.4 and 10 - (2 × 3.2)=3.6, and so on.

## What are the benefits of rules of thumb?

The benefit of rules of thumb is that they can serve as a means of predicting data. This is particularly important when dealing with large datasets and data with unknown variables.

## Summary

Analysts use rules of thumb to observe how much data falls within specific intervals from the mean in a dataset. Investment analysts can use this to estimate the volatility of specific investments, portfolios, or funds.

## References

[1] Google Docs Editors Help. "[STDEV](https://support.google.com/docs/answer/3094054?hl=en)."

[2] Morningstar. "[S&P 500 PR](https://www.morningstar.com/indexes/spi/spx/risk)."