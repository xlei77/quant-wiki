---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

This article introduces a novel quantitative investment framework that aims to discover and optimize Alpha factors in stock investment strategies through the collaboration of **Large Language Models (LLMs)** and **multi-agent** systems. This method screens and generates a diverse set of Alphas from multimodal financial data (financial reports, prices, news, charts), and then dynamically evaluates and selects the optimal factors through a multi-agent mechanism based on real-time market contexts, thereby constructing investment portfolios with stronger adaptability and more stable performance.

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/02/01/1738398298801-307d1f4e-f7b3-498f-a775-a46708bb30c0.png)

---

## 1. Introduction

### 1.1 Background and Motivation

As deep learning achieves significant progress in financial trading prediction, many researchers and practitioners are dedicated to developing more stable and reliable quantitative investment models. However, current models often perform inconsistently across different market environments, with their predictive capabilities being susceptible to noisy data or market volatility. Moreover, in real trading scenarios, data comes in various forms (text, charts, financial indicators, etc.), and how to better integrate and distill this information has become a new challenge in quantitative investment.

> The core ideas of our proposed **new quantitative investment framework** are:  
> **(1) Large Language Models (LLM)** provide powerful information extraction and reasoning capabilities, enabling automatic generation and screening of diverse Alpha factors;  
> **(2) Multi-agent System** dynamically evaluates market conditions, achieving adaptive weighting and combination of strategies in an ever-changing environment.

### 1.2 Main Challenges in Alpha Mining

1. **Rigidity of Traditional Methods**: Many Alpha mining approaches are based on heuristics or empirical rules, making it difficult to quickly adapt to different market environments;  
2. **Difficulty in Multi-source Data Integration**: Information in financial markets extends beyond prices and financial indicators, including news, social media sentiment, economic data, etc.;  
3. **Market Changes**: Alpha strategies that perform well may become ineffective in different market conditions; the key is how to capture and follow structural market transitions.

### 1.3 Framework Overview

To address the above challenges, we propose a quantitative investment solution that integrates LLM exploration, multi-agent selection, and dynamic strategy reweighting.
- **LLM-Generated Alpha**: Extract seed alpha factors from multimodal information including academic papers, financial literature, financial data, and visualizations;
- **Multi-Agent System**: Screen, validate, and confidence-score these alphas under different risk preferences and market scenarios;
- **Dynamic Reweighting**: Automatically adjust the weights of each alpha in the final investment strategy based on market conditions through deep neural networks or other learning methods.

> We conducted extensive empirical tests in China's A-share market (using the SSE 50 Index as an example), with results showing superior performance across multiple metrics compared to traditional methods and other SOTA baselines.

---

## 2. Problem Formulation

### 2.1 Alpha Factors and Portfolio Strategy

In quantitative investment, we typically calculate multiple Alpha factors for n selected stocks during each trading day or trading period.

$\alpha = \sum_i w_i \alpha_i$

Where $\alpha_i$ represents a seed Alpha factor, and $w_i$ is its weight in the final portfolio. Our goal is to find the optimal factor combination that fits the current market scenario and dynamically allocate weights through historical backtesting and real-time market evaluation.

### 2.2 Seed Alpha Mining and Selection

Traditional Alpha mining often relies on static rules or expert experience, making it difficult to handle sudden environmental changes or massive multi-source data. Therefore, we utilize LLM's exploratory capabilities combined with a multi-agent system to achieve:  
1. **LLM Automatic Generation**: Mining potential formulaic Alphas from multi-modal data including academic papers, financial reports, and news;  
2. **Multi-agent Rigorous Evaluation**: Conducting backtesting and market adaptability assessment, providing confidence scores \(\theta\);  
3. **Categorization**: Classifying Alpha factors into independent major categories such as momentum, mean reversion, volatility, fundamentals, etc., facilitating further selection and combination.

### 2.3 Alpha Formalization

We require the seed Alphas produced by LLM to have "interpretable formulaic forms," including:
- **Cross-sectional operations** (such as addition, logarithm, and other short-term operations);
- **Time-series operations** (requiring multi-day data, such as moving averages, lags, etc.).

---

## 3. Methodology

Our overall approach can be divided into three main modules: **(1) Seed Alphas Factory**, **(2) Multi-modal Multi-agent Evaluation**, and **(3) Dynamic Weight Optimization**.

### 3.1 Framework Overview

1. **LLM Seed Alpha Factory**:  
   - Filter and classify multimodal literature, charts, and financial data through large language models to output potential seed Alphas;  
   - Use traditional financial research Alpha categories as foundation (such as momentum, mean reversion, etc.) to ensure relative independence between factors;  
2. **Multi-Agent Decision Making**:  
   - For different risk preferences and market conditions, multiple agents screen high-confidence Alphas in a multimodal data environment (text, numerical, graphical, audio-visual, etc.);  
   - Each agent assigns confidence scores to factors based on backtesting performance and interpretation of market information;  
3. **Dynamic Weight Optimization**:  
   - Finally, combine these candidate Alphas through deep learning (e.g., DNN) to learn their predictive power for future returns;  
   - Continuously adjust weights according to market conditions to achieve adaptive quantitative strategies.

### 3.2 LLM Filtering and Classification

In the first phase, we provide multimodal research documents to LLMs (such as ChatGPT's customized version "Alpha Grail") for summarization, classification, and generation of structured seed Alpha lists.  
- **Multiple Document Sources**: Academic papers, financial reports, charts, financial statements;  
- **Classification Results**: Such as Momentum, Mean Reversion, Volatility, Fundamental, etc.;  
- **Each category contains several specific Alpha formulas**: Such as momentum factor (CLOSE - DELAY(CLOSE,14)), volatility factor STD(CLOSE, 20), etc.

### 3.3 Multimodal Multi-Agent Alpha Evaluation

In the second phase, the multi-agent system combines **text, numerical data, visualization, audio/video** and other multimodal data to evaluate these seed Alphas:  
1. **Risk Preference Analysis**: Different agents with varying risk tendencies (conservative, neutral, aggressive, etc.) score the historical performance of Alphas;  
2. **Adaptive Backtesting**: Simulates trading performance under different market conditions, focusing on metrics such as Information Coefficient (IC), Sharpe Ratio, etc.;  
3. **Confidence Scoring**: Each agent assigns confidence scores to Alphas to filter out unreliable or underperforming factors;  
4. **Algorithmic Automated Selection**: Selects a subset of qualifying Alphas by setting confidence thresholds.

### 3.4 Alpha Weight Optimization

In the third stage, we use deep learning models such as DNN to perform multi-dimensional fitting on multiple Alpha factors selected above:
- **Input**: Daily alpha values and historical stock prices;
- **Hidden Layer**: Activation functions like ReLU can be selected to enhance nonlinear fitting capability;
- **Output**: Predict next period returns and optimize network weights through backtest errors.
Finally, we obtain an optimal set of Alpha weights $\{w_i\}$, combining them into a dynamic and robust quantitative investment strategy.


![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2025/02/01/1738398665334-a4af048e-a5a3-4692-9c67-39591fe961e3.png)

## 4. Experiment

We primarily conduct empirical research within the scope of the SSE 50 Index to verify the following core questions:

1. **RQ1**: Can the framework effectively integrate multi-modal information and capture new Alpha under different market conditions?
2. **RQ2**: Compared to traditional Alpha generation or existing Alpha factories, is the LLM-driven mining method more effective in prediction?
3. **RQ3**: After integrating confidence scoring and adaptive strategies, can the overall performance consistently outperform market indices in live trading tests?

### 4.1 Dataset and Configuration

- **Data Coverage**: SSE 50 Index constituent stocks;  
- **Features**: Basic market data (OHLC, volume, VWAP) and company financial reports, etc.;  
- **Time Period**: Training set from 2021.01.01-2022.12.31, test set from 2023.01.01-2023.12.31;  
- **Evaluation Metrics**: Information Coefficient (IC), cumulative returns, drawdown, Sharpe ratio, etc.

### 4.2 Main Experimental Results

#### 4.2.1 RQ1: Multimodal and Dynamic Alpha Capture

- **Multimodal LLM Analysis**: Combines text (company announcements, news), numerical data (financial reports), and charts (K-lines, trading volume graphs) information to automatically obtain factors suitable for current market conditions across different time periods (e.g., 2021.12.31-2022.09.30 vs. 2022.10.01-2023.xx.xx);
- **Experimental Cases**:
  - **Case 1**: Selects momentum and volume factors, such as RSI, MACD, moving averages, etc.;
  - **Case 2**: Emphasizes volatility and economic factors, such as ATR, Bollinger Band width, gross profit, operating income ratio, etc.
  - Results show that the framework can flexibly select more relevant Alpha sets based on different market conditions.

#### 4.2.2 RQ2: Are LLM-mined Alphas More Predictive?

We use IC to measure the correlation between selected Alphas and actual future returns. Compared to existing "traditional Alpha factories," the LLM framework shows significantly improved average ICs in momentum, volatility, and fundamentals, indicating stronger predictive effectiveness.

#### 4.2.3 RQ3: Can Portfolio Strategy Outperform the Market

We selected the Top-k/Drop-n strategy, buying k stocks with the highest Alpha values daily while limiting portfolio rebalancing to no more than n stocks at a time.  
- **Backtesting Period**: 2023;  
- **Results**:  
  - Our framework achieved a cumulative return of **+53.17%**, while the SSE 50 Index declined by **-11.73%** during the same period, with other benchmark funds also significantly underperforming;  
  - The backtesting proves that this LLM-driven + confidence scoring + dynamic weight adjustment strategy can outperform the market during most market phases.

---

## 5. Related Work

1. **Formula-based Alpha**: Traditionally, Alpha factors are based on genetic programming, genetic algorithms, or machine learning models (such as XGBoost, LSTM), but lack dynamic adaptability in multi-modal information scenarios;  
2. **LLMs in Finance**: Although research on general-purpose large models is booming, their application in financial tasks (especially quantitative trading) is still in early exploration, with many studies focusing on financial text summarization or news sentiment analysis;  
3. **Multi-modal and Multi-agent**: Recent literature indicates that combining different forms of data such as text, images, and numerical data can significantly improve the ability to capture market sentiment and volatility. Additionally, using multi-agent collaborative decision-making can simulate different strategies and preferences, enhancing overall robustness.

---

## 6. Conclusion

This paper proposes a novel approach combining **Large Language Models** with **Multi-Agent Architecture** for quantitative stock investment and Alpha discovery. We generate and screen diversified Alpha factors from multimodal financial information using LLMs, then leverage the multi-agent structure to dynamically evaluate and adjust weights based on real-time market conditions, thereby maintaining high investment returns and strategy robustness across different market states. Empirical results show that this framework significantly outperforms traditional methods across multiple metrics in China's A-share market, establishing a new benchmark for AI-driven quantitative strategies.

> **Future Outlook**:  
> - Consider upgrading the multi-agent system to a Mixture of Experts model to improve learning efficiency;  
> - Incorporate financial knowledge graphs to enhance understanding of implicit information such as industry and company relationships;  
> - Extend applications to other time series prediction fields such as energy forecasting, anomaly detection, and healthcare, expanding the universality of the formulaic Alpha approach.

---

## References (Selected)

1. Fama, E.F. *Efficient capital markets: A review of theory and empirical work.* Journal of Finance, 1970.  
2. Cui, C., Wang, W., Zhang, M., et al. *Alphaevolve: A learning framework to discover novel alphas in quantitative investment.* SIGMOD, 2021.  
3. ...(see original text for more references)

For details, please refer to the appendix for the list of Alpha factors, datasets and experimental setup descriptions, as well as the LLM prompt templates and other details used.

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。欢迎加入**知识星球**获取**内部资料**。


![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/01/29/1738120164157-32d67f79-b006-4f4e-bb7b-13db27759e2b.JPG)