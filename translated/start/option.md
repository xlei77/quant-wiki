---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# A Trillion-Dollar Mathematical Formula: From Physics Equation to Financial Option Pricing

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## From Physics and Mathematics to Financial Markets

You might find it hard to believe that an equation originating from physics and mathematics could give birth to financial industry chains with a **total scale of trillions of dollars**. However, this is a true story in modern financial history. The pricing theory and techniques of **Options** are deeply influenced by mathematics, statistics, physics, and probability theory. By exploring this interdisciplinary field, we can not only understand the origins of options pricing but also glimpse how quantitative finance evolved from theory to practice, ultimately transforming the way global capital markets operate.

## Options Concepts and Risk Management

An option is a financial contract that gives the holder the "right, but not obligation" to buy or sell an asset at a specific price in the future. Taking a European Call Option as an example:

![](https://fastly.jsdelivr.net/gh/bucketio/img10@main/2024/12/07/1733585704642-512cadf5-b279-4dcd-9bbe-af74db3333b4.png)

- Current underlying asset price is $S_0$
- Strike price (exercise price) is $K$
- Expiration date is $T$
- If the underlying price at expiration is $S_T > K$, the option holder can profit $\max(S_T - K,0)$;
- If $S_T \leq K$, the option holder chooses not to exercise, and the loss is limited to the initial option premium paid.

This type of contract was used as early as 600 BC by the Greek philosopher **Thales**. He secured the right to use olive presses by paying a small fee in advance, and when there was a bumper olive harvest, he could profit from it. This forward-thinking approach to risk and opportunity management represents the fundamental logic behind option design.

## From Random Walk to Option Pricing: Bachelier's Pioneering Work

Early option trading relied entirely on traders' experience and intuition for pricing. It wasn't until 1900 that French mathematician Louis Bachelier proposed in his doctoral thesis that future stock price movements could be viewed as a **symmetric random process**. He assumed that over a short time interval $\Delta t$, the stock price change $\Delta S$ satisfies:

$$
\Delta S \sim \sigma \sqrt{\Delta t} Z
$$

where $\sigma$ is volatility, and $K$0 is a standard normal random variable. As time progresses and price changes accumulate, the distribution of stock price $K$1 approaches normal:

$K$2

(This was the assumption in Bachelier's original model, which was later improved to become the lognormal model.)

By calculating the probabilities of various future prices occurring and setting the expected returns equal for both option buyers and sellers, Bachelier introduced the concept of "fair price" for options. Unfortunately, this revolutionary idea did not receive sufficient attention at the time.

## Brownian Motion and Einstein's Insights

Interestingly, Bachelier's random walk concept perfectly aligns with the study of Brownian Motion in physics. In 1905, **Einstein** proved that the disordered motion of suspended particles results from countless unpredictable molecular collisions. This can be mathematically described using the Wiener Process:

$K$3

Einstein's research indirectly proved the actual existence of molecules and provided a solid physical foundation for stochastic processes. This model of randomness coincides remarkably with the unpredictability of financial prices.

## From Casino Tables to Wall Street: The Evolution of Mathematical Strategies

In the mid-20th century, Ed Thorp profited from mathematical strategies in casino blackjack, then applied similar thinking to the stock market. With **"Hedging"** as the core concept, he reduced risk by dynamically adjusting the ratio between underlying assets and option positions (Delta Hedging). For example, when holding a short call option position, one can hold a corresponding portion of the underlying asset to offset potential losses from price increases, making the overall risk approach neutral.

## Black-Scholes-Merton: The Classic Equation for Option Pricing

![](https://fastly.jsdelivr.net/gh/bucketio/img16@main/2024/12/07/1733585830007-52017b1b-3df3-47dc-a4c5-83c490273f40.png)

In 1973, Fischer Black (F. Black), Myron Scholes (M. Scholes), and Robert Merton (R. Merton) proposed the famous Black-Scholes formula. In this model, the stock price is assumed to follow geometric Brownian motion:

$K$4

where $K$5 is the risk-free interest rate. For European call options, the Black-Scholes pricing formula is:

$K$6

where

$K$7

$K$8 is the cumulative distribution function of the standard normal distribution.

The Black-Scholes model provided a clear and calculable standard for option pricing, which facilitated the rapid growth of the options market, subsequently giving rise to trillion-dollar industries including credit default swaps, over-the-counter derivatives, and asset securitization.

## The Duality of Hedging and Leverage

With explicit pricing formulas, companies and investors can use options and derivatives to precisely **hedge risks**. For example, if airlines are concerned about rising oil prices, they can purchase oil-related options to lock in costs. Meanwhile, options provide leverage effects, allowing investors to gain larger exposure with less capital. However, this leverage can also amplify risks during market volatility. During normal periods, abundant derivatives enhance market liquidity and stability; in extreme turbulence, highly correlated crashes can amplify systemic risks through derivatives markets.

## The Rise of the Quantitative Empire: Jim Simons and Renaissance Technologies

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2024/12/07/1733585876241-95f9b25c-8662-4987-aed1-baf7e76cec70.png)

After the Black-Scholes formula became public, simple arbitrage opportunities gradually diminished. Led by Jim Simons, a group of mathematicians and physicists utilized more sophisticated statistical and machine learning methods to mine massive data for tiny but persistent price patterns. Renaissance Technologies' Medallion Fund achieved an astounding average annual return of 66%, which not only challenged market efficiency theories but also demonstrated the power of advanced mathematical tools.

## The Paradox of Perfect Efficiency

As more scholars and practitioners use mathematical models and algorithms to mine market patterns, markets become more efficient and arbitrage opportunities become harder to find. Theoretically, if all price patterns are exhausted, market prices will truly become a random walk, leaving no easy opportunities for profit. This is the paradox of quantitative finance: **While we use mathematics to approach a perfect market, we are simultaneously reducing the potential for future generations of investors to generate excess returns.**

## Conclusion

From Bachelier's early option pricing framework, to Einstein's Brownian motion, and then to the emergence and widespread application of the Black-Scholes formula, mathematics and physics have provided approaches for understanding and pricing risk in financial markets. Quantitative finance has perfected risk management tools, creating trillion-dollar markets. However, as markets evolve toward efficiency and transparency, the increasingly high "intellectual threshold" has also reduced arbitrage opportunities.

On the endless path toward perfection, we have witnessed great innovations and self-adaptation at the intersection of science and finance. This is precisely the charm of quantitative finance: its endpoint may be a world of indistinguishable randomness, but in the journey toward that endpoint, humanity has completely rewritten the rules of finance in the name of mathematics and science.

---

*If you are interested in the combination of artificial intelligence and quantitative finance, welcome to join the LLMQuant community to explore together the applications of AI in quantitative investment.*