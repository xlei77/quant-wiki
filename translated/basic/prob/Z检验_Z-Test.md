---
{}
---

## What is a Z-test?

A Z-test is a statistical test used to determine whether there is a difference between two population means when the variance is known and the sample size is large. It can also be used to compare a single mean against a hypothesized value.

The data must approximately follow a normal distribution, otherwise the test is invalid. To perform a Z-test, parameters such as variance and standard deviation need to be calculated.

### Key Points

- Z-test is a statistical test used to determine whether there are differences between two population means when the variance is known and sample size is large, or to compare one mean against a hypothesized value.
- Z-test is a hypothesis test conducted on data that follows a normal distribution.
- The Z-statistic or Z-score is a number that represents the result of a Z-test.
- Z-test is closely related to t-test, but it's better to perform a t-test when the experiment has a small sample size.
- Z-test assumes that the standard deviation is known, while t-test assumes the standard deviation is unknown.

## Understanding the Z-Test

The Z-test is also a form of hypothesis testing where the Z-statistic follows a normal distribution. Z-tests are most suitable for samples larger than 30, as according to the Central Limit Theorem, the sample is considered to approximately follow a normal distribution as the sample size increases.

When conducting a Z-test, one should specify the null hypothesis, alternative hypothesis, and significance level (alpha level). The Z-score (also known as the test statistic) should be calculated, and results and conclusions should be stated. The Z-statistic or Z-score is a number that represents how many standard deviations away from the population mean a score derived from the Z-test is.

Examples of tests that can be conducted as Z-tests include single-sample location tests, two-sample location tests, paired difference tests, and maximum likelihood estimates. Z-tests are closely related to t-tests, but t-tests are better to perform when the sample size of the experiment is small. Additionally, t-tests assume the standard deviation is unknown, while Z-tests assume the standard deviation is known. If the population standard deviation is unknown, the sample variance is assumed to equal the population variance.

## Single Sample Z-Test Example

Suppose an investor wants to test whether the average daily return rate of a stock is greater than 3%. A simple random sample of 50 returns was calculated, with a mean of 2%. Assume the standard deviation of returns is 2.5%. Therefore, the null hypothesis is that the mean equals 3%.

Conversely, the alternative hypothesis is that the average return rate is either greater than or less than 3%. Assume an alpha value of 0.05% is chosen for a two-tailed test. Thus, each tail has 0.025% of the sample, and the critical values for alpha are 1.96 or -1.96. If the z-value is greater than 1.96 or less than -1.96, the null hypothesis is rejected.

The z-value is calculated by subtracting the observed sample mean from the mean daily return value chosen for testing (3% in this case). Next, divide the resulting value by the standard deviation divided by the square root of the number of observations.

Therefore, the test statistic is:

The investor rejects the null hypothesis because z is less than -1.96 and concludes that the average daily return rate is less than 3%.

## What's the difference between T-test and Z-test?

The Z-test is closely related to the t-test, but when working with small sample sizes (i.e., less than 30), it's better to perform a t-test. Additionally, the t-test assumes that the standard deviation is unknown, while the Z-test assumes that the standard deviation is known.

## When Should You Use a Z-Test?

A Z-test can be used when the population standard deviation is known and the sample size is greater than or equal to 30. If the population standard deviation is unknown, regardless of sample size, a t-test should be used instead.

## What is a Z-Score?

A Z-score or Z-statistic is a number that represents how many standard deviations a score from a Z-test differs from the population mean. Essentially, it is a numerical measurement that describes the relationship between a value and the mean of a set of values. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. A Z-score of 1.0 indicates that the value differs from the mean by one standard deviation. Z-scores can be either positive or negative, with positive values indicating scores above the mean and negative values indicating scores below the mean.

## What is the Central Limit Theorem (CLT)?

In probability theory, the Central Limit Theorem (CLT) states that as the sample size increases, the distribution of samples approximates a normal distribution (also known as the "bell curve"), assuming all samples are of equal size and regardless of the shape of the population distribution. A sample size equal to or greater than 30 is considered sufficient for the CLT to accurately predict population characteristics. The accuracy of Z-tests relies on the validity of the CLT.

## Conclusion

The Z-test is used for hypothesis testing to evaluate whether findings or associations are statistically significant. Specifically, it tests whether two means are equal (null hypothesis). The Z-test can only be used when the population standard deviation is known and the sample size is 30 data points or larger. Otherwise, a t-test should be used.