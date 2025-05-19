---
{}
---

## What is Delta Neutral?

Delta neutral is a portfolio strategy that achieves an overall delta of zero by balancing long and short positions. Options traders use delta neutral strategies to profit from implied volatility or time decay of options. These strategies are also used for hedging. Below we will explain this strategy for both beginners and experienced traders.

### Key Points

- Delta neutral is a portfolio strategy that balances positive and negative deltas across multiple positions to achieve a total delta of zero for the assets.
- Delta neutral portfolios offset market movements within a certain range, resulting in net zero position changes.
- Options traders use delta neutral strategies to profit from implied volatility or time decay of options.
- Delta neutral strategies are also used for hedging purposes.

## Understanding Delta Neutrality

Understanding the concept of delta is crucial in options trading. Delta is one of the "Greeks" in finance, used to measure the sensitivity of an option's price to changes in the underlying asset's price. More specifically, delta measures the expected change in option price for every $1 movement in the underlying security's price. For example, a call option with a delta of 0.25 and a value of $1.40 would be expected to increase to $1.65 if the underlying asset price increases by $1.

A portfolio's delta can be positive, negative, or neutral, depending on the positions held:

Investors seeking delta neutrality aim to balance these deltas so that the overall portfolio delta equals zero. This balance means that the portfolio remains unchanged during small increases or decreases in the underlying asset's price. However, dramatic price movements, volatility changes, and the passage of time can still affect the portfolio's value. Achieving delta neutrality typically requires constant adjustments, as market changes can cause delta to drift away from zero.

## How Delta Neutral Strategy Works

A positive delta means that when the stock price rises, the option price also increases, and when the stock price falls, it decreases. Conversely, a negative delta means the option price falls when the stock price rises, and vice versa. Before explaining this strategy, let's clarify some terminology:

- Long and Short Positions: A long position means you own the asset and expect its value to rise over time. A short position means you've sold the asset short, expecting it to fall.
- Call and Put Options: These are two types of option contracts. A call option gives the holder (buyer) the right to buy an asset at a specific price during a specific period. A put option gives the holder the right to sell an asset at a specific price during a specific period.
- Delta Values: Long put options have deltas ranging from -1 to 0, while long call options always have deltas between 0 and +1. If holding the underlying asset (typically stock) long, the delta is always 1; if short, it's -1. The combination of negative and positive deltas can result in a total delta of zero.

Now we can understand how delta neutral strategy works to achieve a zero delta. Suppose you have a long position in a stock (delta of +1). To make this position delta neutral, you can buy a put option on that stock (which has a delta range of -1 to 0). This is particularly evident in deep in-the-money call options. If the stock price rises by $1, the long position will gain $1 (because delta is +1). However, the put option's price will fall, offsetting the gain from the long position. This ensures that the overall portfolio value remains unchanged even when the stock price changes.

Similarly, if an option has a delta of zero, and the stock rises by $1, the option price won't increase (common in deep out-of-the-money call options). If an option has a delta of 0.5, then for every $1 increase in the underlying stock, the option price will rise by $0.50. This is because its delta (0.5) multiplied by the stock price movement ($1) results in a $0.50 option price change.

Suppose you hold 200 shares of Company X stock at $100 per share, and you believe the price will rise in the long term. However, you're concerned about potential short-term price drops, so you decide to create a delta neutral position to hedge this directional risk.

Holding 200 shares means your delta is +200. You can find offsetting option contracts to neutralize this delta (i.e., -200).

Let's say you find an at-the-money put option on Company X with a delta of -0.50. The negative sign is because put options gain value when the underlying price falls and lose value when it rises. Stock options represent 100 shares of the underlying asset, so buying one put option on Company X provides: -0.50 × 100 = -50 delta.

If you buy four of these put options, your total delta would be: 400 × -0.5 = -200.

By combining 200 shares of Company X stock and 4 at-the-money put options, your overall position will achieve delta neutrality.

**Important Note:** While initial delta hedging can set up a neutral position, option deltas change as the underlying stock moves. This is known as the option's gamma. Therefore, traders wanting to maintain delta neutrality need to monitor and adjust their positions to re-establish delta balance. This process is called dynamic hedging.

## Advantages and Disadvantages of Delta-Neutral Positions

### Advantages and Disadvantages of Delta Neutrality

#### Advantages

- Hedging against small price movements
- Allows option traders to focus on non-directional strategies
- Flexibility in establishing delta-neutral positions

#### Disadvantages

- Significant sudden movements may expose directional risk due to gamma
- Monitoring and adjustments can be expensive and time-consuming

The main benefit of a delta-neutral position is its immunity to small price movements in the underlying asset, whether up or down. This strategy is about predicting how stock prices will change without worrying about small price fluctuations.

Delta-neutral traders typically seek to profit from option time decay (represented by the Greek letter theta) or changes in implied volatility (the Greek letter vega), rather than focusing on directional stock movements. Since delta-neutral trading focuses on offsetting price movement risk, traders can concentrate more on other factors affecting option values.

However, delta-neutrality also means missing out on those price movements, which represents an opportunity cost for some traders. Even if you're not concerned about these price changes, maintaining a delta-neutral position still requires active monitoring and adjustment as the underlying asset moves, which can be costly and unsuitable for inexperienced traders.

Furthermore, sudden large market movements can lead to significant losses because the position is only neutral to small price changes. Therefore, significant and sudden market events can disrupt this strategy.

## How Does Delta Hedging Work?

Delta hedging minimizes directional risk associated with changes in the underlying asset price by using offsetting positions in options contracts. The typical approach is to buy or sell options with equal but opposite exposure to the underlying asset. By doing so, gains (losses) in the underlying asset will be offset by equivalent losses (gains) in the options position.

## Can Delta Neutrality Be Achieved Using Call or Put Options?

Yes. If you hold shares of stock, you can buy put options or sell call options. You can also create a delta-neutral position using options alone, such as holding an at-the-money straddle where you buy a call option with a delta of +0.50 and a put option with a delta of -0.50.

## How Do Option Traders Profit from Delta-Neutral Positions?

Option traders can profit from delta-neutral positions by selling options and collecting time decay as time passes. This strategy can be optimized by eliminating exposure to small price movements. Similarly, traders may bet on whether the underlying asset's volatility will increase or decrease in the future. Delta-neutral positions allow such traders to isolate volatility factors from market direction.

## Summary

Delta neutrality occurs when a trader's net position offsets market price movements, whether up or down. This is achieved by offsetting the delta of one financial instrument against the delta of others. This balance means that small changes in the underlying asset price have minimal impact on the overall value of the combined position (e.g., stocks plus options). The concept relies on gains from one side offsetting losses from the other.

However, it's important to remember that delta is not static; it changes with market movements (gamma) and the passage of time. Therefore, maintaining a delta-neutral position typically requires continuous adjustments, known as dynamic hedging.

## References

[1] D. Passarelli. "[Trading Options Greeks: How Time, Volatility, and Other Pricing Factors Drive Profits](https://www.wiley.com/en-gb/Trading+Options+Greeks:+How+Time,+Volatility,+and+Other+Pricing+Factors+Drive+Profits,+2nd+Edition-p-9781118225127)." John Wiley & Sons, 2020. Pages 237-268.