---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

**TradeMaster** is an open-source platform for quantitative trading (QT) that fully integrates **Reinforcement Learning (RL)** technology throughout the entire quantitative trading process. From data preparation, algorithm implementation, and evaluation to deployment, TradeMaster provides developers and researchers with a **"one-stop"** solution.

---

### I. Latest Updates

| Update Content | Status |
| --- | --- |
| Added FinAgent and EarnMore | 🔨 Updated October 29, 2024 |
| Updated Market Simulator | 🔨 Updated September 21, 2023 |
| Updated Market Dynamics Modeling Tool | 🔧 Updated July 7, 2023 |
| Added support for automatic feature generation and selection | 🔨 Tutorial updated May 11, 2023 |
| Released Python package | 🐳 Updated May 11, 2023 |
| Built TradeMaster website | 🐳 April 23, 2023 |
| Wrote software documentation | 💬 Updated April 11, 2023 |
| Released Colab version | 💬 Updated March 29, 2023 |
| Added Hong Kong stocks and futures datasets | 🧭 Updated March 27, 2023 |
| Added support for Alpha158 indicators | 🔨 Updated March 20, 2023 |
| Official release of TradeMaster 1.0.0 | March 5, 2023 |

---

### II. TradeMaster Overview

TradeMaster divides the quantitative trading workflow into 6 major modules:


![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/01/29/1738123026827-f604dec0-5a06-4fb4-b186-c296326e624a.png)


1. **Multi-modal Market Data**: Covers different financial assets and multiple frequencies;
2. **Complete Data Preprocessing Pipeline**: Automatic cleaning, feature generation, etc.;
3. **High-fidelity Market Simulator**: Includes various mainstream quantitative trading scenarios;
4. **13+ Reinforcement Learning Algorithm Implementations**: Significantly improves trading strategy efficiency;
5. **Systematic Evaluation Tools**: 6 dimensions, 17 measurement metrics to evaluate strategy performance;
6. **Diverse Interfaces**: Meets the needs of interdisciplinary users (research, engineering).

---

### III. Installation and Usage

#### 1. Installation Methods

- **Linux/Windows/MacOS**  
- **Docker**  

The official [Installation](#) guide provides detailed environment configuration instructions.

#### 2. Core Tutorials

TradeMaster comes with a series of "sample code" and **Colab online tutorials** covering the following scenarios:

| Algorithm | Dataset | Market | Task | Code |
| --- | --- | --- | --- | --- |
| EIIE | DJ 30 | US Stocks | Portfolio Management | [tutorial](#) |
| DeepScalper | BTC | Cryptocurrency | Intraday Trading | [tutorial](#) |
| SARL | DJ 30 | US Stocks | Portfolio Management | [tutorial](#) |
| PPO | SSE 50 | A-Shares | Portfolio Management | [tutorial](#) |
| ETEO | Bitcoin | Cryptocurrency | Order Execution | [tutorial](#) |
| Double DQN | Bitcoin | Cryptocurrency | High-Frequency Trading | [tutorial](#) |

---

### IV. Practical Scripts

TradeMaster comes with a rich set of script functionalities:

- **Automatic Hyperparameter Optimization**
- **Automatic Feature Generation**
- **Diffusion Model-Based Data Interpolation and Repair**
- **RL Training with Alpha158 Technical Indicators**
- **TradeMaster Sandbox Testing**

Additionally, it provides Market Dynamics modeling tools and corresponding website interfaces.

---

### 5. Datasets

The platform includes various common market datasets:

| Dataset | Source     | Type       | Range & Frequency     | Data Type | Link |
| ------- | ---------- | ---------- | -------------------- | -------- | ---- |
| S&P500  | Yahoo      | US Stocks  | 2000/01/01-2022/01/01, 1day | OHLCV  | [SP500](#) |
| DJ30    | Yahoo      | US Stocks  | 2012/01/01-2021/12/31, 1day | OHLCV  | [DJ30](#) |
| BTC     | Kaggle     | Forex      | 2000/01/01-2019/12/31, 1day | OHLCV  | [FX](#)   |
| Crypto  | Kaggle     | Cryptocurrency | 2013/04/29-2021/07/06, 1day | OHLCV  | [Crypto](#) |
| SSE50   | Yahoo      | A-Shares   | 2009/01/02-2021/01/01, 1day | OHLCV  | [SSE50](#) |
| Bitcoin | Binance    | Cryptocurrency | 2021/04/07-2021/04/19, 1min | LOB    | [Binance](#) |
| Future  | AKshare    | Futures    | 2023/03/07-2023/03/28, 5min | OHLCV  | [Future](#) |
| HS30    | AKShare    | Hong Kong Stocks | 1988/12/30-2023/03/27, 1day | OHLCV  | [HS30](#) |

Available for download from Google Drive or Baidu Cloud (access code: x24b).

---

### VI. Model Zoo

TradeMaster includes efficient implementations of various RL trading algorithms, including:

- **DeepScalper (CIKM 22)**
- **OPD (AAAI 21)**
- **DeepTrader (AAAI 21)**
- **SARL (AAAI 20)**
- **ETEO (20)**
- **Investor-Imitator (KDD 18)**
- **EIIE (17)**

As well as classic reinforcement learning algorithms based on PyTorch or Ray, such as PPO, A2C, Rainbow, SAC, DDPG, DQN, PG, TD3, etc.

---

### 7. Visualization Tools

TradeMaster provides numerous visualization tools for multi-dimensional evaluation of reinforcement learning quantitative strategies.  
> For example, the **PRIDE-Star** radar chart can intuitively display multiple metrics such as returns and Sharpe ratio, offering a single-view overview of a strategy's strengths and weaknesses.


![](https://fastly.jsdelivr.net/gh/bucketio/img2@main/2025/01/29/1738123100989-f58db4af-6048-40c1-aaf2-1b3adbe6e98c.png)

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/01/29/1738123086122-b3c91503-802d-4e17-b5c4-fda19faf4838.png)


For more details, please refer to the related [paper](#) and [repo](#).

## Related Papers

- **PRUDEX-Compass**: Systematic Evaluation of RL in Financial Markets (TMLR 2023)  
- **Reinforcement Learning for Quantitative Trading (Survey)** (ACM TIST 2023)  
- **Deep RL for Quantitative Trading: Challenges & Opportunities** (IEEE Intelligent Systems 2022)  
- **DeepScalper** (CIKM 2022)  
- **Commission Fee is not Enough** (AAAI 2021)  

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。欢迎加入**知识星球**获取**内部资料**。


![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/01/29/1738120164157-32d67f79-b006-4f4e-bb7b-13db27759e2b.JPG)