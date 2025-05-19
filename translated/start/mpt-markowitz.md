---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# The Pioneer of Quantitative Analysis: Understanding Modern Portfolio Theory and the Markowitz Model

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

In the world of investment and financial management, there's a commonly quoted phrase—"There's no such thing as a free lunch." In other words, all returns come with hidden risks, which is an undeniable fact for anyone looking to participate in the financial markets. This raises the question: How do we quantify this relationship between risk and return? And is there a method that allows us to achieve better returns for our investment portfolio without taking on excessive risk? Today, I'd like to discuss **Modern Portfolio Theory (MPT)** and the **Markowitz Model** proposed by Harry Markowitz.

Perhaps before reading this article, you were already familiar with concepts like "risk management" or "asset allocation," but if you delve deeper into MPT, you might completely change your perspective on risk and even incorporate these principles into your daily decision-making.

## Birth of MPT: Risk, Return, and Nobel Glory

In the 1950s, Harry Markowitz first proposed the core ideas of MPT. He believed that for any asset, there exists a trade-off relationship between risk and reward. If we measure risk using the magnitude of price fluctuations (i.e., volatility), then assets with less stable prices carry higher risks and relatively greater return potential; while more stable assets, though lower in risk, have relatively lower return ceilings.

![](https://fastly.jsdelivr.net/gh/bucketio/img4@main/2024/12/14/1734215702884-60a6995b-8829-4cc9-8cf9-0c834f77053b.png)

In this theoretical framework, risk and return are no longer vague concepts but rather objects that can be described and optimized mathematically. Markowitz himself was awarded the **Nobel Prize in Economics** for this work, which was both a recognition of his personal intellect and an acknowledgment of MPT's standing in the field of finance.

## Correlation and Covariance Matrix: Understanding Asset Interactions

The brilliance of MPT lies in the fact that it focuses not only on the risk and return of individual assets but also emphasizes the interactive relationships between different assets. In real markets, some assets may rise or fall together (positive correlation), some may move in opposite directions (negative correlation), while others may have little to no correlation.

These interactions between assets can be measured using covariance. When we organize the covariance values of various assets into a matrix, we get the famous covariance matrix, denoted by the symbol $$\Sigma$$ (Sigma). This $$\Sigma$$ serves as a panoramic view of the investment portfolio, showing the volatility relationships between all assets. It is through understanding these covariance values that we can better appreciate the importance of selecting assets with relatively low correlation to each other.

## Efficient Frontier: The Key to Finding the Ideal Portfolio

Even when we understand risk and correlation, a challenging question remains: how do we allocate appropriate investment proportions for each asset? After all, theoretically, there are infinite possible portfolio weight combinations. However, Markowitz pointed out that among these countless possibilities, only one specific curve—the "Efficient Frontier"—represents the optimal risk-return combinations.

**The Efficient Frontier** refers to: all portfolio points that achieve the highest expected return for a given level of risk, or achieve the minimum risk for a given return requirement. This means that if your portfolio lies on this frontier, you cannot find a better allocation strategy under the same conditions.

## Mathematical Foundations: From Matrices to Optimal Solutions

Let's delve a bit into the mathematical aspects, but don't worry about being intimidated by formulas - understanding the principles is what matters.

1. Use a weight vector $$w$$ to represent the proportion of each asset in the portfolio.
2. The covariance matrix is $$\Sigma$$.
3. The portfolio variance (i.e., the quantitative measure of risk) can be calculated through $$w^T \Sigma w$$, where $$w^T$$ is the transpose of $$w$$. The square root of variance is the portfolio volatility.
4. If we have an expected return vector $$\mu$$, then the portfolio's expected return $$R$$ is $$\mu^T w$$.

Our objective is: to achieve the highest possible return (maximize $$\mu^T w$$) at the lowest possible risk (minimize $$w^T \Sigma w$$). In mathematical solving, since the objectives are "dual" and mutually constraining, we will obtain a curve solution (the efficient frontier) rather than a single point solution.

The final weight formula can be written as:

$$\Sigma$$2

Here, $$\Sigma$$3 is the investor's risk tolerance parameter, which can range from 0 (extremely conservative) to infinity (extremely adventurous). By changing $$\Sigma$$3, we can select different points along the efficient frontier.

## The Power of Diversification: Why Not Go All-in on Bitcoin or Coca-Cola?

What would be the problem if you invested all your money in a single asset, such as only buying Bitcoin or only buying Coca-Cola stock? Bitcoin's extreme volatility could put you on a "roller coaster" in the short term, while investing solely in Coca-Cola, though stable, limits your potential for higher growth. MPT (Modern Portfolio Theory) tells us: there's no need for extremes - you can diversify risk by holding multiple assets with low correlation and positive expected returns, finding a better solution between overall risk and return.

This thinking applies equally to emerging assets, such as cryptocurrencies. If you want to allocate some investment to Bitcoin but don't want to bet everything on it, portfolio allocation guided by MPT might provide you with direction.

![Harry Markowitz](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2024/12/14/1734215736417-d72c0d15-f926-4249-a867-91bc37e7e91f.png)

## Estimating Expected Returns and the CAPM Model

In the above discussion, the expected return rate $$\mu$$ appears to be known, but in reality, estimating it is quite challenging. You need to determine the expected returns of various assets based on your experience, research, and models.

Many investors refer to the Capital Asset Pricing Model (CAPM) to help them price assets. The CAPM formula is as follows:

$$\Sigma$$6

Where:

- $$\Sigma$$7: Risk-free rate (typically represented by government bond yields, data available from official sources)
- $$\Sigma$$8: Expected market return rate, which can be estimated using historical data or model predictions
- $$\Sigma$$9: An indicator measuring an asset's sensitivity to market volatility, defined as the covariance between the asset and benchmark divided by the benchmark's variance

Using CAPM, you can obtain a relatively "reasonable" expected return for individual assets, which can then be used as elements in $$\mu$$, thus paving the way for portfolio optimization.

## Summary and Action Recommendations

By this point, you may have realized that MPT is not a magical cure-all solution, but rather a tool to make our investment decisions more rational and data-driven. It allows us to weigh risk and reward in a quantifiable way and find optimal allocations through mathematical methods. Of course, no model can guarantee profits without losses, but MPT provides us with a framework to understand what risks we are taking for our expected returns.

**Note: The content of this article does not constitute investment advice. Investment always involves uncertainty, and past performance does not guarantee future results.**