---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# TradingAgents: Multi-Agent LLM Financial Trading Framework

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## Abstract

In recent years, multi-agent collaboration powered by Large Language Models (LLMs) has made significant progress in automated decision-making and problem-solving. However, in the financial domain, most research remains limited to single agents handling specific trading tasks or using multi-agent frameworks to independently collect data, without fully simulating the "division-collaboration" team dynamics within real trading firms. The proposed "TradingAgents" framework draws inspiration from professional trading companies' organizational structures, creating an LLM-based multi-agent team that includes various roles engaged in fundamental research, sentiment analysis, technical analysis, and trading with different risk preferences. The framework also incorporates bullish and bearish research analysts (Bull and Bear analysts) to balance market views and includes risk management teams for exposure monitoring. Under this system, trading agents make decisions by synthesizing team debates and historical data, simulating real-world collaborative trading environments. Experimental results show that compared to benchmark models, this framework demonstrates significant improvements in cumulative returns, Sharpe ratio, and maximum drawdown metrics, proving the potential of multi-agent LLMs in financial trading applications.

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2025/01/18/1737234033648-6cf5f1c2-7345-437d-9fb8-96ed84ee3156.png)

## Introduction

Large Language Models (LLMs) combined with autonomous agents have demonstrated human-like decision-making and workflow replication capabilities across many fields (see Park et al. [2023]; Havrilla et al. [2024]; Talebirad and Nadiri [2023]; Tang et al. [2024]). By equipping language agents with various "tools" and enabling collaboration among agents, complex problems can be broken down into refined subtasks, thereby enhancing problem-solving capabilities. The financial market, as a highly complex system incorporating multiple dimensions including company fundamentals, market sentiment, technical indicators, and macroeconomic events, presents an ideal application scenario for such multi-agent systems.

Traditional quantitative trading systems typically rely on pure quantitative models, making it difficult to comprehensively capture multi-dimensional influencing factors. However, LLMs' efficient processing of natural language data makes them particularly suitable for analyzing textual information from news, financial reports, and social media. Furthermore, while deep learning-driven black-box trading strategies often lack interpretability, multi-agent LLM frameworks can provide greater explainability through transparent reasoning processes and evidence chains (Li et al. [2023a]; Wang et al. [2024b]; Yu et al. [2024]).

Nevertheless, current frameworks applying LLMs to finance and trading face two major bottlenecks:

1. **Difficulty in Authentically Simulating Trading Company Organizational Structures**  
   Most multi-agent financial applications focus only on narrow tasks (Li et al. [2023a]; Wang et al. [2024b]; Yu et al. [2024]) without simulating the team collaboration and process control aspects of real trading companies' organizational structures, making it challenging to effectively replicate mature trading operations in reality.

2. **Inefficient Communication Interfaces**  
   Many systems rely solely on natural language message records (such as chat histories) or unstructured information pools for decision-making (Park et al. [2023]; Qian et al. [2024]). As the number of dialogue rounds increases, information loss or "cross-talk effects" become more pronounced, making it difficult for agents to maintain consistent context and logical relationships over extended periods (especially in dynamic financial environments).

To address these challenges, this paper proposes a new multi-agent trading system. First, we enhance the authenticity and professionalism of the decision-making process by simulating multi-role, multi-level collaboration in professional trading companies: including fundamental analysts, sentiment/news analysts, technical analysts, and long/short position researchers working together for dynamic decision-making; meanwhile, risk management teams monitor exposures to control downside risks in a timely manner. Second, we adopt a hybrid "structured report + natural language debate" mechanism for communication, ensuring rigor and conciseness in decision transmission while enabling multi-round discussions of complex issues through natural language.

We validate this framework through backtesting experiments on historical financial datasets, comparing it with various benchmark strategies and measuring trading performance using metrics such as cumulative returns, Sharpe ratio, and maximum drawdown. The experimental results demonstrate significant advantages of this framework in both trading performance and risk control.

---

## Related Research

### LLMs as Financial Assistants

In the financial sector, researchers fine-tune large language models on financial corpora or train finance-specific LLMs from scratch to meet professional needs in financial analysis, information retrieval, and decision support.

> **Fine-Tuned LLMs for Finance:**  
> Examples include PIXIU (FinMA) (Xie et al. [2023]), FinGPT (Yang, Liu, and Wang [2023]), and Instruct-FinGPT (Zhang, Yang, and Liu [2023]). These models are fine-tuned on extensive financial domain instructions or data, significantly improving their classification and question-answering performance in financial contexts. In certain scenarios, these models even outperform BloombergGPT (Wu et al. [2023]). However, for more generative tasks, they may still slightly lag behind general-purpose large models like GPT-4.

> **Finance LLMs Trained from Scratch:**  
> Models in this category, such as BloombergGPT (Wu et al. [2023]), XuanYuan 2.0 (Zhang, Yang, and Xu [2023]), and Fin-T5 (Lu et al. [2023]), are jointly pre-trained on massive general data and specialized financial texts to enhance their understanding of financial terminology and tasks. These models often outperform general-purpose models of similar size in tasks like financial sentiment classification or summarization. However, when compared to closed-source large models like GPT-3 or PaLM (Chowdhery et al. [2022]), they may face scale limitations.

Overall, finance-specific LLMs can achieve excellent results in specific tasks, demonstrating the importance of domain adaptation. Building larger-scale or higher-quality finance-specific datasets remains the key pathway to further improving the performance of these models.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/01/18/1737234055721-e826d91a-41f6-4004-88af-b45fd0810e12.png)

> Figure 1: Organizational framework diagram of TradingAgents. I. Analyst team collects market information in parallel; II. Research team conducts debates and evaluations of data; III. Traders make trading decisions based on research opinions; IV. Risk management team monitors risk exposure; V. Fund manager gives final approval and executes trades.

### LLM as Traders

This type of work treats LLMs as intelligent agents for direct trading execution, making automated buy/sell decisions by integrating external data such as news, financial reports, and stock prices. These can be classified into three categories: news-driven, reasoning-driven, and reinforcement learning-driven agents.

> **News-Driven Agents:**  
> Embed news and macroeconomic events into LLM inputs to predict stock price movements. Related research shows that both closed-source models like GPT-3.5 and GPT-4, as well as open-source models like Qwen (Bai et al. [2023]) and Baichuan (Yang et al. [2023]), can execute long-short strategies based on news sentiment scoring (Lopez-Lira and Tang [2023]). Their performance in specific financial domains can be enhanced through fine-tuning (such as FinGPT, OPT, etc.) (Zhang et al. [2024a]; Kirtac and Germano [2024]).

> **Reasoning-Driven Agents:**  
> Enhance reflection and debate mechanisms in trading decisions. For example, FinMem (Yu et al. [2023]) and FinAgent (Zhang et al. [2024b]) perform hierarchical memory retrieval on multimodal data before conducting technical indicator analysis to support more accurate trading decisions (Ji et al. [2023]). Other research on multi-agent debate mechanisms (Xing [2024]; TradingGPT (Li et al. [2023b])) improves decision rationality and robustness through mutual questioning between different LLM roles.

> **Reinforcement Learning-Driven Agents:**  
> Use backtesting returns as reward signals to perform reinforcement learning on LLMs. For example, SEP (Koa et al. [2024]) uses RL with memory and reflection mechanisms to continuously optimize model predictions. Other works combine LLM-generated word vectors with market features to train trading strategies through algorithms like PPO (Ding et al. [2023]; Schulman et al. [2017]).

### Using LLM for Alpha Factor Mining

LLM can also be used to generate Alpha factors rather than directly execute trades. For example, QuantAgent (Wang et al. [2023]) employs a dual-loop (inner-loop/outer-loop) architecture, where the "writer agent" generates scripts based on ideas from the "trader agent," receives feedback from the "judge agent," and finally backtests and iteratively refines these in the real market. AlphaGPT (Wang et al. [2023]) also proposed a human-in-the-loop Alpha factor mining process. Such studies demonstrate that using LLM to generate and optimize trading strategies or factors is both feasible and efficient in practice.

---

## TradingAgents: Role Specialization

By assigning clear roles and objectives to LLM agents, complex trading processes can be broken down into manageable subtasks. Financial trading is particularly well-suited for this model: in reality, trading firms already operate with multiple expert teams working in coordination. TradingAgents draws inspiration from this approach, distributing seven roles within a simulated "trading company": including Fundamentals Analyst, Sentiment Analyst, News Analyst, Technical Analyst, Researcher, Trader, and Risk Manager.

### Analyst Team

The analyst team (see Figure 2) consists of four types of agents, each with specific responsibilities, covering all aspects of market information:

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/01/18/1737234079367-1d92b86f-c1fd-4858-8dcb-5d7a835d4a1e.png)

> Figure 2: Illustration of TradingAgents' Analyst Team

- **Fundamental Analyst**  
  Evaluates companies' intrinsic value by analyzing financial statements, earnings reports, insider trading, and other data to determine whether stocks are undervalued or overvalued, providing reference for long-term investment.

- **Sentiment Analyst**  
  Focuses on social media, sentiment scoring, and internal company sentiment among other public information to predict how short-term investor behavior might impact stock prices.

- **News Analyst**  
  Tracks macroeconomic indicators, major news, and corporate events to identify breaking news or policy changes that could potentially affect the market, providing basis for capturing market turning points.

- **Technical Analyst**  
  Calculates technical indicators such as MACD, RSI, analyzes price-volume relationships and price patterns to determine trading timing and trend directions.

The output from this analyst team forms a comprehensive interpretation of the market, providing reliable information input for the subsequent research team.

### Research Team

The research team (see Figure 3) is primarily responsible for critically evaluating data provided by the analyst team and conducting multiple rounds of debate from both long and short perspectives:

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/01/18/1737234106063-b227bc1d-70c2-4211-aba2-73df9df02669.png)

> Figure 3: TradingAgents Research Team: Bullish and Bearish Perspectives

- **Bullish Researchers**  
  Emphasize positive aspects and growth potential, providing supporting arguments for long strategies.

- **Bearish Researchers**  
  Focus on revealing potential risks and negative signals, providing "opposing" viewpoints to avoid blind market entry.

Through this dialectical approach, the research team can reach balanced conclusions about market risks and returns, providing traders with more comprehensive strategy recommendations.

### Trading Agent

The Trading Agent (see Figure 4) makes specific buy and sell decisions by consolidating opinions from analyst and research teams, combining multi-dimensional inputs including quantitative data and sentiment information:

![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/01/18/1737234120399-46e853de-cc49-471c-9956-21ccb91edba6.png)

> Figure 4: TradingAgents' trader decision-making process

- **Evaluate recommendations from analysts and researchers**
- **Determine trading timing and size**
- **Execute buy/sell orders**
- **Dynamically adjust positions**

As a role directly facing the market, traders need to balance potential returns with risks and respond quickly to market changes.

### Risk Management Team

The Risk Management Team (see Figure 5) monitors portfolio risk exposures in real-time and ensures trading activities comply with pre-established risk parameters and regulatory requirements:

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/01/18/1737234141836-9af89d93-289e-4021-9b3b-c51a0f6f1537.png)

> Figure 5: TradingAgents Risk Management and Fund Manager Approval Process

- **Evaluate market volatility, liquidity, counterparty risks, etc.**
- **Execute risk mitigation strategies, such as stop-loss or position diversification**
- **Provide risk feedback to traders and suggest adjustments**
- **Ensure overall portfolio aligns with company risk appetite**

Through the collaboration of these multiple roles, TradingAgents can execute decision-making processes in a simulated environment that mirror the rigorous, highly specialized internal processes of real trading firms. All agents utilize the ReAct (Yao et al. [2023]) prompting framework, coordinating actions under shared environmental states, and engaging in internal debates or tool calls when needed to ensure dynamic and flexible decision-making.

---

## TradingAgents: Agent Workflow

### Communication Protocol

Currently, most LLM multi-agent frameworks still only use natural language messages as the sole means of communication (Fatouros et al. [2024b]; Li et al. [2023a]; Yang et al. [2024]; Yang, Yue, and He [2023]). However, for tasks like financial trading that require long-term planning and involve complex information dimensions, pure natural language "continuous dialogue" often leads to "cross-talk" or loss of key information (Hong et al. [2024]).

To address this, we draw inspiration from frameworks like MetaGPT and introduce a **structured communication protocol**: transmitting reports through clearly defined formats, ensuring that only information relevant to the specific role is read and processed, and recording it to shared states after report generation. This approach can reduce redundant messages and lower the risk of information distortion during multiple rounds of dialogue.

### Agent Interaction Types

Unlike previous trading frameworks that relied heavily on natural language chat, TradingAgents primarily collaborate through **structured documents** and **brief natural language dialogues**:

- **Structured Reports**:
  - Analyst Team: Each generates concise research reports containing key metrics, conclusions, and recommendations.
  - Traders: After reading analyst reports, provide clear trading signals with rationales, which are then reviewed by the risk management team.

- **Natural Language Discussions**:
  - Research Team: Long/short researchers review global state and analysis reports, engage in n rounds of dialogue, then a "moderator" agent summarizes, provides final views and records them.
  - Risk Management Team: Regarding trader decisions, conducts n rounds of debate based on different risk appetites (aggressive, neutral, conservative), finally the moderator compiles and proposes modifications.
  - Fund Manager: Reviews risk management team's discussions, decides whether to execute and records the final decision.

### Underlying LLM Models

To balance task complexity and speed requirements, we use a mix of different LLMs in the framework:

- **"Fast Thinking" Models (like `gpt-4o-mini`, `gpt-4o`)**: Efficiently handle low-depth tasks such as summarization, data retrieval, or table-to-text conversion.
- **"Deep Thinking" Models (like `o1-preview`)**: Excel at multi-round reasoning, decision-making, and long-text report writing tasks.

Specifically:

- Analyst nodes mostly require deep reasoning capabilities to generate solid analytical results;
- Researchers and traders also rely on deep reasoning models to ensure decision quality;
- Tool and API calls are delegated to relatively lightweight models to improve efficiency.

Through flexible switching between different LLMs, TradingAgents can operate without GPU requirements using only API services, and easily integrate stronger reasoning models or finance-specific models in the future to further improve performance.

---

## Experiment

### Backtesting

We conducted backtesting of the framework using multi-asset, multi-modal stock data from companies including Apple, Nvidia, Microsoft, Meta, Google, etc. The specific data sources include:

- **Historical Stock Prices**: Opening price, high price, low price, closing price, trading volume, etc. from January 1, 2024 to March 29, 2024.
- **News Data**: Daily news from multiple sources including Bloomberg, Yahoo, EODHD, FinnHub, Reddit, covering macroeconomic and company events.
- **Social Media & Sentiment**: Posts from Reddit, X/Twitter and other social platforms, along with sentiment scores calculated by auxiliary LLMs.
- **Insider Trading & Sentiment**: Company insider trading information and public documents.
- **Financial Statements**: Quarterly and annual reports regularly released by companies.
- **Company Profile and History**: Third-party provided profiles and historical financial information.
- **Technical Indicators**: 60 common technical indicators including MACD, RSI, Bollinger Bands, etc.

### Simulation Settings

The backtesting period is from January 1, 2024, to March 29, 2024. TradingAgents only read data from the current day and prior days, avoiding the use of future information (to prevent "look-ahead bias"). Based on the buy, sell, or hold decisions made after analysis, we execute corresponding orders in the simulation environment and record daily returns and risk metrics.

### Benchmark Models

The benchmark strategies for comparison include:

- **Buy and Hold**: Buy and hold all selected stocks on average, without any active trading.
- **MACD Strategy**: Generate buy/sell signals based on crossover points between MACD line and signal line.
- **KDJ + RSI Strategy**: Combine KDJ and RSI indicators to identify overbought/oversold zones for trading.
- **ZMR (Zero Mean Reversion)**: Place orders based on price deviation and reversion signals relative to a benchmark line.
- **SMA (Simple Moving Average)**: Use crossovers between long-term and short-term moving averages for buying or selling.

### Evaluation Metrics

We use the following common indicators to measure the strategy's risk and return:

1. **Cumulative Return (CR)**  

$$
\text{CR} = \left(\frac{V_{\text{end}} - V_{\text{start}}}{V_{\text{start}}}\right)\times 100\%
$$
where $V_{\text{end}}$ is the portfolio value at the end of backtesting, and $V_{\text{start}}$ is the initial portfolio value.

2. **Annualized Return (AR)**

$$
\text{AR} = \left(\left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{\frac{1}{N}} - 1\right)\times 100\%
$$

where $N$ is the number of years (this backtest is approximately 3 months, which can be proportionally converted to annualized figures).

3. **Sharpe Ratio (SR)**  

$$
\text{SR} = \frac{\bar{R} - R_{f}}{\sigma}
$$

4. **Maximum Drawdown (MDD)**  

$$
\text{MDD} = \max_{t \in [0,T]} \Bigl(\frac{\text{Peak}_t - \text{Trough}_t}{\text{Peak}_t}\Bigr)\times 100\%
$$

Reflects the maximum percentage decline in portfolio value from peak to trough during the backtesting period.

## Results and Analysis

### Performance Comparison

Table 1 below shows the performance of TradingAgents compared to various benchmark strategies on stocks including Apple (AAPL), Google (GOOGL), and Amazon (AMZN). We can see that TradingAgents demonstrates clear advantages across all metrics.

**Table 1:** Performance comparison of different methods across four evaluation metrics. Bold values indicate the best statistical indicators, and the last row (improvement) shows the percentage increase of TradingAgents compared to the second-best benchmark.

| Categories | Models | **AAPL** |     | **GOOGL** |     | **AMZN** |
| --- | --- | --- | --- | --- | --- | --- |
| CR%↑ | ARR%↑ | SR↑ | MDD%↓ |  | CR%↑ | ARR%↑ | SR↑ | MDD%↓ |  | CR%↑ | ARR%↑ | SR↑ | MDD%↓ |
| Market | B&H | -5.23 | -5.09 | -1.29 | 11.90 |  | 7.78 | 8.09 | 1.35 | 13.04 |  | 17.1 | 17.6 | 3.53 | 3.80 |
| Rule | MACD | -1.49 | -1.48 | -0.81 | 4.53 |  | 6.20 | 6.26 | 2.31 | 1.22 |  | - | - | - | - |
| Based | KDJ&RSI | 2.05 | 2.07 | 1.64 | 1.09 |  | 0.4 | 0.4 | 0.02 | 1.58 |  | -0.77 | -0.76 | -2.25 | 1.08 |
| Strat- | ZMR | 0.57 | 0.57 | 0.17 | 0.86 |  | -0.58 | 0.58 | 2.12 | 2.34 |  | -0.77 | -0.77 | -2.45 | 0.82 |
| egies | SMA | -3.2 | -2.97 | -1.72 | 3.67 |  | 6.23 | 6.43 | 2.12 | 2.34 |  | 11.01 | 11.6 | 2.22 | 3.97 |
| | TradingAgents | **26.62** | **30.5** | **8.21** | **0.91** |  | **24.36** | **27.58** | **6.39** | **1.69** |  | **23.21** | **24.90** | **5.60** | **2.11** |
|      | Improvement(%) | +24.57 | +28.43 | +6.57 | - |  | +16.58 | +19.49 | +4.26 | - |  | +6.10 | +7.30 | +2.07 | - |

#### Cumulative Returns and Annualized Returns

In **Table 1** and the figure below, TradingAgents achieved **at least 23.21% cumulative returns** and **24.90% annualized returns** on all three stocks, outperforming other benchmark methods by **more than 6.1%**. Notably for the highly volatile AAPL, it achieved **over 26%** returns in just under three months, while many traditional technical indicator strategies showed relatively weak performance during this period.

![](https://fastly.jsdelivr.net/gh/bucketio/img8@main/2025/01/18/1737234726980-6d6ef67a-ac90-4fae-9780-eb6017ad9f78.png)

> (a) Comparison of Cumulative Returns (CR) for AAPL

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/01/18/1737234738834-2023dd7d-baab-464e-9938-14ef7d78b3b7.png)

> (b) Example of specific trading points by TradingAgents on AAPL  
> Green/red arrows indicate long/short timing respectively

#### Sharpe Ratio

TradingAgents also demonstrates outstanding performance in terms of Sharpe ratio: achieving ratios of **above 5.60** on AAPL, GOOGL, and AMZN, which is **at least 2.07** higher than the second-best strategy. This indicates that under the same volatility or risk level, TradingAgents can achieve higher excess returns, demonstrating a better risk-return balance.

#### Maximum Drawdown

Rule-based strategies typically have certain advantages in risk control, but their returns are generally not high. TradingAgents, through multi-agent debates and especially the regulation of risk management teams, not only captures major market opportunities but also manages to control the maximum drawdown around 2, avoiding situations of excessive risk-taking.

#### Interpretability

Compared to most current deep learning trading models which are "black box" decisions, LLM multi-agent systems offer higher interpretability: their operations and reasoning can be output in natural language, which not only makes it easier for traders to understand and debug, but also enables targeted adjustments based on the decision-making process. In the appendix, we list TradingAgents' complete logs for a single day, including how it calls tools, reasons, and executes decisions, demonstrating its transparency far superior to general deep neural network trading strategies.

### Discussion

Experimental results show that through role division, mutual debate, and collaborative decision-making, TradingAgents can significantly improve trading performance. On one hand, the complementary nature of multiple data sources and expert perspectives helps traders make more comprehensive judgments; on the other hand, the risk management team can promptly restrict and optimize strategies, ensuring returns while avoiding severe drawdowns. Furthermore, the reasoning process recorded in natural language between multiple agents provides good explainability and auditability for the strategies, which is particularly crucial in financial practice.

---

## Conclusion

The TradingAgents framework proposed in this paper simulates a multi-role, multi-level collaborative environment similar to a real trading company: each LLM agent specializes in analyzing a specific dimension or taking on specific responsibilities, exchanging information and making decisions through multiple rounds of dialogue and structured reports, ultimately achieving automated stock trading. In backtesting experiments, TradingAgents significantly outperformed various benchmarks in key metrics including cumulative returns, Sharpe ratio, and maximum drawdown.  
In the future, we plan to deploy this framework in live trading environments, further expand the types of roles and task scope, and integrate real-time data processing capabilities to enhance TradingAgents' adaptability to rapidly changing financial markets.

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。