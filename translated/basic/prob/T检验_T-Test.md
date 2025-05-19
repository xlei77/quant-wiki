---
{}
---

## What is a T-test?

A T-test is an inferential statistical method used to determine whether there is a significant difference between the means of two groups of data and their relationship. T-tests are used when datasets follow a normal distribution and have unknown variance, such as data recorded from flipping a coin 100 times.

A T-test is a type of hypothesis test in statistics that uses t-statistics, t-distribution values, and degrees of freedom to determine statistical significance.

### Key Points

- T-test is an inferential statistical method used to determine whether there is a statistically significant difference between the means of two variables.
- T-test is a type of hypothesis testing used in statistics.
- Calculating a T-test requires three basic data values, including the difference between the means of each dataset, the standard deviation of each group, and the number of data values.
- T-tests can be either paired or independent.

## Understanding T-Tests

T-tests compare the means of two datasets and determine whether they come from the same population. In the example above, student samples from Class A and Class B are unlikely to have identical means and standard deviations. Similarly, samples drawn from a control group taking placebos and a group taking prescription medication should have slightly different means and standard deviations.

Mathematically, a T-test draws a sample from each of the two sets and establishes a problem statement. It assumes a null hypothesis that the two means are equal.

Using formulas, the value is calculated and compared against standard values. The null hypothesis is accordingly accepted or rejected. If the null hypothesis meets the conditions for rejection, it indicates that the data readings are strong and unlikely to be due to chance.

The T-test is just one of many tests used for this purpose. Statisticians use tests other than T-tests to examine more variables and larger sample sizes. For larger sample sizes, statisticians use z-tests. Other testing options include chi-square tests and f-tests.

## Using T-Test

Suppose a pharmaceutical company is testing a new drug. Following standard procedure, the drug is given to one group of patients, while a placebo is given to another group, called the control group. A placebo is a substance with no therapeutic value that serves as a baseline for measuring the response of the other group (taking the actual drug).

After the drug trial, members of the control group taking the placebo reported an average increase in life expectancy of three years, while members of the group taking the new drug reported an average increase in life expectancy of four years.

Initial observations suggest that the drug is working. However, these observations could also be due to chance. A T-test can be used to determine if the results are valid and applicable to the entire population.

Four assumptions are made when using a T-test. The collected data must follow a continuous or ordinal scale, such as IQ test scores; the data is collected from a randomly selected portion of the total population; the data will result in a bell-shaped normal distribution; and there is equal or homogeneous variance when standard deviations are equal.

## T-Test Formulas

Three basic data values are needed to calculate a T-test. These include the difference between the means of each dataset (i.e., mean difference), the standard deviation for each group, and the number of data values in each group.

This comparison helps determine how chance affects the differences and whether the differences exceed that range of chance. The T-test questions whether the differences between groups represent real differences in the study or are merely random differences.

The T-test produces two values as its output: t-value and degrees of freedom. The t-value, or t-score, is the ratio between the difference of means of two sample sets and the variation that exists within the sample sets.

The numerator value is the difference between the means of two sample sets. The denominator is the variation present in the sample sets, which is a measure of dispersion or variability.

The calculated t-value is then compared with values obtained from a critical value table called the T-distribution table. Higher t-scores indicate greater differences between two sample sets. Lower t-values indicate greater similarities between two sample sets.

**T-Score:** Larger t-scores (or t-values) indicate differences between groups, while smaller t-scores indicate similarities between groups.

Degrees of freedom refers to values that are free to vary in the study and are crucial for evaluating the significance and validity of the null hypothesis. These values are typically calculated based on the number of data records available in the sample sets.

Related t-test or paired t-test is a dependent test performed when samples consist of matched pairs of similar units or when there are repeated measurements. For example, there might be cases where the same patient is tested repeatedly before and after receiving a specific treatment. Each patient serves as their own control sample.

This method is also applicable in situations where samples are related or have matching characteristics, such as comparative analyses involving children, parents, or siblings.

The formulas for calculating the t-value and degrees of freedom for paired t-test are:

$$ \begin{aligned}&T=\frac{\textit{mean}1 - \textit{mean}2}{\frac{s(\text{diff})}{\sqrt{(n)}}}\\&\textbf{其中：}\\&\textit{mean}1\text{ 和 }\textit{mean}2=\text{每个样本集的平均值}\\&s(\text{diff})=\text{配对数据值的差异的标准差}\\&n=\text{样本大小（配对差异的数量）}\\&n-1=\text{自由度}\end{aligned} $$

Equal variance t-test is an independent t-test used when the sample sizes in each group are the same, or when the variances of the two datasets are similar.

The formulas for calculating the t-value and degrees of freedom for equal variance t-test are:

$$ \begin{aligned}&\text{T-value} = \frac{ mean1 - mean2 }{\frac {(n1 - 1) \times var1^2 + (n2 - 1) \times var2^2 }{ n1 +n2 - 2}\times \sqrt{ \frac{1}{n1} + \frac{1}{n2}} } \\&\textbf{其中：}\\&mean1 \text{ 和 } mean2 = \text{每个样本集的平均值} \\&var1 \text{ 和 } var2 = \text{每个样本集的方差} \\&n1 \text{ 和 } n2 = \text{每个样本集中的记录数} \end{aligned} $$

And,

$$ \begin{aligned} &\text{自由度} = n1 + n2 - 2 \\ &\textbf{其中：}\\ &n1 \text{ 和 } n2 = \text{每个样本集中的记录数} \\ \end{aligned} $$

Unequal variance t-test is an independent t-test used when sample sizes in each group are different and the variances of the two datasets are also different. This test is also known as Welch's t-test.

The formulas for calculating the t-value and degrees of freedom for unequal variance t-test are:

$$ \begin{aligned}&\text{T-value}=\frac{mean1-mean2}{\sqrt{\bigg(\frac{var1}{n1}{+\frac{var2}{n2}\bigg)}}}\\&\textbf{其中：}\\&mean1 \text{ 和 } mean2 = \text{每个样本集的平均值} \\&var1 \text{ 和 } var2 = \text{每个样本集的方差} \\&n1 \text{ 和 } n2 = \text{每个样本集中的记录数} \end{aligned} $$

And,

$$ \begin{aligned} &\text{自由度} = \frac{ \left ( \frac{ var1^2 }{ n1 } + \frac{ var2^2 }{ n2 } \right )^2 }{ \frac{ \left ( \frac{ var1^2 }{ n1 } \right )^2 }{ n1 - 1 } + \frac{ \left ( \frac{ var2^2 }{ n2 } \right )^2 }{ n2 - 1}} \\ &\textbf{其中：}\\ &var1 \text{ 和 } var2 = \text{每个样本集的方差} \\ &n1 \text{ 和 } n2 = \text{每个样本集中的记录数} \\ \end{aligned} $$

## Which T-Test to Use?

The following flowchart can be used to determine which T-test to use based on the characteristics of the sample sets. Key items to consider include the similarity of sample records, the number of data records in each sample set, and the variance of each sample set.

## Example of Unequal Variance T-Test

Suppose diagonal measurements are taken of paintings received at an art gallery. One group of samples includes 10 paintings, while another group includes 20 paintings. The datasets and their corresponding means and variances are as follows:

||Set 1|Set 2
|---|---|---|
||19.7|28.3
||20.4|26.7
||19.6|20.1
||17.8|23.3
||18.5|25.2
||18.9|22.1
||18.3|17.7
||18.9|27.6
||19.5|20.6
||21.95|13.7
|||23.2
|||17.5
|||20.6
|||18
|||23.9
|||21.6
|||24.3
|||20.4
|||23.9
|||13.3
|Mean|19.4|21.6
|Variance|1.4|17.1

Although Set 2 has a higher mean than Set 1, we cannot conclude that the population corresponding to Set 2 has a higher mean than the population corresponding to Set 1.

Is the difference from 19.4 to 21.6 merely due to chance, or is there a difference in the population of all paintings received by the art gallery? We frame the question by assuming a null hypothesis (that the means between the two sample sets are the same) and perform a T-test to test whether this hypothesis is reasonable.

Since the number of data records differs (n1 = 10 and n2 = 20), and the variances are also different, we use the formula mentioned in the unequal variance T-test section to calculate the t-value and degrees of freedom for the above datasets.

The t-value is -2.24787. Since the negative sign can be ignored when comparing two t-values, the calculated value is 2.24787.

The degrees of freedom value is 24.38, and since the formula definition requires rounding down to the smallest possible integer value, it is reduced to 24.

A probability level (alpha level, significance level, p) can be specified as the acceptance criterion. In most cases, a value of 5% can be assumed.

Using the degrees of freedom value of 24 and a 5% significance level, consulting the t-value distribution table yields a value of 2.064. Comparing this with the calculated value of 2.247 shows that the calculated t-value is greater than the table value at the 5% significance level. Therefore, it is safe to reject the null hypothesis that there is no difference between the means. The population sets have inherent differences, and it is not due to chance.

## How to Use the T-Distribution Table?

The T-distribution table comes in both one-tailed and two-tailed formats. The former is used to evaluate situations with fixed values or ranges that have a clear direction (positive or negative). For example, what is the probability that an output value stays below -3, or what is the probability of getting above 7 when rolling a pair of dice? The latter is used for range boundary analysis, such as asking whether coordinates fall between -2 and +2.

## What is an Independent T-test?

An independent T-test uses samples that are selected independently of each other, where the datasets in the two groups do not reference the same values. They might include 100 randomly unrelated patients divided into two groups of 50 patients each. One group becomes the control group and takes a placebo, while the other group receives the prescribed treatment. This constitutes two independent sample groups that are unpaired and unrelated to each other.

## What Does a T-Test Explain and How to Use Them?

A T-test is a statistical test used to compare the means of two groups. It is commonly used in hypothesis testing to determine whether a process or treatment has an effect on the population of interest, or whether two groups are different from each other.