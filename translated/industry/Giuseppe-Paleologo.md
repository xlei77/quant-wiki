---
{}
---

This article features interviews with buy-side heavyweight Giuseppe Paleologo and sell-side leader Nick Baltas, focusing on three "Multi" aspects: Multi-Asset, Multi-Strategy Portfolios, and Multi-Manager Hedge Funds

* Giuseppe Paleologo previously worked at **Citadel** in **Risk and Quantitative Analysis**, served as Head of Enterprise Risk at **Millennium**, and recently became the **Head of Risk Management** at **HRT**

* Nick Baltas is currently a **Goldman Sachs Managing Director** and **Head** of Cross-Asset Delta One, Commodities and Systematic Trading Research & Structuring

## Interview with Giuseppe Paleologo, Currently Head of Risk Management at HRT Hedge Fund

We begin by discussing the practical work of quantitative researchers in multi-manager hedge funds. As a semi-supporting role to the base Portfolio Managers (PMs), Gappy explains how **Portfolio Manager Coverage**, **Factor Hedging**, and **Internal Alpha Capture** work together to help maximize the firm's Profit and Loss (P&L).

Then, we delve deep into the broad areas of **Factor Research** and **Portfolio Construction**, where Gappy shares some of his strong views on factor construction and application. Topics discussed include:

* **Returns and Characteristics**
* **Alpha Signal Mixing and Integration**
* **Single-Period vs Multi-Period Optimization**
* **Linear vs Non-Linear Models**

### 1. **Question**: Gappy, could you briefly introduce your background?

**Answer**:  
I am currently on garden leave, and previously I worked at **Citadel** in **Risk and Quantitative Analysis**, served as the **Head of Enterprise Risk** at **Millennium**, and most recently as the **Head of Risk Management** at **HRT**.

---

### 2. **Question**: What were your responsibilities as a Quant Researcher at various companies?

**Answer**:  
I alternated between two roles: first as a Quantitative Researcher, and second as a Risk Management Consultant. I compare quantitative research to the offensive players in a football team, while risk management is the defense. My responsibility was to ensure that the company's risks aligned with the partners' risk tolerance, to thoroughly understand various strategies, and to prevent the company from encountering worst-case scenarios, or at least make such scenarios bearable.

---

### 3. **Question**: Can you explain the job responsibilities of "Portfolio Manager Coverage"?

**Answer**:  
PM coverage helps evaluate whether portfolio managers are taking appropriate risks and conducts performance attribution analysis. This goes beyond standard attribution analysis to include advanced performance attribution and addressing customized issues, such as factor model adjustments.

---

### 4. **Question**: How do you explain the extreme PnL distributions that hedge funds sometimes face?

**Answer**:  
When PnL is either very large or very small, the distribution of stock contributions tends to be highly uneven, with a small number of stocks making disproportionate contributions to the PnL. This phenomenon is known as "heavy-tailed distribution" and exists not only within individual PM portfolios but also across multiple PMs on hedge fund platforms.

---

### 5. **Question**: What's your view on hedging strategies in hedge funds, especially regarding momentum risk hedging?

**Answer**:  
Hedging strategies vary depending on different portfolios (stocks or derivatives). Companies typically create a hedging account and overlay a hedging portfolio to make the overall portfolio more desirable from a risk perspective. When there are enough Portfolio Managers (PMs), momentum risk becomes very apparent and must be hedged against.

---

### 6. **Question**: How Can Quantitative Research Teams Help Portfolio Managers Generate Alpha? (Alpha Capture)

**Answer**:  
The responsibility of quantitative research teams is to help design appropriate incentive mechanisms that motivate PMs to generate more Alpha. The challenge facing successful hedge funds is not just maintaining a high Sharpe ratio to earn some profits, but rather how to earn more profits while maintaining a high Sharpe ratio.

---

### 7. **Question**: What is your view on the use of returns versus characteristics in factor models?

**Answer**:  
Characteristics are superior to returns as a basis for creating factors because they provide greater explanatory power and have been validated in empirical data. Many hedge funds develop customized factor models to meet their specific needs, as generic factor models may fail commercially because customization is key.

---

### 8. **Question**: Crowding is an interesting phenomenon. What's your view on its impact on hedge funds?

**Answer**:  
Crowding is not a typical factor because it's an endogenous event rather than an external event that repeats daily. However, hedge funds must pay attention to this effect as it can lead to liquidity spirals and events similar to "quant quakes."

---

### 9. **Question**: Do you think quantitative strategies can be applied to asset classes other than stocks?

**Answer**:  
Quantitative strategies are not limited to the stock market; they are widely applied to other asset classes such as foreign exchange and commodities. The principles of factor models can be applied across different markets.

---

### 10. **Question**: What are the fertile areas for future quantitative research? What areas do you think are not fully explored?

**Answer**:  
Although factor models have existed for decades, there are still many unexplored areas, especially in agent-based modeling. This approach is crucial for understanding crowding effects in financial markets.

---

### 11. **Question**: What books or perspectives do you prefer regarding risk management?

**Answer**:  
I really like Aaron Brown's book "Red-Blooded Risk." The book suggests that a good risk manager should not only warn PMs when they're taking on too much risk but should also encourage them to take more risk when necessary, to balance appropriate risk and return.

---

## Interview with **Nick Baltas**, Managing Director at Goldman Sachs, Head of Cross-Asset Delta One, Commodities and Equity Systematic Trading Strategies and Structuring

We begin by discussing how **Nick Baltas** utilizes a broad range of systematic strategy tools when addressing client needs. As the head of cross-asset strategies and structured research at Goldman Sachs, Nick explains the crucial roles of **strategy selection**, **cross-asset investing**, and **client utility functions** in constructing multi-asset portfolios.

First, we explore how Nick leverages his extensive toolkit of systematic strategies to address the challenges faced by asset owners.

Second, we discuss Nick's research on **cross-asset skewness**. This aspect is rarely addressed in cross-asset strategies, and Nick has authored one of the authoritative papers in this field, offering numerous nuanced insights into implementing skewness strategies.

Next, we delve into the broad areas of **cross-asset risk premia** and **portfolio construction**, where Nick shares some of his unique insights into systematic strategy design and application. Topics discussed include:

* **Classification of systematic strategies**
* **Defensive versus return enhancement strategies**
* **Trend following and skewness strategies**
* **Signal mixing and strategy mixing**

Finally, Nick shares his perspectives on **building multi-strategy portfolios**, both from a theoretical standpoint and in terms of practical implementation to meet client needs.

---

### 1. **Question**: How did you start your career? What is your background?

**Nick Baltas' response**:  
I'm from Greece, where I studied Electrical and Computer Engineering. After that, I moved to London to complete my master's degree, followed by a PhD. During my doctoral studies, I gradually transitioned from engineering to financial economics, and began researching equity momentum, correlation risk, and trend-following strategies. After completing my PhD, I briefly worked at a hedge fund before moving into investment banking, where I focused on quantitative research for multi-asset portfolios. Currently, I'm responsible for cross-asset strategy development at Goldman Sachs.

---

### 2. **Question**: You often mention the client's "utility function". Could you explain this concept and its role in systematic investing?

**Nick Baltas's Response**:  
The utility function is a key tool that helps us understand clients' investment objectives. Different types of clients, including sovereign wealth funds, pension funds, family offices, etc., have different investment needs. Some clients pursue defensive portfolios to protect assets from market downturns; others may focus more on returns and are even willing to take on certain risks. By understanding the client's utility function, we can tailor systematic investment solutions specifically for them.

---

### 3. **Question**: When designing investment strategies, how do we find suitable systematic strategies for different utility functions?

**Nick Baltas's response**:  
We categorize strategies into four types: contractual hedging strategies, statistical hedging strategies, diversified risk premium strategies, and return enhancement strategies. Contractual hedging strategies include purchasing put options and constructing collar structures, mainly used to address sudden short-term market volatility. Statistical hedging strategies focus more on long-term trends, such as market conditions like those in 2008 and 2022. Diversified risk premium strategies typically don't increase downside risk, while return enhancement strategies may take on more risk in exchange for higher returns. Through proper classification of different strategies, we can better meet client needs.

---

### 4. **Question**: In hedge funds, how do crowding effects and capacity risks in systematic investment strategies impact strategy performance?

**Nick Baltas's Response**:  
Capacity risk is our primary consideration when constructing systematic portfolios. Capacity risk can be divided into two aspects: position capacity and trading capacity. Position capacity determines how quickly we can exit the market when needed, while trading capacity affects how much market liquidity we can consume in daily operations. We ensure we don't significantly impact the market through controlling daily trading volume and dynamic constraints. Moreover, crowding effects themselves aren't always negative. In some strategies, crowding might be a necessary condition for the strategy to function.

---

### 5. **Question**: How to combine different signals and strategies in a multi-asset strategy? (e.g., trend following and carry strategies)

**Nick Baltas's response**:  
There is a significant difference between combining signals and combining strategies. Combining signals means integrating different signals together before optimization, while combining strategies involves building separate strategies and then merging them. In trend following strategies, we allocate risk through risk budgeting, while in carry strategies, we focus on finding optimal combinations through different market signals. Ultimately, we want the two strategies to complement rather than cancel each other out when combined, leading to better portfolio performance.

---

### 6. **Question**: Why do you prefer using risk budgeting in cross-asset investment strategies?

**Nick Baltas's Answer**:  
I prefer using risk budgeting to manage risks across different assets and strategies. Through risk budgeting, we can ensure that each market has equal risk weight in the portfolio, preventing high-volatility assets from excessively influencing the overall portfolio performance. Risk budgeting is particularly effective for trend-following strategies, as it can dynamically adjust position sizes and automatically modify risk exposure as market volatility changes, thereby optimizing overall performance.

---

### 7. **Question**: You mentioned that philosophical design principles are important when constructing multi-asset portfolios. Could you elaborate on this?

**Nick Baltas's response**:  
I believe there are certain design principles that should always be followed when constructing portfolios, even if these principles don't directly show their effects in backtesting. For example, setting position concentration risk limits, which restrict the maximum risk exposure to each market. While such limitations might not significantly impact backtest results, in actual operations, they can protect the portfolio during market events and prevent excessive exposure to risks in any single market. Therefore, although some design principles may not directly affect backtest results, they are crucial for risk management.

---

### 8. **Question**: What is your view on different risk premium strategies in cross-asset investment, such as trend following, carry strategies, and skewness strategies?

**Nick Baltas's response**:  
Each strategy has its unique characteristics and applicable scenarios. Trend following strategies are typically considered defensive as they perform well during market downturns. Carry strategies rely on time series and cross-market yield differentials, and they may underperform during risk events. Skewness strategies are a type of reversal signal that typically emerges after significant market sell-offs. The combination of different strategies can provide portfolios with broader risk management and return potential, with the specific combination depending on each client's utility function.

---

### 9. **Question**: What areas or research directions are you particularly interested in currently?

**Nick Baltas's response**:  
I've been particularly interested in sleep science lately, especially a book called "Why We Sleep." This book explores why humans need to spend so much time sleeping each day and explains how sleep affects brain function, memory, and learning ability. For me, sleep is a fascinating area of research that's also closely connected to my daily life.

---