---
{}
---

## What is a T-test?

A T-test is a type of inferential statistics used to determine whether there is a significant difference between the means of two groups and their relationship. T-tests can be used when a dataset follows a normal distribution and the variance is unknown, such as in a dataset recording 100 coin tosses.

A T-test is a method used for statistical hypothesis testing that determines statistical significance using t-statistics, t-distribution values, and degrees of freedom.

### Key Points

- T-test is a type of inferential statistics used to determine whether there is a statistically significant difference between the means of two variables.
- T-test is a type of statistical hypothesis testing.
- Calculating a T-test requires three basic data values, including the difference between the means of each dataset, the standard deviation of each group, and the number of data values in each group.
- T-tests can be related (dependent) or independent.

## Understanding T-test

The T-test compares the means of two datasets and determines whether they come from the same population. In the above examples, student samples from Class A and Class B are unlikely to have identical means and standard deviations. Similarly, samples drawn from a control group taking placebos and a group taking prescription medications should have slightly different means and standard deviations.

Mathematically, the T-test takes a sample from each of the two datasets and establishes a problem statement. It assumes a null hypothesis that the two means are equal.

The value is calculated using a formula and compared against standard values. Based on the results, the null hypothesis is either accepted or rejected. If the null hypothesis is rejected, it indicates that the data readings are strong and unlikely to be due to chance.

The T-test is just one of many tests used for this purpose. Statisticians use other tests beyond the T-test to study more variables and larger sample sizes. For large sample sizes, statisticians use the z-test. Other testing options include chi-square tests and F-tests.

## Using T-Test

Suppose a pharmaceutical company is testing a new drug. Following standard procedure, the drug is administered to one group of patients, while another group, called the control group, receives a placebo. A placebo is a substance with no therapeutic effect, serving as a baseline to measure the response of patients taking the actual drug.

After the drug trial, members of the control group who took the placebo reported an average increase in life expectancy of three years, while the group taking the new drug reported an average increase in life expectancy of four years.

Initial observations suggest the drug is effective. However, this observation could also be coincidental. A T-test can be used to determine whether the results are valid and applicable to the entire population.

When using a T-test, there are four assumptions. The collected data must follow a continuous or ordinal scale, such as IQ test scores; the data is collected from randomly selected portions of the population; the data will result in a normal distribution bell curve; and there is equal or homogeneous variance with equal standard deviations.

## T-Test Formulas

Three basic data values are needed to calculate a T-test. These include the difference between the means of each dataset (mean difference), the standard deviation of each group, and the number of data values in each group.

This comparison helps determine if differences are due to chance and whether they exceed the range of coincidence. The T-test questions whether differences between two groups represent real differences in the study or are merely random variations.

The T-test output produces two values: the t-value and degrees of freedom. The t-value, or t-score, is the ratio between the difference in means of two sample sets and the variation that exists within the sample sets.

The numerator is the difference between the means of two sample sets. The denominator is the variation that exists within the sample sets, measuring dispersion or variability.

The calculated t-value is then compared with values obtained from a critical value table called the T-distribution table. Higher t-scores indicate greater differences between two sample sets. Lower t-values indicate greater similarity between two sample sets.

**T-score**: Larger t-scores or t-values indicate differences between groups, while smaller t-scores indicate similarity between groups.

Degrees of freedom refers to values that can vary in the study and are crucial for evaluating the significance and validity of the null hypothesis. The calculation of these values typically depends on the number of data records available in the sample sets.

Related T-tests or paired T-tests are dependency-type tests appropriate when samples consist of matched similar units or when there are repeated measurements. For example, there might be multiple tests of the same patient before and after receiving a treatment. Each patient serves as their own control sample.

This method is also suitable for cases where samples are related or have matching characteristics, such as comparative analyses involving children, parents, or siblings.

The formulas for calculating the t-value and degrees of freedom for paired T-tests are:

$$ \begin{aligned}&T=\frac{\textit{mean}1 - \textit{mean}2}{\frac{s(\text{diff})}{\sqrt{(n)}}}\\&\textbf{其中：}\\&\textit{mean}1\text{和}\textit{mean}2=\text{每个样本集的平均值}\\&s(\text{diff})=\text{配对数据值差异的标准差}\\&n=\text{样本大小（配对差异的数量）}\\&n-1=\text{自由度}\end{aligned} $$

Equal variance T-test is an independent T-test used when sample sizes for each group are the same or when the variances of two datasets are similar.

The formulas for calculating the t-value and degrees of freedom for equal variance T-tests are:

$$ \begin{aligned}&\text{T值}=\frac{\textit{mean}1-\textit{mean}2}{\sqrt{\frac{(n1-1)\times\textit{var}1^2+(n2-1)\times\textit{var}2^2}{n1+n2-2}\times\frac{1}{n1}+\frac{1}{n2}}}\\&\textbf{其中：}\\&\textit{mean}1\text{和}\textit{mean}2=\text{每个样本集的平均值}\\&\textit{var}1\text{和}\textit{var}2=\text{每个样本集的方差}\\&n1\text{和}n2=\text{每个样本集中的记录数量}\end{aligned} $$

and,

$$ \begin{aligned} &\text{自由度} = n1 + n2 - 2 \\ &\textbf{其中：}\\ &n1\text{和}n2 = \text{每个样本集中的记录数量} \\ \end{aligned} $$

Unequal variance T-test is an independent T-test used when sample sizes for each group are different and the variances of two datasets are also different. This test is also known as Welch's t-test.

The formulas for calculating the t-value and degrees of freedom for unequal variance T-tests are:

$$ \begin{aligned}&\text{T值}=\frac{mean1-mean2}{\sqrt{\bigg(\frac{var1}{n1}{+\frac{var2}{n2}\bigg)}}}\\&\textbf{其中：}\\&mean1\text{和}mean2=\text{每个样本集的平均值} \\&var1\text{和}var2=\text{每个样本集的方差} \\&n1\text{和}n2=\text{每个样本集的记录数量} \end{aligned} $$

and,

$$ \begin{aligned} &\text{自由度} = \frac{ \left ( \frac{ var1^2 }{ n1 } + \frac{ var2^2 }{ n2 } \right )^2 }{ \frac{ \left ( \frac{ var1^2 }{ n1 } \right )^2 }{ n1 - 1 } + \frac{ \left ( \frac{ var2^2 }{ n2 } \right )^2 }{ n2 - 1}} \\ &\textbf{其中：}\\ &var1\text{和}var2=\text{每个样本集的方差} \\ &n1\text{和}n2=\text{每个样本集的记录数量} \\ \end{aligned} $$

## How to Choose a T-test?

The following flowchart can be used to determine which type of T-test to use based on the characteristics of sample sets. Key considerations include the similarity of sample records, the number of data records in each sample set, and the variance of each sample set.

## Example of Unequal Variance T-test

Suppose an art gallery measures the diagonals of received paintings. One sample group includes 10 paintings, while another includes 20 paintings. The datasets and their corresponding means and variances are as follows:

||Sample 1|Sample 2
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
|||18.0
|||23.9
|||21.6
|||24.3
|||20.4
|||23.9
|||13.3
|Mean|19.4|21.6
|Variance|1.4|17.1

Although Sample 2 has a higher mean than Sample 1, we cannot conclude that the population mean corresponding to Sample 2 is higher than that of Sample 1.

Is the difference from 19.4 to 21.6 purely coincidental, or is there a real difference between the populations of all received paintings? We establish the question by assuming a null hypothesis that the means of the two sample sets are equal, and conduct a T-test to examine the validity of this hypothesis.

Since the number of data records differs (n1 = 10 and n2 = 20) and the variances are different, calculate the t-value and degrees of freedom for the above datasets using the formula mentioned in the unequal variance T-test section.

The calculated t-value is -2.24787. Since the negative sign can be ignored when comparing two t-values, the calculation value is 2.24787.

The degrees of freedom value is 24.38, which is rounded down to the nearest integer according to the formula definition, resulting in 24.

A probability level (significance level α, p-value) can be specified as an acceptance criterion. In most cases, a value of 5% can be assumed.

Using the degrees of freedom value of 24 and a 5% significance level, consulting the t-value distribution table yields a value of 2.064. Comparing this with the calculated value of 2.247 shows that the calculated t-value is greater than the table value at the 5% significance level. Therefore, we can safely reject the null hypothesis that there is no difference between the means. There is an inherent difference between the population sets, and these differences are not coincidental.

## How to Use the T-Distribution Table?

The T-distribution table comes in both one-tailed and two-tailed formats. The one-tailed format is used to evaluate situations with fixed values or ranges where the direction is clear, whether positive or negative. For example, what is the probability of an output value being less than -3, or what is the probability of rolling a sum greater than 7 with a pair of dice? The two-tailed format is used for interval analysis, such as checking whether a coordinate falls between -2 and +2.

## What is an Independent T-test?

An independent T-test uses samples that are selected independently of each other, where the two groups of datasets do not point to the same values. For example, it could include 100 randomly unrelated patients divided into two groups of 50 patients each. One group serves as a control group taking a placebo, while the other group receives prescribed treatment. This constitutes two independent and unordered sample groups.

## What does a T-test explain and how is it used?

A T-test is a statistical test typically used to compare the means of two groups. It is frequently used in hypothesis testing to determine whether a process or treatment has an effect on the population of interest, or whether there is a difference between two groups.

## References

No references cited.