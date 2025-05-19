---
{}
---

## What is Volatility Smile?

The volatility smile is a common graph obtained by plotting the strike prices against implied volatilities for a set of options with the same underlying asset and expiration date. It gets its name from its smile-like shape. The implied volatility increases when options become more out-of-the-money (OTM) or in-the-money (ITM), while it is relatively lower for at-the-money (ATM) options. Not all options exhibit a volatility smile.

### Key Points

- When options have the same expiration date and underlying asset but different strike prices, the implied volatility graph often shows a smile-shaped pattern.
- The volatility smile indicates that in-the-money (ITM) or out-of-the-money (OTM) options have higher implied volatility.
- Options with strike prices near or at-the-money (ATM) typically have the lowest implied volatility.
- Not all options exhibit implied volatility smiles. Short-term options and currency-related options are more likely to show volatility smiles.
- Individual options may also display volatility smiles as they become more in-the-money or out-of-the-money.
- While implied volatility is a factor in options pricing, it's not the only one. Traders need to consider other factors that affect option prices and volatility.

## What Does Volatility Smile Tell Us?

The volatility smile is formed by changes in implied volatility as the underlying asset moves in or out of the money. The more in-the-money or out-of-the-money an option becomes, the higher its implied volatility tends to be, while at-the-money options typically have the lowest implied volatility.

The volatility smile does not conform to the Black-Scholes model, which is one of the primary formulas used for pricing options and other derivatives. The Black-Scholes model predicts that when plotting implied volatility curves against different strike prices, the curve should be flat. According to the model, all options with the same expiration date and underlying asset should have consistent implied volatility, regardless of the strike price. However, this is not the case in reality.

The volatility smile began appearing in option pricing after the 1987 stock market crash. Prior to this, this phenomenon was not present in U.S. markets, suggesting that market structure was more aligned with Black-Scholes model predictions. After 1987, traders realized that extreme events could occur, and markets exhibited significant skewness. Consequently, in reality, implied volatility increases or decreases as options move further in-the-money or out-of-the-money.

Furthermore, the existence of the volatility smile indicates that demand for in-the-money and out-of-the-money options typically exceeds that of at-the-money options. Demand drives prices, which in turn affects implied volatility. This can be partially attributed to the reasons mentioned above. Extreme events can lead to significant fluctuations in option prices, and the possibility of large movements is incorporated into implied volatility calculations.

## Examples of Using Volatility Smile

When comparing different options with the same underlying asset and expiration date but different strike prices, a volatility smile can be observed. When plotting implied volatility against different strike prices, a U-shape may appear. The U-shape is not always as perfect as shown in the above figure.

To roughly estimate whether an option exhibits a U-shape, one can examine an option chain that lists implied volatilities for various strike prices. If the option shows a U-shape, ITM and OTM options should have approximately similar implied volatilities. The further the strike price is from at-the-money, the higher the implied volatility, while options near at-the-money have the lowest implied volatility. If this is not the case, the option does not exhibit the characteristics of a volatility smile.

The implied volatility of a single option can also be plotted as a time series against fluctuations in the underlying asset's price. When prices move in or out, implied volatility may show a U-shape pattern.

This is useful when searching for options with lower implied volatility. In such cases, options close to at-the-money can be selected. If seeking higher implied volatility, more in-the-money or out-of-the-money options should be chosen. However, remember that as the underlying asset's price moves closer to or further from the strike price, this will affect the implied volatility. Therefore, maintaining an options portfolio with specific implied volatility levels will require constant adjustments.

Not all options exhibit a volatility smile. Before using the volatility smile to aid trading decisions, it's essential to verify whether the option's implied volatility truly fits this model.

## The Difference Between Volatility Smile and Volatility Skew/Smirk

While short-term options and foreign exchange options tend to conform to the volatility smile pattern, index options and long-term equity options typically align more with the volatility skew. The skew/smirk indicates that implied volatility may be higher for in-the-money or out-of-the-money options.

## Limitations of Using Volatility Smile

First, it is crucial to determine whether the options being traded truly conform to the volatility smile pattern. While the volatility smile is a model that some options may follow, implied volatility might also better align with reverse or forward skews/smiles.

Furthermore, due to other market factors (such as supply and demand dynamics), the volatility smile (if applicable) may not form a clean U-shape (or smile). While it may have a basic U-shape, it could be quite uneven, with implied volatilities of certain options being higher or lower than what the model would predict.

The volatility smile highlights the direction traders should focus on when seeking higher or lower implied volatilities, but many other factors need to be considered when making options trading decisions.

## References

[1] Luca Benzoni, Pierre Collin-Dufresne, and Robert S. Goldstein. "[Explaining Asset Pricing Puzzles Associated with the 1987 Market Crash](http://pages.stern.nyu.edu/~dbackus/GE_asset_pricing/BCDG%2087%20crash%20Jan%2010.PDF)," Page 1. Journal of Financial Economics, September 2011.