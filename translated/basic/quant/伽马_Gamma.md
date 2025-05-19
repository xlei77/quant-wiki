---
{}
---

## What is Gamma?

Gamma (Γ) is an option risk measure that describes how much the Delta of an option changes for each point movement in the underlying asset price. Delta represents how much the option premium (price) changes for each point movement in the underlying asset price. Therefore, Gamma measures how the rate of change in option price varies with fluctuations in the underlying price. The higher the Gamma, the greater the volatility in the option price.

Gamma is an important indicator that measures the convexity of a derivative's value relative to its underlying asset. It is one of the "option Greeks," used alongside Delta, Rho, Theta, and Vega. These metrics are used to evaluate different types of risks in options portfolios.

### Key Points

- Gamma is the rate of change in an option's Delta value based on a unit change in Delta price.
- It is a second-order risk factor, sometimes referred to as the Delta of Delta.
- Gamma is highest when options are at-the-money and lowest when options are far from being at-the-money.
- All else being equal, options closer to expiration have higher Gamma than longer-dated options.
- Gamma is used to measure how changes in the underlying asset will affect an option's moneyness.
- Delta-Gamma hedging can protect option positions against movements in the underlying asset.

## Understanding Gamma

Gamma is the first derivative of Delta, used to measure option price movements relative to how far in-the-money or out-of-the-money the option is. It describes how Delta changes with respect to changes in the underlying asset. Therefore, if an option has a Delta of +40 and a Gamma of 10, a $1 increase in the underlying price will cause the option's Delta to become +50.

Gamma is small when the measured option is deep in-the-money or deep out-of-the-money. Gamma is largest when the option is near or at-the-money. Gamma is also larger for options closer to expiration compared to longer-dated options.

Gamma is an important indicator because it addresses convexity issues in option hedging strategies.[1] Some portfolio managers or traders may be involved with portfolios of very large value and thus require greater precision in hedging. A third-order derivative called "Color" can be used. Color measures the rate of change in Gamma and is important for maintaining Gamma-hedged portfolios.

**Note:** Similar to physics, an option's Delta is its "velocity," while an option's Gamma is its "acceleration."

## What is the Purpose of Gamma?

Since option Delta values are only valid for a short period, Gamma provides traders with a more precise picture of how an option's Delta changes over time and with changes in the underlying price. Delta is the rate of change in option price relative to changes in the underlying asset price.

As options become more in-the-money, Gamma decreases, approaching zero, while Delta approaches 1. As options become more out-of-the-money, Gamma also approaches zero. Gamma is highest when the price is at-the-money.

Calculating Gamma is complex and requires financial software or spreadsheets to find exact values. However, the following demonstrates an approximate calculation of Gamma. Consider a call option on an underlying stock that currently has a Delta of 0.40. If the stock value increases by $1.00, the option value will increase by 40 cents, and its Delta will also change. After the $1 increase, suppose the option's Delta is now 0.53. The 0.13 difference in Delta can be considered an approximate value of Gamma.

**Important Note:** All long option positions have positive Gamma, while all short options have negative Gamma.

## Gamma Example

Suppose a stock is trading at $10, and its option has a Delta of 0.5 and a Gamma of 0.10. Then, for every $1 movement in the stock price, the Delta will adjust by 0.10. This means that a $1.00 increase will result in the option's Delta increasing to 0.60. Similarly, a $1.00 decrease will cause the Delta to decrease to 0.40.

## How Do Traders Hedge Gamma?

Gamma hedging is a strategy that attempts to maintain a constant Delta in an options position. This is achieved by buying and selling options to offset each other, bringing the net Gamma close to zero. At this point, the position is referred to as Gamma neutral. Typically, traders also want to maintain zero Gamma around a Delta neutral (zero Delta) position. This is accomplished through Delta-Gamma hedging, where both net Delta and net Gamma are close to zero. In this case, the value of the options position can be protected from changes in the underlying asset price.

## What is Long Gamma Strategy?

If a trader is long Gamma, their option position's Delta increases with changes in the underlying asset's price. For example, a long Gamma position will see continuously increasing Delta as the underlying price rises, or continuously decreasing Delta as the price falls. If the trader can sell Delta when prices rise and buy Delta when prices fall, a long Gamma exposure can generate net profits by incentivizing the trader to consistently buy low and sell high.

## What is Gamma Risk?

For option positions with short Gamma, there is a risk of compounded losses due to underlying price movements. For example, if such a position starts Delta-neutral and the stock rises, it will generate increasingly negative Delta for the position, thus causing the options to lose more and more money as the underlying rises. However, the risk lies in that if Delta is bought at these increasingly higher prices, the underlying may reverse direction and fall, generating positive Delta during the decline, thereby amplifying the previous losses.

## Conclusion

Gamma measures the rate of change in Delta for each point increase in the underlying asset. It is a valuable tool that helps traders predict changes in the Delta of options or overall positions. Gamma is larger for at-the-money options and gradually decreases for both in-the-money and out-of-the-money options. Unlike Delta, Gamma is always positive for both long call and put options.

## References

[1] Sheldon Natenberg. "Option Volatility Trading Strategies." John Wiley & Sons, 2012.