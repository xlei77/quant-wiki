---
{}
---

## What is P-value?

In statistics, a p-value is defined as a number that represents the probability of obtaining a test statistic equal to or more extreme than the actual observed value, assuming the null hypothesis is true.

P-values can serve as an alternative to rejection regions, providing the minimum significance level at which the null hypothesis can be rejected. The smaller the p-value, the stronger the support for the alternative hypothesis.

Government agencies frequently use p-values to enhance the credibility of research or reports. For example, the U.S. Census Bureau stipulates that any analysis with a p-value greater than 0.10 must be accompanied by a statement indicating that the difference is not statistically different from zero. The Census Bureau has also established standards specifying which p-values are acceptable for various publications.[1]

### Key Points

- P-value is a statistical measurement method used to validate hypotheses based on observed data.
- P-value measures the probability of obtaining the observed results, assuming the null hypothesis is true.
- The lower the p-value, the greater the statistical significance of the observed difference.
- A p-value less than or equal to 0.05 is generally considered statistically significant.
- P-values can serve as an alternative or complement to pre-selected confidence levels in hypothesis testing.

## Understanding P-values

P-values are typically found using p-value tables or electronic spreadsheets/statistical software. These calculations are based on the assumed or known probability distribution of the specific test statistic being measured. Sample size determines the reliability of observed data and directly affects the accuracy of p-value calculations. The p-value method for hypothesis testing uses calculated P-values derived from the deviation between the observed value and selected reference value, taking into account the probability distribution of the statistic - the greater the difference between the two values, the smaller the corresponding p-value.

Mathematically, p-values are calculated using integral calculus, computing the area under the probability distribution curve for all values of the test statistic that are at least as far from the reference value as the observed value is, relative to the total area under the probability distribution curve. Standard deviation, which quantifies the dispersion of data points from the mean, plays an important role in these calculations.

The calculation of p-values varies depending on the type of test performed. Three types of tests describe the location on the probability distribution curve: left-tailed test, right-tailed test, or two-tailed test. In each case, degrees of freedom play a crucial role in determining the shape of the distribution and the calculation of p-values.

In simple terms, the greater the difference between two observed values, the less likely that difference is due to simple random chance, which is reflected in a lower p-value.

## P-Value Method for Hypothesis Testing

The P-value method for hypothesis testing uses calculated probabilities to determine whether there is evidence to reject the null hypothesis. This determination largely depends on the test statistic, which summarizes the hypothesis-relevant information from the sample. The null hypothesis, also called the conjecture, is the initial statement about the population (or data generation process). The alternative hypothesis specifies whether the population parameter differs from the value stated in the conjecture.

In practice, significance levels are declared in advance to determine how small the p-value must be to reject the null hypothesis. Since different researchers may use different significance levels when examining a problem, readers might sometimes find it difficult to compare results from two different tests. P-values provide a solution to this issue.

**Important Note:** Even a low p-value does not necessarily prove statistical significance, as there remains a possibility that the observed data is a chance result. Only repeated experiments or studies can confirm whether a relationship is statistically significant.

For example, suppose a study comparing returns between two specific assets is conducted by different researchers using the same data but different significance levels. Researchers might reach opposite conclusions about whether differences exist between the assets.

If one researcher uses a 90% confidence level while another researcher requires a 95% confidence level to reject the null hypothesis, and if the p-value for the observed difference between the two returns is 0.08 (corresponding to a 92% confidence level), then the first researcher would find a statistically significant difference between the two assets, while the second researcher would find no statistically significant difference between the returns.

To avoid this issue, researchers can report the p-value of the hypothesis test and allow readers to interpret statistical significance themselves. This is known as the p-value approach to hypothesis testing. Independent observers can note the p-value and decide for themselves whether this represents a statistically significant difference.

## Examples of P-Value

An investor claims that their portfolio performs equivalently to the Standard & Poor's (S&P) 500 index. To verify this, the investor conducts a two-tailed test.

The null hypothesis states that the portfolio's return rate is equivalent to the S&P 500 index's return rate during the specified period, while the alternative hypothesis states that the portfolio's return rate is not equivalent to the S&P 500 index's return rate—if the investor conducts a one-tailed test, the alternative hypothesis would state that the portfolio's return rate is either less than or greater than the S&P 500 index's return rate.

P-value hypothesis testing doesn't necessarily use a pre-selected confidence level at which the investor should reset the null hypothesis of equivalent returns. Instead, it provides a way to measure how much evidence exists to reject the null hypothesis. The smaller the p-value, the more evidence there is against the null hypothesis.

Therefore, if the investor finds a p-value of 0.001, there is strong evidence against the null hypothesis, and the investor can confidently conclude that the portfolio's return rate is not equivalent to the S&P 500 index's return rate.

While this doesn't provide an exact threshold for when an investor should accept or reject the null hypothesis, it does have another very practical advantage. P-value hypothesis testing provides a direct way to compare the relative confidence an investor can have when choosing between different types of investments or portfolios relative to benchmarks such as the S&P 500 index.

For example, for two portfolios A and B that perform differently from the S&P 500 index with p-values of 0.10 and 0.01 respectively, the investor can be more confident that Portfolio B, with the lower p-value, will actually show consistently different results.

## Is a P-value of 0.05 Significant?

A p-value less than 0.05 is generally considered statistically significant, in which case the null hypothesis should be rejected. A p-value greater than 0.05 indicates that the deviation from the null hypothesis is not statistically significant, and the null hypothesis is not rejected.

## What Does a P-value of 0.001 Mean?

A p-value of 0.001 indicates that if the null hypothesis being tested is indeed true, the probability of observing results at least as extreme as the actual results is one in a thousand. This leads the observer to reject the null hypothesis, because either a highly rare data outcome has been observed, or the null hypothesis is incorrect.

## How to Compare Two Different Hypothesis Test Results Using P-values?

If you have two different results, one with a p-value of 0.04 and another with a p-value of 0.06, the result with the p-value of 0.04 would be considered statistically more significant than the result with the p-value of 0.06. Beyond this simplified example, you can compare a p-value of 0.04 with a p-value of 0.001. Both are statistically significant, but the example with 0.001 provides stronger evidence against the null hypothesis than the example with 0.04.

## Bottom Line

The p-value is used to measure the significance of observed data. When researchers discover an apparent relationship between two variables, there is always a possibility that this correlation could be coincidental. P-value calculations help determine whether the observed relationship might have occurred by chance.

## References

[1] U.S. Census Bureau. "[Statistical Quality Standard E1: Analyzing Data](https://www.census.gov/about/policies/quality/standards/standarde1.html)."