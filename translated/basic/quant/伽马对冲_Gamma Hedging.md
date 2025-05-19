---
{}
---

## What is Gamma Hedging?

Gamma hedging is a trading strategy aimed at maintaining stable delta in options positions as the underlying asset price changes, typically keeping delta neutral. This strategy is used to reduce risks when the underlying security experiences sharp rises or falls, especially during the last few days approaching expiration.

The gamma of an options position refers to the rate at which the option's delta changes for every one-point movement in the underlying asset price. Gamma is an important measure of the convexity of derivative value relative to the underlying asset. In contrast, delta hedging strategies can only reduce the impact of small price movements in the underlying asset on option prices.

### Key Points

- Gamma hedging is a sophisticated options strategy used to reduce exposure of options positions to large fluctuations in the underlying security.
- Gamma hedging is also used at options expiration to protect against rapid changes in the underlying asset price, which can occur as expiration approaches.
- Gamma hedging is typically used in conjunction with delta hedging.

## Operating Principles of Gamma Hedging

A gamma-neutral options position refers to a position that is protected against significant fluctuations in the underlying security. Achieving a gamma-neutral position is a method of managing options trading risk by constructing a portfolio where the rate of delta change is close to zero, regardless of whether the underlying asset rises or falls. This process is called gamma hedging. A gamma-neutral portfolio thus hedges against second-order time-price sensitivity.

Gamma hedging is accomplished by adding additional options contracts to the portfolio, typically opposite to the current position. For example, if the position holds a large number of call options, the trader might add a small number of put options to offset unexpected price drops in the next 24 to 48 hours, or sell carefully selected call options at different strike prices. Gamma hedging is a complex activity that requires careful calculation for proper implementation.

## Gamma and Delta

Gamma is a standard variable name inspired by the Greek alphabet, originating from the Black-Scholes model, which is recognized as the first standard formula for option pricing. In this formula, two variables help traders understand how option prices change with movements in the underlying security's price: delta and gamma.

Delta tells traders the expected change in option price for a small movement (specifically a $1 movement) in the underlying stock or asset.

Gamma represents the rate of change in an option's delta as the underlying stock or other asset's price changes. In essence, gamma is the rate of change of the rate of change in option prices. However, some traders also view gamma as the expected change resulting from two consecutive $1 movements in the underlying asset price. Therefore, adding gamma to delta yields the expected change when the underlying security moves $2 in two steps.

## Delta-Gamma Hedging

Delta-gamma hedging is an options strategy that combines delta and gamma hedging to mitigate risks from both the underlying asset and changes in its own delta. Delta hedging alone can protect positions against small movements in the underlying asset. However, larger movements will alter the hedge (changing delta), exposing the position. By adding gamma hedging, the delta hedge remains intact.

When implementing delta-gamma hedging, investors need to create new hedges as the underlying asset's delta changes. The amount of underlying stock bought or sold varies depending on whether the underlying asset price rises or falls and the magnitude of the change.

Traders attempting to maintain delta-hedged or delta-neutral positions typically execute trades that have minimal impact on small, short-term price fluctuations. These trades usually represent bets on volatility, or more specifically, whether demand for options on that security will significantly increase or decrease in the future. However, even delta hedging cannot effectively protect option traders on the day before expiration. On this day, due to the minimal time remaining until expiration, even normal price fluctuations in the underlying security can cause significant changes in option prices. Therefore, delta hedging alone is insufficient in such situations.

Gamma hedging complements delta hedging strategies by protecting traders against price changes beyond expectations, or protecting the entire portfolio, especially when time value has almost completely disappeared, from the effects of rapid price changes on options.

**Important Note:** Although traders often seek delta-gamma hedging to maintain delta neutrality; conversely, traders may wish to maintain specific delta positions, which could be positive delta (or negative delta), while remaining gamma neutral.

## Gamma Hedging and Delta Hedging

As shown above, delta hedging and gamma hedging are typically used in combination. A simple delta hedge can be created by simultaneously buying call options and short selling a certain amount of the underlying stock. If the stock price remains unchanged but volatility increases, traders can profit, unless time decay erodes these profits. Traders can offset the erosion of time value and protect against large changes in delta by adding a put option with a different strike price to these strategies; adding this second call option to the position creates a gamma hedge.

As the value of the underlying stock rises and falls, investors can buy or sell stock as needed to maintain position neutrality. This may increase trading volatility and costs. Delta and gamma hedges don't need to be completely neutral, and traders can adjust their exposure to positive or negative gamma over time as needed.