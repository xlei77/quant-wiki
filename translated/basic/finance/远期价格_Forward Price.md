---
{}
---

## What is Forward Price

The forward price is the predetermined delivery price agreed upon by both parties in a forward contract for the underlying commodity, currency, or financial asset, which will be paid on a specific future date. At the inception of the forward contract, the forward price makes the contract value zero, but changes in the underlying asset price will cause the forward price to show positive or negative values.

The formula for calculating the forward price is as follows:

$$ \begin{aligned} &F_0 = S_0 \times e^{rT} \\ \end{aligned} $$

## Basic Concepts of Forward Prices

Forward prices are built upon the current spot price of the underlying asset, plus any holding costs, such as interest, storage costs, foregone interest, and other expenses including opportunity costs.

While the contract has no intrinsic value at inception, it may gain or lose value over time. Hedging positions in forward contracts are equivalent to a zero-sum game. For example, if one investor holds a long position in a pork futures contract while another investor holds a short position, any gains from the long position will equal the losses incurred by the second investor from the short position. By setting the initial value of the contract to zero, both parties are equal at the contract's inception.

### Key Points

- Forward price is the price at which the seller delivers the underlying asset, financial derivative, or currency to the buyer on a predetermined date.
- Forward price roughly equals the spot price plus associated holding costs, such as storage costs, interest rates, etc.
- Investors may want to lock in a forward price to hedge against future market volatility risks.
- The disadvantage of locking in a forward price is that the asset's value may move unfavorably against the investor.

## Forward Price Calculation Example

When the underlying asset in a forward contract pays no dividends, the forward price can be calculated using the following formula:

$$ \begin{aligned} &F = S \times e ^ { (r \times t) } \\ &\textbf{其中:} \\ &F = \text{合约的远期价格} \\ &S = \text{基础资产的当前现货价格} \\ &e = \text{近似为2.7183的数学无理常数} \\ &r = \text{适用于远期合约存续期的无风险利率} \\ &t = \text{以年份计的交付日期} \\ \end{aligned} $$

For example, suppose a security currently trades at $100 per unit. An investor wants to enter into a forward contract expiring in one year. The current risk-free annual interest rate is 6%. Using the above formula, the calculated forward price is:

$$ \begin{aligned} &F = \$100 \times e ^ { (0.06 \times 1) } = \$106.18 \\ \end{aligned} $$

If there are holding costs, these will be added to the formula:

$$ \begin{aligned} &F = S \times e ^ { (r + q) \times t } \\ \end{aligned} $$

Here, q represents the holding cost.

If the underlying asset pays dividends during the contract period, the forward price formula becomes:

$$ \begin{aligned} &F = ( S - D ) \times e ^ { ( r \times t ) } \\ \end{aligned} $$

Where D equals the sum of the present values of each dividend, calculated as:

$$ \begin{aligned} D =& \ \text{PV}(d(1)) + \text{PV}(d(2)) + \cdots + \text{PV}(d(x)) \\ =& \ d(1) \times e ^ {- ( r \times t(1) ) } + d(2) \times e ^ { - ( r \times t(2) ) } + \cdots + \\ \phantom{=}& \ d(x) \times e ^ { - ( r \times t(x) ) } \\ \end{aligned} $$

Continuing with this example, assume the security pays a dividend of 50 cents every three months. First, calculate the present value of each dividend:

$$ \begin{aligned} &\text{PV}(d(1)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 3 }{ 12 } ) } = \$0.493 \\ \end{aligned} $$

$$ \begin{aligned} &\text{PV}(d(2)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 6 }{ 12 } ) } = \$0.485 \\ \end{aligned} $$

$$ \begin{aligned} &\text{PV}(d(3)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 9 }{ 12 } ) } = \$0.478 \\ \end{aligned} $$

$$ \begin{aligned} &\text{PV}(d(4)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 12 }{ 12 } ) } = \$0.471 \\ \end{aligned} $$

The sum of these present values is $1.927. Then substitute this amount into the dividend-adjusted forward price formula:

$$ \begin{aligned} &F = S \times e ^ { (r \times t) } \\ &\textbf{其中:} \\ &F = \text{合约的远期价格} \\ &S = \text{基础资产的当前现货价格} \\ &e = \text{近似为2.7183的数学无理常数} \\ &r = \text{适用于远期合约存续期的无风险利率} \\ &t = \text{以年份计的交付日期} \\ \end{aligned} $$0

## What is the difference between forward price and spot price?

The forward price refers to the predetermined future delivery price of the underlying commodity, currency, or financial asset agreed upon by both parties in a forward contract. In contrast, the spot price is the current market price of the asset.

## Why Do Some Investors Want to Lock in Forward Prices?

Investors may want to lock in forward prices to hedge against future market volatility risks. For example, farmers might want to enter into forward wheat contracts before harvest to protect against potential grain price declines due to drought or floods.

## What are the disadvantages of locking in forward prices?

The main disadvantage of locking in forward prices is that the asset's value may adversely affect the investor, resulting in losses compared to selling at spot prices upon delivery. Additionally, forward contracts with longer maturities increase the risk of non-payment or default.

## What are the main factors affecting asset forward prices?

Investors determine an asset's forward price based on its current spot price plus holding costs (such as storage, transportation, opportunity costs, and foregone interest). Generally, holding costs are higher for forward contracts with longer maturities.

## Conclusion

The forward price is the future delivery price of an asset agreed upon by both parties in a forward contract. Such contracts have zero value at inception since market conditions have not yet changed. Investors determine the forward price by adding the spot price of the underlying asset to the cost of carry. Using forward prices in futures contracts provides hedging against market fluctuations, but this can be a double-edged sword if the asset's value moves unfavorably for the investor.