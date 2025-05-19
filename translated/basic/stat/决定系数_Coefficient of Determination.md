---
{}
---

## What is the Coefficient of Determination?

The coefficient of determination is a statistical measure used to examine how variations in one variable can be explained by variations in another variable, particularly when predicting specific event outcomes. This coefficient is more commonly known as r-squared (or r²). It evaluates the strength of the linear relationship between two variables and is widely relied upon by investors when conducting trend analysis.

This coefficient typically answers a key question: if a stock is listed in an index and experiences price fluctuations, what percentage of its price movements is caused by price movements in that index?

### Key Points

- The coefficient of determination is a complex concept surrounding data statistical analysis and financial models.
- It is used to explain the relationship between independent and dependent variables.
- The coefficient of determination is commonly known as r-squared (or r²), representing its statistical value.
- This measurement ranges between 0.0 and 1.0, where 1.0 indicates perfect correlation, which is a reliable model for future predictions.
- A value of 0.0 indicates that asset prices do not depend on index movements.

## Understanding the Coefficient of Determination

The coefficient of determination is a measure that explains how much of the variability in one factor is caused by its relationship with another factor. This correlation is expressed as a value between 0.0 to 1.0 or 0% to 100%.

A value of 1.0 indicates a 100% price correlation, representing a reliable model for future predictions. A value of 0.0 suggests that the model shows prices are independent of the index.[1]

A value of 0.20 indicates that 20% of the asset price movements can be explained by the index; a value of 0.50 indicates that 50% of price movements can be explained.

**Important Note:** The coefficient of determination is the square of the correlation coefficient, which is typically denoted as "r" in statistics. The value "r" can be negative, but r² cannot be negative because r-squared is the result of "r" multiplied by itself, and the square of a negative number is always positive.[2]

## Calculating the Coefficient of Determination

The coefficient of determination is calculated by creating a scatter plot and trend line of the data.

If you were to plot the closing prices of the S&P 500 and Apple (AAPL) stock for trading days from December 21 to January 20, you would collect prices as shown in the following table.[3]4

||S&P Daily Close|AAPL Daily Close
|---|---|---|
|January 20|$3,972.61|$137.87
|19|$3,898.85|$135.27
|18|$3,928.86|$135.21
|17|$3,990.97|$135.94
|13|$3,999.09|$134.76
|12|$3,983.17|$133.41
|11|$3,969.61|$133.49
|10|$3,919.25|$130.73
|9|$3,892.09|$130.15
|6|$3,895.08|$129.62
|5|$3,898.85|$0125.02
|4|$3,898.85|$1126.36
|3|$3,898.85|$2125.07
|December 30|$3,898.85|$3139.93
|29|$3,898.85|$4129.61
|28|$3,898.85|$5126.04
|27|$3,898.85|$6130.03
|23|$3,898.85|$7131.86
|22|$3,898.85|$8132.23
|21|$3,898.85|$9135.45

Next, you will create a scatter plot. The degree to which the data fits the regression model is called goodness of fit, which measures the distance between the trend line and all data points scattered in the graph.

Most spreadsheets use the same formula to calculate r² for a dataset. If your data is in columns A and B of your spreadsheet:

Using this formula and highlighting the corresponding cells gives an r² of 0.347 for S&P 500 and Apple prices, indicating a low correlation between the two, whereas an r² between 0.5 and 1.0 would indicate a higher correlation.

Manually calculating the coefficient of determination involves several steps. First, collect the data from the above table, then calculate all required values as shown in the following table:[4]

- x = S&P 500 Daily Close
- y = AAPL Daily Close

||x|x²|y|y²|xy
|---|---|---|---|---|---|
|January 20|$3,972.61|$15,781,630.21|$3,928.86|$119,008.14|$547,703.74
|19|$3,898.85|$15,201,031.32|$135.27|$3,928.86|$4527,397.44
|18|$3,928.86|$15,435,940.90|$3,928.86|$618,281.74|$531,221.16
|17|$3,990.97|$15,927,841.54|$135.94|$3,928.86|$9542,532.46
|13|$3,999.09|$15,992,720.83|$3,990.97|$118,160.26|$538,917.37
|12|$3,983.17|$15,865,643.25|$133.41|$3,990.97|$4531,394.71
|11|$3,969.61|$15,757,803.55|$3,990.97|$617,819.58|$529,903.24
|10|$3,919.25|$15,360,520.56|$130.73|$3,990.97|$9512,363.55
|9|$3,892.09|$15,148,364.57|$3,999.09|$116,939.02|$506,555.51
|6|$3,895.08|$15,171,648.21|$129.62|$3,999.09|$4504,880.27
|5|$3,898.85|$014,501,625.61|$3,999.09|$615,630.00|$476,088.66
|4|$3,898.85|$114,845,377.82|$126.36|$3,999.09|$9486,861.29
|3|$3,898.85|$214,624,046.74|$3,983.17|$115,642.50|$478,285.19
|December 30|$3,898.85|$314,741,760.25|$139.93|$3,983.17|$4537,261.24
|29|$3,898.85|$414,816,956.52|$3,983.17|$616,798.75|$498,905.18
|28|$3,898.85|$514,312,753.57|$126.04|$3,983.17|$9476,837.05
|27|$3,898.85|$614,663,155.56|$3,969.61|$116,907.80|$497,917.38
|23|$3,898.85|$714,782,640.83|$131.86|$3,969.61|$4506,977.97
|22|$3,898.85|$814,610,665.31|$3,969.61|$617,484.77|$505,434.63
|21|$3,898.85|$915,042,296.83|$135.45|$3,969.61|$9525,334.70
|Sum (Σ)|$3,919.25|$0302,584,424.00|$3,919.25|$1348,307.23|$3,919.25|$2$3,919.25|$3$3,919.25|$4$3,919.25|$5$3,919.25|$6$3,919.25|$7$3,919.25|$8$3,919.25|$9$

As you can see, this can become very tedious and prone to errors when dealing with several weeks of trading data.

## Explaining the Coefficient of Determination

When you obtain the coefficient of determination, you can use it to evaluate the degree of correlation between the price movements of the asset you're assessing and those of an index or benchmark. In the example of Apple and the S&P 500, the coefficient of determination for this period is 0.347.

**Tip:** Since Apple is listed in many indices, you can calculate r² to determine whether it corresponds to price movements of other indices.

A coefficient of determination of 0.357 indicates that Apple's stock price movements have some correlation with the index, as 1.0 represents high correlation while 0.0 indicates no correlation.

One important point to note is that r-squared does not tell the analyst whether the coefficient of determination value is inherently good or bad. It is at the analyst's discretion to evaluate this correlation and its application in future trend analysis.

## How to Interpret the Coefficient of Determination?

The coefficient of determination shows the degree of correlation between a dependent variable and an independent variable. It is also known as r² or r-squared. The value should be between 0.0 and 1.0. The closer to 0.0, the weaker the correlation of the dependent variable; the closer to 1.0, the stronger the correlation. [1]

## What Does R-squared Tell You in Regression?

In regression, r-squared tells you whether there is a dependency relationship between two values, and the degree to which one value depends on another.

## What Happens if the Coefficient of Determination is Greater Than 1?

The coefficient of determination cannot be greater than 1, as the formula will always return a number between 0.0 and 1.0. If the value exceeds or falls below these numbers, it indicates an error. [1]

## Conclusion

The coefficient of determination is a ratio that demonstrates the degree of dependence of one variable on another. Investors use it to assess the correlation between asset price movements and their listed indices.

When an asset's r² is closer to zero, it indicates that its price movements are not dependent on the index. If its r² is closer to 1.0, it indicates that it is more dependent on the index's price movements.

## References

[1] Pennsylvania State University Eberly College of Science. "[STAT 462 Applied Regression Analysis: 2.5 - The Coefficient of Determination, r-squared](https://online.stat.psu.edu/stat462/node/95/)."

[2] LibreTexts Statistics. "[10.6: The Coefficient of Determination](https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_%28Shafer_and_Zhang%29/10%3A_Correlation_and_Regression/10.06%3A_The_Coefficient_of_Determination)."

[3] Nasdaq. "[APPL Historical Data](https://www.nasdaq.com/market-activity/stocks/aapl/historical)."

[4] Nasdaq. "[SPX Historical Data](https://www.nasdaq.com/market-activity/index/spx/historical)."