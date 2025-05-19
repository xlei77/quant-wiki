---
{}
---

## What is Backtesting?

Backtesting is a general method for evaluating how a strategy or model would have performed in the past. It evaluates the viability of trading strategies by utilizing historical data. If the backtesting results are good, traders and analysts may have confidence in continuing to use the strategy in the future.

### Key Points

- Backtesting evaluates the viability of trading strategies or pricing models by examining historical data.
- The fundamental principle is that any strategy that performed well in the past may also perform well in the future, and vice versa.
- When testing ideas on historical data, it is highly beneficial to reserve a period of historical data for testing. If the test is successful, further validating its potential viability on other time periods or out-of-sample data can increase confidence.

## Understanding Backtesting

Backtesting allows traders to simulate trading strategies using historical data to generate results and analyze risks and profitability before committing any actual capital.

When properly conducted, backtesting that yields positive results assures traders that the strategy is fundamentally sound and may generate profits when implemented in reality. Conversely, backtesting that produces suboptimal results will prompt traders to modify or abandon the strategy.

**Important:** Particularly complex trading strategies, such as those implemented by automated trading systems, often rely heavily on backtesting to prove their worth, as these strategies are too complex to evaluate through other means.

Backtesting can be performed as long as the trading idea can be quantified. Some traders and investors may seek qualified programmers to develop their ideas into testable forms. Typically, this involves programmers coding the ideas into proprietary languages supported by trading platforms.

Programmers can integrate user-defined input variables, allowing traders to "fine-tune" the system. For example, in a simple moving average (SMA) crossover system, traders can input (or modify) the lengths of the two moving averages used in the system. Traders can then backtest to determine which moving average lengths performed best in historical data.

## Ideal Backtesting Scenarios

An ideal backtest selects sample data from a relevant time period, with a duration that should reflect various market conditions. This allows for better judgment of whether the backtest results represent random occurrences or reasonable trading performance.

The historical dataset must include a genuine representative sample of stocks, including those of companies that eventually went bankrupt, were sold, or liquidated. Conversely, including only historical stock data of companies that still exist will artificially generate high returns in backtesting.

Backtesting should consider all trading costs, no matter how trivial they may seem, as these costs can accumulate over the backtesting period and significantly impact the appearance of strategy profitability. Traders should ensure their backtesting software can account for these costs.

Out-of-sample testing and forward performance testing provide further confirmation of system effectiveness and can demonstrate the system's true performance before actual capital is involved. Strong correlation between backtesting, out-of-sample, and forward performance testing results is crucial for determining the viability of a trading system.

## Backtesting and Forward Performance Testing

Forward performance testing, also known as paper trading, provides traders with another set of out-of-sample data to evaluate their system. Forward performance testing simulates actual trading by following system logic in real-time markets. It is called paper trading because all trades are executed only on paper; that is, entries and exits of trades and any profits or losses from the system are recorded, but no actual trades are executed.

An important aspect of forward performance testing is strict adherence to system logic; otherwise, it becomes difficult, if not impossible, to accurately evaluate this step of the process. Traders should honestly record any trade entries and exits, avoiding behaviors such as selectively recording trades or not recording certain trades on paper, rationalizing that "I wouldn't have taken that trade anyway." If a trade occurs following system logic, it should be recorded and evaluated.

## Backtesting and Scenario Analysis

While backtesting uses actual historical data for fitting or success testing, scenario analysis utilizes hypothetical data to simulate various possible outcomes. For example, scenario analysis simulates specific changes in portfolio securities or key factors, such as changes in interest rates.

Scenario analysis is typically used to estimate changes in portfolio value when adverse events occur, and can be used to examine theoretical worst-case scenarios.

## Backtesting Pitfalls

To ensure backtesting provides meaningful results, traders must develop and test strategies with good faith, trying to avoid biases. This means strategy development should not depend on the data used for backtesting.

While this sounds simple, it's actually quite challenging. Traders typically build strategies based on historical data. They must strictly test using data sets different from those used to train the model. Otherwise, the backtest will produce artificially inflated results that have no practical significance.

Similarly, traders must avoid data mining, which involves testing numerous hypothetical strategies against the same data set. This too can produce successes that fail in real-time markets, as many invalid strategies might outperform the market during specific periods purely by chance.

One way to compensate for the tendency toward data mining or selective documentation is to use strategies that succeeded during related or in-sample time periods and backtest them using data from different or out-of-sample time periods. If the backtest results are similar for both in-sample and out-of-sample periods, their validity is more likely to be verified.