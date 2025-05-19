---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# Do You Really Understand the Sharpe Ratio? A Quantitative Trader's Guide to the Sharpe Ratio

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Hello everyone, welcome to this educational article about the Sharpe Ratio. This article will help you understand more systematically and deeply the important role of the Sharpe Ratio in quantitative investment and portfolio management, and how professional **quantitative traders** view the Sharpe Ratio.

## 1. Why Shouldn't We Only Look at Returns?

Intuitively, we often view "**returns**" as the core metric for evaluating an investment's performance, but in real-world investing, "returns" are only half the story.

**Case Study: Green Investment vs. Black Investment**

![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2024/12/23/1734960763355-11eae165-6b02-400e-a5c1-69b78e47cd57.png)

- **Green Investment**: Final total return of 40%, relatively stable process
- **Black Investment**: Also has a final total return of 40%, but with dramatic fluctuations

Though their final returns appear identical, this doesn't mean their "quality" is the same. The black investment's dramatic ups and downs create the following issues:

1. **Psychological Pressure**: If major drawdowns occur mid-way, investors may panic and potentially sell at a loss prematurely.
2. **Lack of Confidence**: Greater volatility makes future performance harder to predict; the steady upward trend of the green investment offers better predictability.
3. **Liquidity Needs**: If cash is needed during a major drawdown in the black investment, one might be forced to sell at a low point, resulting in actual losses.

Conclusion: Given the same "final return," **more stable** investments are clearly more desirable. This introduces the concept of "risk-adjusted returns"—we need to give "volatility" or "risk" its proper place in performance measurement.

## 2. Quantifying "Risk" Using Volatility

To consider risk when measuring returns, we must first quantify risk. **Standard Deviation** or **Volatility** is the most common way to measure risk in investments, denoted as $\sigma$.

Its mathematical definition is:

$$
\sigma = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \bigl(r_t - \bar{r}\bigr)^2}
$$

- $r_t$: Return rate of investment in period $t$
- $\bar{r}$: Average return rate
- $n$: Number of periods in the statistics (e.g., days, weeks, months)

In simple terms, volatility is "**the degree to which returns deviate from their mean**". The higher the volatility, the more unstable the investment's "direction" is, and the higher the risk.

## 3. Definition of the Sharpe Ratio

After having "**volatility**" as a tool to measure risk, we can define "**risk-adjusted return**"—namely the "Sharpe Ratio."

### 3.1 General Form

Theoretically, the most common formula for the Sharpe ratio is:

$$
\text{Sharpe Ratio}
= \frac{\bar{r} - r_f}{\sigma}
$$

- $\bar{r}$: Average return on investment
- $r_f$: Risk-free rate, which may be omitted or simplified in some cases
- $\sigma$: Volatility of investment returns

However, in many quantitative trading practices, especially for short-term periods (such as daily data), many practitioners temporarily ignore $r_f$, or set $$
\sigma = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \bigl(r_t - \bar{r}\bigr)^2}
$$1. This leads to a more simplified form:

$$
\sigma = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \bigl(r_t - \bar{r}\bigr)^2}
$$2

### 3.2 Annualized Sharpe Ratio

For ease of comparison, we sometimes "annualize" the Sharpe ratio. When using **daily data**, it is typically multiplied by $$
\sigma = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \bigl(r_t - \bar{r}\bigr)^2}
$$3 (approximately 252 trading days):

$$
\sigma = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \bigl(r_t - \bar{r}\bigr)^2}
$$4

When using **monthly data**, multiply by $$
\sigma = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \bigl(r_t - \bar{r}\bigr)^2}
$$5 to annualize, and so on.

### 3.3 What Makes It Good?

- **Higher returns lead to higher Sharpe ratio**: Reflects the positive contribution of returns to the metric.
- **Greater volatility leads to lower Sharpe ratio**: Less stable investments are "penalized" more severely.

Therefore, the Sharpe ratio achieves two goals at once: it both encourages high returns and constrains high risk.

## 4. An Intuitive Example of the Sharpe Ratio

Going back to the "Green vs. Black" example from the beginning:

- If we calculate the Sharpe ratio for **green**, assume the result is 2
- For **black**, assume the result is only 0.5
- Given the same 40% return, the Sharpe ratio clearly shows that "green is better than black"

**Reason**: Green is more stable, achieving the same returns as black while taking less risk.

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2024/12/23/1734963810708-b3e038b6-cc6f-43cb-8703-d1c8798f5668.png)

## 5. How to Improve the Sharpe Ratio Through Portfolio Construction?

### 5.1 Diversification

Suppose there are two investments:

- **Red**
- **Blue**

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/02/20/1740049082289-ee4e97e8-da36-4661-9b34-6caef0323e89.png)
They have similar returns and volatility patterns, and each has a Sharpe ratio of 2. They appear to be equally matched. However, if they are **negatively correlated** or have low correlation, meaning when red rises blue falls, or their trends differ significantly, we can combine these two investments with certain weights (for example, 50% each) to create a new portfolio (represented as "Perp" in the figure).

The results are often surprising:

- Red and blue each have a Sharpe ratio of 2
- Their combined portfolio might see the Sharpe ratio soar to 5 (or even higher), maintaining the same returns while significantly reducing volatility

**Reason**: They partially offset each other in price fluctuations, ultimately making the overall portfolio curve smoother.
**Insight**: This is the quantitative manifestation of "**don't put all your eggs in one basket**"; when we seek to "hedge" or "diversify investments," we are essentially trying to improve the portfolio's Sharpe ratio.

## 6. High Sharpe vs. High Returns: The Magic of Leverage

Some might ask: "If one strategy has moderate returns but a high Sharpe ratio, while another strategy has higher returns but an average Sharpe ratio, which should I choose?"

**Answer: In most cases, choose the strategy with the high Sharpe ratio and amplify it through leverage.**

### 6.1 Principles of Leverage

Suppose you have $100 in capital:

1. You borrow another $100 to invest in a certain asset
2. Now your total investment is $200, with a leverage ratio = 2x

- If the asset rises by 1%, you don't earn $1, but rather $2; equivalent to a 2% return on your **principal**
- Similarly, if the asset falls by 1%, the loss is also amplified to $2

Conclusion: **Leverage amplifies both absolute gains and absolute losses, but does not change the Sharpe ratio**. This is because as the return multiple increases, volatility increases proportionally - both are amplified simultaneously, so the ratio between the numerator and denominator remains unchanged.

### 6.2 How to Use Leverage?

- First, select a strategy with a sufficiently high "**Base Sharpe Ratio**"
- If you feel the return level is insufficient, you can apply leverage to the strategy to achieve higher "**Final Returns**"
- During this process, the Sharpe ratio remains largely unchanged (ignoring financing costs, slippage, trading costs, and other real-world factors), meaning you can achieve an "**Stable + Higher Returns**" ideal investment line

**Note**: Excessive leverage can lead to margin calls, liquidity risk, and higher borrowing costs, which need to be carefully controlled.

## 7. Theoretical Support and Common Issues

### 7.1 Statistical Testing: t-Statistic

From a statistical perspective, if we want to test whether a strategy's returns are significantly greater than 0, we calculate the t-statistic (t-stat). Mathematical derivations show that:

$$
\sigma = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \bigl(r_t - \bar{r}\bigr)^2}
$$6

- The higher the Sharpe ratio, the higher the corresponding t-stat
- This means the strategy's profitability is "more statistically significant," and we have more confidence in its continued profitability

### 7.2 Academic Theory: Tangency Portfolio

In modern portfolio theory (as an extension of Markowitz theory), if an investor's objective is to **maximize returns while minimizing variance (or volatility)**, then the optimal choice is the "**tangency portfolio**", which is **the portfolio with the highest Sharpe ratio**. This provides the theoretical foundation for proving that "**higher Sharpe ratios are better**".

### 7.3 Sharpe Ratio Levels in Real Markets

- **S&P 500 Index**: Long-term (20-year period) Sharpe ratio is approximately 0.4~0.5
- **Warren Buffett** (Berkshire Hathaway): approximately 0.75
- **Excellent Hedge Funds**: above 2.0
- **Extreme High Sharpe** (>5): Generally only occurs in small-scale operations, specific market conditions, or near-arbitrage opportunities; difficult to replicate at large scale

If you can maintain a **Sharpe ratio $$
\sigma = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} \bigl(r_t - \bar{r}\bigr)^2}
$$7** over years, you're already outperforming the vast majority of investors in the market.

## 8. Summary

1. While **returns** are important, they shouldn't be viewed in isolation; **risk (volatility)** is equally crucial.
2. The **Sharpe Ratio** combines return and risk, making it the mainstream indicator for measuring "risk-adjusted returns."
3. **Diversification** and **hedging** can reduce overall volatility, significantly improving a portfolio's Sharpe ratio.
4. When a high-Sharpe strategy's absolute returns are insufficient, **leverage** can be considered to enhance returns without reducing the Sharpe ratio.
5. The Sharpe ratio has solid foundations and important status in both statistical and financial theory.
6. Achieving a long-term Sharpe ratio of 2+ can outperform the vast majority of market participants.

**We hope this in-depth introduction helps you better understand the Sharpe ratio. Pursuing higher Sharpe ratios and creating smooth return curves are ultimate goals for many quantitative trading and investment management strategies. Best of luck with your investments!**

---

> **Postscript**:
>
> - The Sharpe ratio used here mostly ignores the risk-free rate $r_f$, as in many current investment environments, $r_f$ is relatively small compared to volatility.
> - In actual trading, factors such as leverage financing costs, transaction costs, slippage, taxes, and market restrictions must be considered, which will affect the actual Sharpe ratio.
> - For strategies with extremely high Sharpe ratios, maintain vigilance and evaluate their robustness and sustainability.
