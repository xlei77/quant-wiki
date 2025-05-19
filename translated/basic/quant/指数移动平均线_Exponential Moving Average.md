---
{}
---

## What is Exponential Moving Average (EMA)?

The Exponential Moving Average (EMA) is a weighted moving average (MA) that assigns greater weight and importance to more recent data points. The Exponential Moving Average is also known as the Exponentially Weighted Moving Average. Compared to the Simple Moving Average (SMA), EMA responds more significantly to recent price changes, while SMA assigns equal weight to all observations within the period.

### Key Points

- EMA is a moving average that assigns greater weight to the most recent data points.
- Like all moving averages, this technical indicator is used to generate buy and sell signals based on crossovers and deviations from historical averages.
- Traders typically use different EMA lengths, such as 10-day, 50-day, and 200-day moving averages.

## Exponential Moving Average (EMA) Formula

$$ \begin{aligned} &\begin{aligned} EMA_{\text{今天}}=&\left(\text{今天的值}\ast\left(\frac{\text{平滑因子}}{1+\text{天数}}\right)\right)\\ &+EMA_{\text{昨天}}\ast\left(1-\left(\frac{\text{平滑因子}}{1+\text{天数}}\right)\right)\end{aligned}\\ &\textbf{其中：}\\ &EMA=\text{指数移动平均线} \end{aligned} $$

While there are many possible choices for the smoothing factor, the most common choice is:

- Smoothing factor = 2

This gives greater weight to the most recent observations. If the smoothing factor increases, recent observations will have a larger impact on the EMA.

## Calculating EMA

Calculating EMA requires one more observation than SMA. If you want to use 20 days as the observation period for EMA, you must wait until day 20 to obtain the SMA. On day 21, you can use the previous day's SMA as the first EMA for yesterday.

The calculation of SMA is relatively straightforward. It is simply the sum of stock closing prices during the time period divided by the number of observations in that period. For example, a 20-day SMA is the sum of closing prices over the past 20 trading days divided by 20.

Next, you need to calculate the multiplier used for smoothing (weighting) the EMA, typically calculated using the formula: [2 ÷ (number of observations + 1)]. For a 20-day moving average, this multiplier is [2/(20+1)] = 0.0952.

Finally, use the following formula to calculate the current EMA:

- EMA = Closing Price × Multiplier + EMA(previous day) × (1-Multiplier)

EMA assigns higher weights to recent prices, while SMA assigns equal weights to all values. For short-term EMAs, the latest price carries more weight than in long-term EMAs. For example, with a 10-period EMA, the multiplier for the most recent price data is 18.18%, while for a 20-period EMA, the weight is only 9.52%.

There are slight variations of EMA that use opening price, high price, low price, or median price instead of closing price.

## What Can EMA Tell You?

The 12-day and 26-day Exponential Moving Averages (EMA) are commonly cited and analyzed short-term moving averages. The 12-day and 26-day EMAs are used to create indicators such as the Moving Average Convergence Divergence (MACD) and the Percentage Price Oscillator (PPO). Generally, the 50-day and 200-day EMAs are used as indicators of long-term trends. When a stock price crosses the 200-day moving average, it is often considered a technical signal of price reversal.

Traders who use technical analysis find moving averages very useful and insightful when properly applied. However, they also recognize that these signals can cause confusion when misused or misinterpreted. All commonly used moving averages in technical analysis are lagging indicators.

Therefore, conclusions drawn from applying moving averages to specific market charts should aim to confirm market trends or indicate their strength. Usually, the best time to enter the market has already passed before the moving average shows that the trend has changed.

EMA somewhat mitigates the negative effects of lag. Because EMA calculations give more weight to recent data, it "hugs" price action more closely and responds more quickly. This is particularly important when using EMA to generate trade entry signals.

Like all moving average indicators, EMA works best in trending markets. When the market is in a strong and sustained uptrend, the EMA indicator line will also show an uptrend, and vice versa. An alert trader will pay attention to the direction of the EMA line and its rate of change from one bar to the next. For example, suppose the price action of a strong uptrend begins to flatten and reverse. From an opportunity cost perspective, it might be time to switch to more bullish investments.

## Examples of How to Use EMA

EMA is typically used in combination with other indicators to confirm significant market changes and evaluate their effectiveness. EMA is more applicable for traders who operate in intraday trading and fast-moving markets. Traders often use EMA to determine trading bias. If the EMA on a daily chart shows a strong upward trend, intraday traders might adopt a strategy of trading only in the long direction.

## Differences between EMA and SMA

The main difference between EMA and SMA lies in their sensitivity to data changes used in calculations.

Specifically, EMA assigns higher weights to recent prices, while SMA assigns equal weights to all values. These two moving averages are similar in that they are interpreted in the same way, and technical traders typically use them to smooth out price fluctuations.

Since EMA weights recent data more heavily than older data, it responds more quickly to the latest price changes compared to SMA. This makes EMA results more timely, which explains why many traders prefer to use EMA.

## Limitations of EMA

It is not clear whether more recent days within a time period should be given greater emphasis. Many traders believe that newer data better reflects the current trend of a security. At the same time, some argue that excessive focus on recent data can lead to bias, resulting in more false signals.

Similarly, EMA relies entirely on historical data. Many economists believe that markets are efficient, meaning that current market prices already reflect all available information. If markets are indeed efficient, then using historical data should not provide any guidance on the future direction of asset prices.

## What is a Good Exponential Moving Average?

Long-term EMAs (such as 50-day and 200-day) tend to be used by long-term investors, while short-term investors tend to use 8-day and 20-day EMAs.

## Is Exponential Moving Average Better Than Simple Moving Average?

EMA places more emphasis on recent price movements, which means it responds more quickly to price changes than SMA.

## How to Interpret Exponential Moving Averages?

Investors typically view rising EMAs as support levels for price action, while declining EMAs are seen as resistance. Based on this interpretation, investors look for buying opportunities when prices approach rising EMAs, and selling opportunities when prices approach declining EMAs.