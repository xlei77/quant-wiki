---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# InvestorBench: A Benchmark for LLM Financial Decision-Making Tasks

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

In recent research, Large Language Model (LLM)-based agents have demonstrated exceptional decision-making capabilities in complex and open-ended environments, covering multiple application scenarios including financial trading (Zhang et al. (2024b); Guo et al. (2024); Eigner and Händler (2024); Wang et al. (2024)). However, for specific trading decision needs in the financial domain, constructing a multimodal LLM agent framework adaptable to various financial tasks remains a significant challenge. This primarily stems from the high volatility and diversity of financial markets: agents must not only capture time-sensitive core trading signals but also make high-quality decisions in an environment where information modalities are mixed and market conditions change rapidly.

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2025/01/18/1737237784124-94217376-4d7d-4a1c-a81e-660bd7bffe4f.png)
> **Figure 1: Overall architectural diagram of the InvestorBench framework.**

Moreover, as application scenarios expand from single assets to multiple financial tasks, the influencing factors in financial decision-making become increasingly complex and diverse depending on the task type. For example, single stock trading requires focus on company and industry-level fundamentals and financial report data (Yi et al. (2022)); cryptocurrency trading is more driven by instant news and market sentiment (Bhatnagar et al. (2023)); while ETFs typically emphasize long-term asset allocation and passive investment strategies (Madhavan (2016)).

Although several LLM agent frameworks for specific financial scenarios have recently emerged, such as **FinMem** (Yu et al. (2024a)), **FinAgent** (Zhang et al. (2024a)), **CryptoTrade** (Li et al. (2024)), **FinRobot** (Yang et al. (2024)), and **FinCon** (Yu et al. (2024b)), these solutions often focus on single or few financial tasks and mostly rely on private data, making horizontal comparative evaluation difficult. Therefore, there is an urgent need for an **open-ended benchmark oriented towards multi-task scenarios** that can both uniformly evaluate LLM agents' performance across different financial decision-making tasks and facilitate fair comparison of multimodal data and different models.

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/01/19/1737284464992-0582404b-c648-4999-bb22-4645fb092cd3.png)

To address this, we present **InvestorBench**: an open-source benchmark system for **diverse financial decision-making tasks**. This framework extends the multi-layer memory structure approach of FinMem (Yu et al. (2024a)), covering three core areas: stock trading, cryptocurrency trading, and ETF investment, while providing a multi-source data environment. Compared to traditional methods relying on similarity retrieval (like FinAgent), FinMem-style hierarchical memory with multi-rate decay mechanisms enables LLM agents to more effectively integrate and balance multi-temporal, multimodal information, both reinforcing critical long-term information and responding to short-term trading signals in real-time. Additionally, InvestorBench comes with multiple data sources and evaluation metrics, creating a **unified and extensible** evaluation platform for researchers and practitioners.

> **Our Main Contributions:**
>
> 1. Established **InvestorBench**—the first LLM financial decision benchmark featuring multi-task and multimodal data sources, helping evaluate LLM agents' reasoning and sequential decision-making capabilities in complex, open-ended financial scenarios.
> 2. Provided an **open multi-source financial environment** (stocks, cryptocurrencies, ETFs) with supporting APIs and data repositories, ensuring evaluation reproducibility and extensibility.
> 3. Proposed a **unified and flexible** LLM-Agent framework that can easily substitute different LLMs as the core brain. In this study, we tested **13 models**, including general LLMs and finance-domain fine-tuned LLMs, systematically evaluating their performance across three major financial decision-making tasks.

---

## Introduction

Large Language Models (LLMs) have achieved remarkable results in decision-making tasks across numerous complex scenarios (Zhang et al. (2024b); Guo et al. (2024); Eigner and Händler (2024); Wang et al. (2024)). However, applying them to the **financial domain** remains challenging: financial markets are highly volatile, noisy, time-sensitive, and rich in data types (numerical, textual, macroeconomic indicators, sentiment analysis, etc.). For agents to trade accurately, they need to capture information and make continuous high-quality decisions in partially observable (POMDP) environments (Bertsekas and Shreve (1996); Liu et al. (2020); Kabbani and Duman (2022)).

> **Designing multi-task financial agents is even more challenging:**  
> Different financial products have different focuses—stocks require industry reports and fundamentals; cryptocurrencies are particularly sensitive to real-time news and sentiment; ETFs focus more on long-term portfolio costs and allocation strategies. Therefore, unified evaluation of LLM agents' adaptability and decision quality across different financial tasks has become a key research requirement.

Recently emerged financial LLM multi-agent frameworks, such as FinMem, FinAgent, CryptoTrade, FinRobot, and FinCon, provide different approaches for specific scenarios:

- **FinRobot** focuses on market analysis;
- **FinMem** and **FinAgent** mainly target stock/ETF trading;
- **CryptoTrade** only covers cryptocurrencies;
- **FinCon** ventures into multi-asset portfolio management but is still limited to a small number of stocks.

> **Limitations:** Most frameworks only target limited types of financial decision-making tasks, lacking universality; they often rely on private data, making subsequent evaluation and reproduction difficult.

**InvestorBench** was proposed against this background: it further expands on FinMem's "hierarchical memory + multi-rate decay" foundation, introducing various financial market environments to uniformly evaluate LLM-Agent performance in multi-task decision-making. Its features include:

- **Multi-level Memory**: Unlike FinAgent's pure text similarity retrieval, InvestorBench inherits FinMem's hierarchical memory structure, with different levels distinguishing different temporal decay rates, ensuring balance between timeliness and long-term memory;
- **Coverage of Three Major Tasks**: stock trading, cryptocurrency trading, ETF investment;
- **Open Multi-modal Data Sources**: covering multiple aspects including market data, news, company reports, sentiment, and macroeconomic data.

### Summary

1. Proposes **InvestorBench**, an "open financial multi-task LLM" Benchmark, aimed at evaluating LLM agents in complex, open-ended financial scenarios;  
2. Provides a multi-source real data environment that can be combined with any LLM-agent design;  
3. Systematically tested **13 LLMs** (including closed-source, open-source, and financially fine-tuned models), demonstrating their performance differences in sequential financial decision-making.

---

## LLM Trading Agent

In this section, we will introduce the LLM agent framework provided by InvestorBench, and formally describe financial decision-making tasks based on **Partially Observable Markov Decision Process (POMDP)** (Bertsekas and Shreve (1996); Liu et al. (2020); Kabbani and Duman (2022)).

### 2.1 Definition

The LLM agent in **InvestorBench** consists of several sub-modules, designed to simulate or exceed the research capabilities of professional investors:

- **Brain/Backbone (LLM Core)**: The agent's core, used for understanding and generating natural language, supporting complex reasoning and market information interpretation (such as making market predictions and retrospective analysis).
- **Perception**: The perception module that converts raw market data (numerical, textual, visual, etc.) into structured formats suitable for LLM processing.
- **Profile**: Role and task background description.
  - Role: Configured as a senior investor with dynamic risk preferences (e.g., more aggressive during positive market trends, more conservative otherwise).
  - Task Background: Key information about target assets (historical trends, industry overview, product characteristics, etc.).
- **Memory**: Memory module for storing and retrieving historical market information and reasoning experiences.
  - **Working Memory**: Mainly performs current observations, summaries, and immediate reflections;
  - **Layered Long-term Memory**: Uses multi-layer structure + different decay rate memory mechanisms to ensure distinction and priority management of long, medium, and short-term information.
- **Action**: Executes specific trading instructions, choosing "Buy", "Sell" or "Hold" based on LLM output, and generates next decisions by incorporating profit/loss records and risk feedback.

### 2.2 Financial Decision Modeling

Consider financial trading as an **infinite-horizon POMDP** (Partially Observable Markov Decision Process), with time index $ \mathbb{T} = \{0,1,2,\dots\} $ and discount factor $ \alpha \in (0,1] $.

- **State Space**: $ \mathcal{X} \times \mathcal{Y} $, where $ \mathcal{X} $ represents the observable components (such as market prices), and $ \mathcal{Y} $ represents unobservable components (such as market sentiment).
- **Action Space**: $ \mathcal{A} $, specifically $ \{\text{Buy}, \text{Sell}, \text{Hold}\} $.
- **Reward Function**: $ \mathcal{R}(o,b,a) $, directly using daily Profit and Loss (PnL).
- **Observation Process**: $ \{O_t\} \subseteq \mathcal{X} $, **Reflection Process**: $ \{B_t\} \subseteq \mathcal{Y} $, representing the LLM agent's self-review/reasoning.
- **Strategy**: $ \alpha \in (0,1] $0, where LLM treats prompts as conditions and outputs trading instructions.

Let $ \alpha \in (0,1] $1 be the reward at time $ \alpha \in (0,1] $2, then the objective function for this financial decision is:

$ \alpha \in (0,1] $3

---

## InvestorBench

Next, we will introduce the overall design of the InvestorBench framework, as shown in Figure 1.

### 3.1 Benchmark Components

InvestorBench consists of four major parts:

1. **Data Sources and Market Environment**: Integrates open-source data and third-party APIs (such as Yahoo Finance, SEC EDGAR, etc.) to build a multimodal market environment data warehouse for model construction.  
2. **LLM Agent**: Equipped with sub-modules including Brain, Perception, Profile, Memory, and Action, and can utilize external tools (table parsing, API calls, etc.) for data operations (vector database management, information enhancement and retrieval).  
3. **Financial Decision Tasks**: Provides trading scenarios for three types of assets (stocks, cryptocurrencies, ETFs).  
4. **Evaluation Metrics**: Uses common quantitative indicators in the financial field (such as Cumulative Return CR, Sharpe Ratio SR, etc.) to measure the performance of LLM agents.

### 3.2 Trading Environment

We have constructed three open datasets for three types of tasks (stocks, cryptocurrencies, ETFs), aiming to provide a comprehensive evaluation environment integrating market data, news, and sentiment.

1. **Stock Environment**  
   - **Stock OHLCV**: Daily open, high, low, close prices and trading volume, sourced from Yahoo Finance.  
   - **Company Report Excerpts**: 10-Q, 10-K, etc., downloaded from SEC EDGAR.  
   - **News**: Daily news collection for 7 stocks from 2020-07-01 to 2021-05-06. Partially from Zhou et al. (2021)'s dataset, with Tesla, Apple, and others sourced from Refinitiv Real-Time News.  
   - **Sentiment**: News text classified as positive/negative/neutral using *gpt-3.5-turbo-0125*.

2. **Cryptocurrency Environment**  
   - **OHLCV** data sourced from CoinMarketCap.  
   - **Multi-source crypto news** from cryptonews, cryptopotato, cointelegraph (Vanhoucke (2023)), and another dataset from Zhou et al. (2021);  
   - **Sentiment** similarly generated by *gpt-3.5-turbo-0125*.

3. **ETF Environment**  
   - Based on the **NIFTY** dataset (Saqur et al. (2024)), including ETF-related news headlines and corresponding sentiment labels from 2019-07-29 to 2020-09-21.

In actual backtesting, we split the data by date—allowing agents to build memory databases during the "training/warm-up period" and evaluating final performance during the "testing period."

### 3.3 Evaluation Metrics

We selected four common indicators: **Cumulative Return (CR)**, **Sharpe Ratio (SR)**, **Annualized Volatility (AV)**, and **Maximum Drawdown (MDD)**. Among these, CR and SR are typically considered core metrics: CR reflects long-term return levels, while SR measures the risk-return ratio.  
> **Table 1** lists 13 LLMs tested in InvestorBench, including closed-source APIs, open-source models, and finance domain-tuned models.

---

## Experiments and Results

We conducted tests on three types of single-asset trading scenarios (stocks, cryptocurrencies, ETFs), comparing the performance of open-source models, closed-source models, and finance-specific models. To ensure fairness, we standardized the experimental setup and evaluation metrics, conducting multiple repeated experiments for each model within their respective backtesting periods and using median metrics.

### 4.1 Experimental Setup

- **Benchmark Strategy**: The comparison baseline for stocks and cryptocurrencies is "Buy & Hold", while ETFs can use the same approach or equal-weight portfolio.
- **Temperature Parameter**: The LLM-Agent system is uniformly set to 0.6, balancing consistency and creativity.
- **Backtesting Period**:
  - **Stocks**: Warm-up from 2020-07-01 to 2020-09-30, testing from 2020-10-01 to 2021-05-06;
  - **Cryptocurrencies**: Warm-up from 2023-02-11 to 2023-04-04, testing from 2023-04-05 to 2023-11-05;
  - **ETFs**: Warm-up from 2019-07-29 to 2019-12-30, testing from 2020-01-02 to 2020-09-21.
- **Model Deployment**: Built on vllm; models with less than 10B parameters are deployed on 2 RTX A6000 GPUs, medium-sized models (10-65B) use 4 RTX A6000s, and models larger than 65B use 8 A100 80GB.

### 4.2 Result One: Stock Trading

> **Table 2** shows the trading performance and averages of 13 models across 7 stocks. Figures 3(a) and 3(b) further provide visual comparisons across different categories and parameter scales, leading to the following conclusions:

1. **Closed-source Models Perform Better in Stock Trading**  
   > Compared to open-source or financially fine-tuned models, closed-source models (such as the GPT-4 family, GPT-o1-preview, etc.) demonstrate significantly higher and more stable CR and SR overall. This indicates that although some models have been fine-tuned on financial texts (like Palmyra-Fin-70B), they show no obvious advantages in continuous trading decision scenarios, perhaps because they are primarily designed for long-text interpretation rather than reinforced sequential decision-making.

2. **Increased Parameter Scale Significantly Enhances Reasoning and Robustness**  
   > Among open-source models, LLMs with parameters greater than 67B show higher average CR and SR than medium and small models, with lower variance (see Figure 3(b)). This aligns with common findings: LLM reasoning ability improves with parameter scale, which holds true for highly uncertain stock trading tasks as well.

3. **Closed-source LLMs Have Advantages in High-volatility, Mixed-signal Market Environments**  
   > During the testing period, TSLA and NIO experienced dramatic price fluctuations with mixed market signals, while other targets mostly showed unidirectional upward trends. We observed that closed-source models could better integrate historical momentum, position information, and self-reflection to make more accurate decisions when handling highly volatile targets. While large-scale open-source models also demonstrate some adaptability, they are relatively less effective.

### 4.3 Results 2 & 3: Cryptocurrency Trading and ETF Trading

In cryptocurrency and ETF trading scenarios, market trends also show a certain **mixed bullish/volatile** state. Cryptocurrencies show relatively smaller fluctuations, while ETFs demonstrate more obvious price movements. Key observations include:

1. **Capturing cryptocurrency trading signals requires large-scale open-source LLMs or closed-source models**  
   > As shown in Table 3, small or medium-scale open-source models generally underperform the Buy & Hold baseline in terms of CR and SR, indicating that for such highly sensitive and sentiment-driven crypto markets, LLMs need sufficient reasoning complexity to keep pace.

2. **ETF investment relies more on powerful general pre-trained models**  
   > Table 4 shows that in ETF scenarios, closed-source models significantly outperform other models across multiple metrics including CR and SR. This may be because ETF trading typically requires cross-industry, cross-sector macro logic and long-term strategies; models without extensive pre-trained knowledge find it difficult to uncover key signals.

### 4.4 Discussion

Overall, LLMs show significant variations in trading performance across different asset classes, which reflects both the complexity of financial markets and highlights the importance of **model selection and fine-tuning**. Generally, **closed-source LLMs**, due to their massive underlying training scale and rich parameters, demonstrate stronger reasoning capabilities across multiple scenarios including stocks and ETFs. For **open-source models** to compete, they need to further expand their parameter scale or undergo reinforcement fine-tuning specifically for sequential decision-making. Additionally, whether LLM-Agents can flexibly "remember" historical patterns and conduct dynamic risk assessments greatly affects their robustness under different market conditions. Designs incorporating multi-layer memory and risk adaptation mechanisms prove valuable in complex scenarios.

---

## Related Research

### 5.1 Large Language Models in Finance

The rapid development of general-purpose language models has inspired research into **domain-specific models for finance**, such as FinBert (Liu et al. (2021); Yang et al. (2020)), FinGPT (Liu et al. (2023)), FinMA (Xie et al. (2023)), BloombergGPT (Wu et al. (2023)), and others. These models are pre-trained or fine-tuned on massive financial datasets to accommodate professional terminology and financial task requirements. Meanwhile, the rise of LLMs has also promoted the application of **financial multi-agent systems** in trading and investment research, such as FinMem (Yu et al. (2024a)) and FinAgent (Zhang et al. (2024a)). However, significant differences exist among frameworks in terms of task scope and data types, making it difficult to establish unified standards for comprehensive evaluation of these LLM-Agents.

### 5.2 Financial LLM Benchmarks

Existing general benchmarks for financial NLP, such as **FLUE** (Shah et al. (2022)), cover five tasks including sentiment analysis, news classification, and entity recognition; **Pixiu** (Xie et al. (2023)) and **FinBen** (Xie et al. (2024)) have also expanded to include multimodal and document understanding tasks. However, they mostly focus on **static NLP** tasks and have not yet evaluated **LLM agents in real-time trading and continuous decision-making** scenarios. InvestorBench focuses on testing **dynamic, multi-step decision-making**, filling this gap.

---

## Conclusion

**InvestorBench** offers researchers two main usage modes:

1. **Mode One**: Integrate proprietary or fine-tuned LLMs into InvestorBench's Agent framework for multi-task decision making, and compare results with our provided model benchmarks;
2. **Mode Two**: Directly utilize InvestorBench's environment and evaluation interfaces by integrating them into custom Agents to compare the effectiveness of different Agent designs.
This provides a flexible platform for in-depth exploration of LLM financial decision-making capabilities across diverse real-world environments.

> **Future Outlook**: We plan to expand to richer data modalities (such as audio earnings calls, graphical candlestick charts, etc.), while maintaining framework usability and exploring its potential applications across multi-asset portfolios and longer time horizons.

---

## Limitation

1. Currently, **InvestorBench** primarily focuses on single-asset decision-making tasks and has not yet covered multi-asset portfolio management;  
2. Due to copyright restrictions, the quality of some data may be limited, which could have certain impacts on model evaluation.

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。