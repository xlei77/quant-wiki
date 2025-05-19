---
{}
---

Here is the English translation of the provided text, maintaining technical accuracy, formatting, and precision for financial documentation:

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Year-end Bonus! 48 Selected AI Quantitative Finance Papers for 2024 | With Key Insights

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

As a year-end bonus from LLMQuant, this summary includes a total of **41 papers** (selected and extended reading) covering **cutting-edge research** in quantitative finance. These papers span diverse topics from stocks, foreign exchange, commodities, fixed income and credit markets to portfolio optimization, market prediction, derivatives modeling, macroeconomic and geopolitical risk, as well as cryptocurrencies and DeFi. Notably, an increasing number of works are incorporating artificial intelligence (AI) and large language models (LLMs) into financial analysis and trading, not only improving the accuracy and efficiency of predictions and assessments but also providing new approaches for strategy formulation, investment decision-making, and risk management.

## Table of Contents

- Applications of Artificial Intelligence and Large Language Models in Finance and Trading

  1. Extending Core Earnings Measures Using Large Language Models
  2. Risk-Neutral Modeling of Interest Rate Curves Using Autoencoders
  3. Applications and Benchmarking of Large Language Models in Finance and Investment Management
  4. Discovering New Categories of Financial Price Jumps Using "Wavelet Riding"
  5. Modeling News Interactions and Impacts to Predict Financial Markets
  6. Leveraging Generative AI for Economic Insights
  7. Incorporating Machine Learning into the Markowitz Portfolio Selection Paradigm
  8. The "Cocktail Effect" of Multi-Task Fine-Tuning: A Case Study in Finance
  9. Inference of Missing and Real-Time Financial Data Using Spatio-Temporal Diffusion Models
  10. "Simulate and Optimize": Designing Novel Assistance Products with a Two-Layer Mortgage Simulator
  11. XGBoost Binary Classification Framework with Reduced Discriminatory Bias and Explainability

**New Developments in Portfolio Strategies and Market Prediction**

  12. Joint Estimation of Conditional Means and Covariances for Unbalanced Panel Data
  13. Dynamic Factor Allocation Using Regime Switching Signals
  14. Statistical Arbitrage in Ranking Space
  15. Mean-Variance and Mean-ETL Portfolio Selection Updates
  16. Extracting Alpha from Financial Analyst Networks
  17. Predicting Stock Premia at High Risk Levels and Prices of Risk
  18. Dynamic Portfolio Optimization Using Full-Time Domain Neural Networks

**Electronic Financial Markets and Limit Order Books (LOB)**

  19. Linear Strategies for Nonlinear Price Impact
  20. No Tick Too Small: A General Approach to Modeling Small-Tick Limit Order Books
  21. Multi-Task Dynamic Pricing in Credit Markets Using Contextual Information
  22. Do Maker-Taker Limit Order Rebates Improve Market Outcomes?
  23. Optimal Execution Under Deterministic Time-Varying Liquidity: Well-Posedness and Price Manipulation
  24. Simulation and Analysis of Sparse Order Books: Application to Intraday Electricity Markets
  25. The Impact of Liquidity on the Feasibility of Spoofing in Financial Markets
  26. Inventory, Market Making, and Liquidity in OTC Markets

**Financial Derivatives Modeling and Volatility Frontiers**

  27. Realized Volatility Forecasting Considering Spillover Effects: A Graph Neural Network Perspective
  28. Fast Deep Hedging with Second-Order Optimization
  29. Global Stock Market Volatility Prediction Based on Graph Signal Processing
  30. Hedging with Perpetual Derivatives: Trinomial Option Pricing and Implied Parameter Surface Analysis
  31. Modeling Monthly Average VIX Based on the Log Heston Model
  32. GARCH-Assisted Neural Networks for Financial Market Volatility Prediction

**New Trends in Financial Markets and Macroeconomics**

  33. Factors Driving Liquidity in China's Credit Bond Market
  34. AI and Big Data Holdings: New Opportunities for Central Banks
  35. GMM Estimation with Brownian Kernels and Income Inequality Measurement
  36. Taming the Curse of Dimensionality: Quantitative Economics Using Deep Learning
  37. Negative Mean Output Gaps and Symmetry Bias in Statistical Filters
  38. Stylized Facts of the Money Market: An Empirical Analysis of Euro Area Data
  39. A Minimalist Model of Money Creation Under Regulatory Constraints
  40. Can Competition Increase the Profits of Factor Investing?
  41. Margin Call Conditional Prediction Using Dynamic Graph Neural Networks
  42. Foundational Models for Value-at-Risk Time Series
  43. Bank Model Validation Practices: A Structured Approach

**Decentralized Finance (DeFi) Frontiers**

  44. Drivers of Liquidity in Decentralized Exchanges: Evidence from the Uniswap Protocol
  45. AgileRate: Bringing Adaptability and Robustness to DeFi Lending Markets

**Time Series Forecasting**

  46. XForecast: Evaluating Natural Language Explanations for Time Series Forecasting
  47. Interval Estimation for Multi-Step Time Series Forecasting Using Online Isotonic Inference

**Cutting-Edge Research Beyond the Selection**
  48. Crossing Boundaries: Research Beyond the Selected List

## Extending Core Earnings Measures Using Large Language Models

**Paper Information:**  
M Shaffer, CCY Wang, SSRN, 2024  
University of Southern California, Harvard Business School  
[Original Link](https://papers.ssrn.com)

**Research Results and Key Findings**

This study evaluates the effectiveness of large language models (LLMs) in measuring core earnings of companies through 10-K disclosure documents, finding significant improvements compared to traditional metrics.

- When using structured "sequential" prompts, LLM-generated core earnings metrics outperform GAAP net income and other common indicators in predicting future average earnings.
- Unlike unstructured "baseline" methods, the sequential approach accurately distinguishes between non-recurring and recurring earnings components, improving predictive effectiveness and reducing confusion with other financial concepts.
- LLM-based core earnings measures demonstrate high predictive power for long-term net income and strongly correlate with future market valuations, potentially significantly reducing the cost of financial information analysis.

Figure 2 shows distribution histograms of GAAP net income and two LLM core earnings estimates (all per share values).  

- Lazy Analyst Core Earnings/Share: Using the "Lazy Analyst" LLM prompt  
- Sequential Prompt Core Earnings/Share: Core earnings estimated using the sequential prompting method  
- GAAP Earnings (Net Income per Share)

## Risk-Neutral Modeling of Interest Rate Curves Using Autoencoders

**Paper Information:**  
A Lyashenko, F Mercurio, A Sokol, SSRN 4967989, 2024  
Quantitative Risk Management, Bloomberg, CompatibL  
[Original Link](https://papers.ssrn.com)

**Research Results and Key Findings**

This research uses autoencoders (AE) to model yield curves in a risk-neutral framework, preserving historical structure while ensuring arbitrage-free dynamics.

- Autoencoders provide a low-dimensional representation of yield curves, achieving historical consistency and efficient calibration to market prices.  
- The study proposes a method to deviate from the AE manifold through convexity adjustments, ensuring arbitrage-free evolution of forward interest rate curves.  
- Numerical results show excellent performance in multi-currency interest rate swap data, improving the accuracy of curve representation and hedging stability.

Here is the English translation of the provided text, maintaining technical accuracy, formatting, and precision for financial documentation:

Figure 1: Shows static arbitrage-free trajectories (blue) and the generating manifold ring MXY under three choices of δ=0.1, 0.2, 0.3.

## Applications and Benchmarks of Large Language Models in Finance and Investment Management

**Authors:**  
Kong Y, Nie Y, Dong X, Mulvey JM, Poor HV, Wen Q, Zohren S  
(University of Oxford, Princeton University, Squirrel AI)

**Research Findings and Key Insights**

- LLM-based multi-agent systems enhance capabilities in automated trading, corporate strategic planning, and market sentiment analysis through collaborative specialized agents and self-reflective reasoning frameworks.  
- Introduction of comprehensive benchmarks such as FLUE and PIXIU establishes robust standards for evaluating LLMs in financial NLP tasks (e.g., financial forecasting, named entity recognition, sentiment analysis).  
- Language-specific benchmarks emphasize customized evaluation in different linguistic environments to improve the adaptability and effectiveness of financial LLMs in global markets, while addressing challenges of data privacy and computational costs.

The paper emphasizes the transformative applications of LLMs in trading, corporate planning, financial sentiment analysis, and the importance of their evaluation benchmarks.

**(Page 10/65)**

---

## Discovering New Categories of Financial Price Jumps Using the "Wavelet Riding" Method

**Authors:**  
C Aubrun, R Morel, M Benzaquen, JP Bouchaud, 2024  
(CNRS, Capital Fund Management, École Polytechnique, ENS)

**Research Findings and Key Insights**

This study proposes a novel unsupervised classification method using multi-scale wavelet representation to distinguish different types of financial price jumps and co-jumps, providing new insights into their endogenous or exogenous nature.

- Time asymmetry of volatility is the main characteristic distinguishing endogenous from exogenous price jumps: endogenous jumps are more symmetric, while exogenous jumps exhibit stronger volatility in the late jump phase.  
- The study identifies new categories of price jumps with local mean reversion and trend alignment features (such as "mean-reverting" and "trend-aligning" jumps).  
- Analysis shows that most large-scale co-jump events are driven by endogenous contagion mechanisms rather than exogenous news, emphasizing the intrinsic interconnectedness and reflexivity of market dynamics.

The attached figure shows the distribution of co-jumps for 295 US stocks over an 8-year period. The x-axis represents dates, the y-axis shows the time of jump occurrences, and each circle represents the number and scale of co-jumps occurring within a 1-minute interval, with larger, warmer-colored circles indicating more stocks jumping simultaneously. The study highlights a concentration of co-jump events around October 2019, emphasizing periods of peak market activity and contagion effects.

## Modeling News Interactions and Impacts for Financial Market Prediction

**Authors:**  
M Wang, SB Cohen, T Ma - arXiv:2410.10614 (2024)  
The University of Edinburgh

**Research Findings and Key Insights**

The FININ model outperforms existing methods in market prediction by integrating news interactions with market data.

- FININ improves daily average Sharpe ratios for S&P 500 and NASDAQ 100 to 0.429 and 0.341 respectively, demonstrating the effectiveness of integrating news and market data.  
- The study reveals delayed effects of news on market pricing, long memory effects in news, limitations of pure sentiment analysis, and the importance of comprehensive news analysis.  
- The model is tested on over 15 years of data, encompassing more than 2.7 million news articles, using a data fusion encoder and market-aware impact quantifier.

Figure 2 illustrates the FININ model structure, including the data fusion encoder and market-aware impact quantifier, which integrate market and news features through multi-layer attention, MLP, and other modules to output market insights.

## Leveraging Generative AI for Economic Insights

**Authors:**  
M Jha, J Qian, M Weber, B Yang - arXiv:2410.03897 (2024)  
University of Chicago, Booth School of Business, Georgia State University

**Research Findings and Key Insights**

The study introduces an AI-based economic index (AI Economy Score) derived from management expectations, which effectively predicts future economic indicators and outperforms existing measures.

- The AI Economy Score significantly predicts economic indicators such as GDP growth, output, and employment.  
- Compared to existing indicators like survey forecasts, this index shows advantages in long-term prediction and micro-level analysis.  
- Its long-term predictability and micro-level insights are validated using a vector autoregression framework, offering practical value to policymakers, researchers, and investors.

The figure compares the AI Economy Score with actual GDP growth and SPF forecasts from 2007Q1 to 2023Q1, using dual axes to contrast the index with GDP indicators, revealing their dynamic relationship over time.

## Incorporating Machine Learning into the Markowitz Portfolio Selection Paradigm

**Authors:**  
M López de Prado, J Simonian, FA Fabozzi - Annals of Operations Research (2024)  
Stevens Institute of Technology, Cornell University

**Research Findings and Key Insights**

The study demonstrates that Deep Q-Network (DQN) strategies significantly outperform traditional methods in multi-asset portfolios, achieving higher returns and lower risks.

- DQN strategies yield 30% higher profits compared to 10 traditional portfolio management strategies, with better performance in Sharpe ratio and maximum drawdown.  
- The authors adapt DQN to the discrete action space of multi-asset portfolios, combining CNN and dual Q-network methods to propose a discretization approach for market behavior.  
- Tested on historical price data of 5 low-correlation US stocks, the DQN strategy continuously optimizes future cumulative returns within a reinforcement learning framework, showing superior performance.

Figure 5 shows the cumulative return curves of different strategies during the test period from 2017/01/05 to 2017/11/17. The DQN strategy outperforms benchmark strategies for most of the test period, particularly demonstrating strong advantages in the middle and later stages.

**(Page 14/65)**

---

## The "Cocktail Effect" of Multi-Task Fine-Tuning Enhances LLM Performance — A Financial Case Study

**Authors:**  
M Brief, O Ovadia, G Shenderovitz, NB Yoash - arXiv:2024  
Microsoft, Tel Aviv University

**Research Findings and Key Insights**

Multi-task fine-tuning significantly improves LLM performance on financial tasks, enabling smaller models to surpass larger models through task integration.

- The study shows that through multi-task fine-tuning, the smaller Phi-3-Mini model can outperform the larger GPT-4-o model on financial benchmarks.  
- Empirically validates the "cocktail effect," where training on multiple related tasks synergistically enhances model performance.  
- Introduces general instruction data as regularization, utilizes mathematical data to improve numerical reasoning, and verifies interaction effects between datasets through systematic exploration of 220 models.

Figure 1 compares the performance of GPT-4-o, baseline Phi-3-Mini models, and the best multi-task fine-tuned Phi-3-Mini on financial tasks (Twitter sentiment analysis, topic analysis, FinNerCLS, FPB tasks, FinQA, ConvFinQA, Headline). Bar charts for each task show significant improvements in performance through multi-task fine-tuning.

**(Page 15/65)**

---

## Inference of Missing and Real-Time Financial Data Based on Spatiotemporal Diffusion Models

**Authors:**  
Y Fang, R Liu, H Huang, P Zhao, Q Wu - ACM (2024)  
City University of Hong Kong, Brunel University London

**Research Findings and Key Insights**

Here is the English translation of the provided text, maintaining technical accuracy and formatting:

This study proposes an innovative approach using the Spatio-Temporal Diffusion Model (STDM) for financial data imputation, effectively capturing spatio-temporal correlations and improving imputation accuracy.

- Key contributions include feature-specific projection, cross-sectional graph convolution, and implicit samplers, reducing computational memory usage while maintaining high accuracy.  
- Outperforms existing methods on the OSAP dataset, with model effectiveness validated through ablation experiments and factor portfolio construction.  
- Emphasizes the importance of capturing spatial and temporal dependencies for financial data imputation and real-time analysis.

Figure 1 shows the predictor architecture of STDM, including multiple residual blocks and feature mappings, extracting spatio-temporal dependencies through feature-specific projection, temporal attention, and cross-sectional graph convolution.

**(Page 16/65)**

---

## "Simulation and Optimization": Designing Novel Assistance Products with a Two-Layer Mortgage Simulator

**Authors:**  
L Ardon, BP Evans, D Garg, AL Narayanan - arXiv:2024  
J.P. Morgan AI Research, University of Sydney

**Research Findings and Key Points**

The study develops an innovative two-layer simulation method for optimizing mortgage assistance products, enhancing household resilience to financial shocks, and assisting policymakers.

- Authors extend agent-based models to enable counterfactual analysis and policy learning based on product conditions, proposing a general parameterized financial product configuration method.  
- The methodology includes an inner layer for household behavior simulation and an outer layer for product design optimization, calibrated using demographic data.  
- Adaptive simulation can identify favorable configurations, reduce default rates, and improve social welfare, providing scalable, low-cost tools for policymakers and financial institutions.

Figure 1 illustrates the structure of this two-layer optimization method: outer layer product design and inner layer simulation. The inner layer optimizes household strategies and product allocation parameters given outer layer decisions, forming an adaptive closed loop.

**(Page 17/65)**

---

## Reduced Discriminatory Bias and Interpretable XGBoost Binary Classification Framework

**Authors:**  
A Pangia, A Sudjianto, A Zhang, T Khan - arXiv:2410.19067 (2024)  
Wells Fargo, University of North Carolina at Charlotte

**Research Findings and Key Points**

The LDA-XGB1 framework incorporates fairness constraints into XGBoost, offering a new approach for financial credit models to balance accuracy and fairness.

- LDA-XGB1 incorporates fairness constraints and monotonicity into XGBoost, reducing bias against protected groups while maintaining interpretability compared to traditional fair credit models.  
- Authors propose a dual-objective optimization method using binning and Information Value (IV), introducing "Less Discriminatory Alternative" (LDA) and "Fair Information Value" (FIV) to reduce disparate impact.  
- Tested on simulated and real data, LDA-XGB1 achieves a trade-off between fairness and accuracy, meeting regulatory requirements and providing a powerful tool for financial institutions.

The attached figure shows a bar chart of feature importance in the monotonic XGB1 model, where the Mortgage feature dominates among Inquiry, Balance, Utilization, Amount Past Due, Delinquency, and Open Trade.

**(Page 18/65)**

---

## Joint Estimation of Conditional Mean and Covariance for Unbalanced Panels

**Authors:**  
D Filipovic, P Schneider - arXiv:2410.21858 (2024)  
EPFL, Swiss Finance Institute

**Research Findings and Key Points**

The study proposes a nonparametric model for simultaneously estimating conditional mean and covariance of unbalanced panel data, outperforming traditional models in empirical asset pricing.

- The model offers consistency and finite sample guarantees while maintaining positive definiteness and symmetry of the covariance matrix.  
- On U.S. stock data from 1962-2021, the method shows significant out-of-sample Sharpe ratio improvements, with notable enhancements over constant covariance models.  
- Utilizes convex optimization, low-rank approximation, and Nystrom method to achieve computational efficiency for large-scale empirical analysis.

The figure compares out-of-sample predictive R² performance using cosine and Gaussian kernels in four line graphs. Analysis of unbalanced U.S. stock excess returns data from 1962 to 2021 for m=5, 10, 20, 40, with shaded areas indicating major market crash periods.

**(Page 19/65)**

---

## Dynamic Factor Allocation Using Regime Switching Signals

**Authors:**  
Y Shu, JM Mulvey - arXiv:2410.14841 (2024)  
Princeton University

**Research Findings and Key Points**

Using a Sparse Jump Model to identify market regimes can improve factor allocation performance, providing a powerful method for dynamic asset allocation.

- Utilizes Sparse Jump Model to identify market states, achieving positive Sharpe ratios for all factors with low inter-factor correlations.  
- Incorporates regime inference into the Black-Litterman framework, resulting in dynamic allocation strategies outperforming static benchmarks in information ratio and maximum drawdown.  
- Tested on seven U.S. equity factors, proposing a novel factor regime analysis method using historical data and market environment characteristics, distinct from traditional factor timing strategies.

The figure shows the cumulative excess return curve for the Value Factor from 2012 to 2024, using the Sparse Jump model to identify bull (green) and bear (red) states, with the blue line representing cumulative performance.

**(Page 20/65)**

---

## Statistical Arbitrage in Rank Space

**Authors:**  
YF Li, G Papanicolaou - arXiv:2410.06568 (2024)  
Stanford University

**Research Findings and Key Points**

Applying neural networks for statistical arbitrage in rank space significantly improves returns and Sharpe ratios compared to traditional methods.

- Proposes a framework for statistical arbitrage in rank space, achieving an average annual return of 35.68% and a Sharpe ratio of 3.28 from 2007 to 2022 using intraday rebalancing and neural network optimization.  
- Compared to traditional name space, rank space exhibits a more stable market structure driven by a single factor and stronger mean-reversion characteristics.  
- Utilizes U.S. stock data, Principal Component Analysis (PCA) decomposition, and neural network portfolio optimization, with rank space neural network strategies outperforming parametric models.

The figure compares market structure differences between name space and rank space in multiple subplots, including market capitalization proportions, principal eigenvalues of correlation matrices, and empirical probability distributions of eigenvalue spectra.

**(Page 21/65)**

---

## Updated Research on Mean-Variance and Mean-ETL Optimization in Portfolio Selection

**Authors:**  
BP Shao, JB Guerard Jr, G Xu - Annals of Operations Research (2024)  
Tudor Investment Corporation

**Research Findings and Key Points**

Using composite variables from analyst forecasts for robust regression and portfolio optimization can achieve significant active returns even after considering transaction costs.

- Integrating analyst forecasts, revisions, and their directions into composite variables and incorporating them into robust regression models achieves significant active returns in portfolios.  
- Mean-variance and mean-ETL optimizations statistically significantly produce active returns, remaining reliable through data mining corrections.  
- Employs time series models with multivariate normal fat-tailed distribution innovations and Beaton-Tukey weighted regression techniques to handle outliers, enhancing return potential in practical scenarios.

Here is the English translation of the text, maintaining technical accuracy and formatting:

This paper updates the research results on the application of MV and ETL optimization in portfolio selection, emphasizing the effectiveness of robust regression models.

**(Page 22/65)**

---

## Extracting Alpha from Financial Analyst Networks

**Authors:**  
D Gorduza, Y Kong, X Dong, S Zohren - arXiv:2410.20597 (2024)  
University of Oxford

**Research Findings and Key Points**

Applying Graph Attention Networks (GAT) to analyst coverage networks significantly improves trading strategy performance, capturing complex inter-company relationships.

- Using GAT models on analyst coverage networks significantly improves trading strategy annualized returns (29.44%) and Sharpe ratios (4.06), outperforming traditional methods.  
- GAT captures complex non-linear relationships between companies by simultaneously analyzing company characteristics and network structure, predicting stock performance and formulating flexible adaptive trading strategies.  
- Data spans 2006-2022, using stock prices and analyst estimates to construct networks, with edges representing stocks co-covered by analysts, realizing the potential of graph machine learning in financial markets.

The figure shows the GAT trading model pipeline, starting from stock prices, feature matrices, analyst coverage, and adjacency matrices, processing through GAT to output future return predictions.

**(Page 23/65)**

---

## Predicting the Equity Premium Using High Threshold Risk Levels and Risk Prices

**Authors:**  
N Bansal, C Stivers - Financial Management (2024)  
University of Louisville

**Research Findings and Key Points**

The study shows that using VIX and sentiment indices can effectively predict US equity premiums, demonstrating robust predictive power across different market environments.

- When market sentiment is high (low-risk periods), equity premiums decrease; when VIX exceeds the 80%-85% percentile (high-risk periods), premiums increase significantly.  
- At 6-month and 12-month prediction horizons, adjusted R² reaches 19% and 29% respectively, showing robust predictive power across time periods and market conditions.  
- Using data from 1990-2023 for in-sample and out-of-sample tests, with control variables, a refined understanding of market dynamics can improve the accuracy of financial forecasting and risk assessment.

This study focuses on the impact of VIX and sentiment on equity risk premiums, showing that when VIX is high, the market's risk premium rises significantly, providing reference for investor risk assessment and policy-making.

**(Page 24/65)**

---

## Dynamic Portfolio Optimization Using Global-in-Time Neural Networks

**Authors:**  
PM van Staden, PA Forsyth, Y Li - Applied Mathematical Finance (2024)  
University of Waterloo

**Research Findings and Key Points**

This study proposes a global-in-time neural network model for dynamic portfolio optimization that does not require dynamic programming, outperforming traditional methods.

- A neural network model without traditional dynamic programming provides a more flexible and efficient optimization method for complex financial problems.  
- Introduces novel methods and terminology, using advanced neural network structures and market simulations to demonstrate that neural networks can handle complexities in portfolio optimization.  
- The model outperforms traditional schemes in simulation results, providing new research directions for financial optimization problems.

This paper provides an innovative neural network approach to dynamic portfolio optimization, avoiding the limitations of dynamic programming and opening new paths for financial optimization.

**(Page 25/65)**

---

## Linear Strategies for Nonlinear Price Impact

**Authors:**  
Brokmann X, Itkin D, Muhle-Karbe J, Schmidt P  
Mathematical Finance (2024)  
Qube Research and Technologies, Imperial College London, LSE

**Research Findings and Key Points**

The study shows that linear trading strategies optimized for quadratic costs can approach optimal performance for nonlinear price impacts by adjusting effective cost parameters.

- Linear strategies optimized for nonlinear price impacts have performance losses below 2%, applicable across a wide range of risk levels.  
- Adapting effective quadratic cost parameters to the concavity of price impacts allows linear strategies to perform close to complex numerical algorithms but with lower computational burden.  
- The method achieves near-optimal performance in markets with nonlinear impacts without requiring advanced numerical solutions, providing practical approaches for real trading.

The figure shows annualized P&L curves, with the optimized linear strategy curve very close to the highly complex Kolm-Ritter Viterbi algorithm, demonstrating the effectiveness of the adjusted linear strategy.

**(Page 26/65)**

---

## No Tick Is Too Small: A Universal Approach to Modeling Small-Tick Limit Order Books

**Authors:**  
K Jain, JF Muzy, J Kochems, E Bacry - arXiv:2410.08744 (2024)  
University College London, University of Oxford

**Research Findings and Key Points**

The research proposes a universal Hawkes Process model to simulate limit order book dynamics across different tick sizes, revealing significant characteristic differences among large, medium, and small-tick stocks.

- Using high-frequency LOB data, 15 stocks are classified (large, medium, small tick) to analyze key characteristics of bid-ask spreads, price movements, and liquidity distribution.  
- Proposes a universal Hawkes process model capable of simulating order book dynamics for small-tick stocks, validating its universality through simulations across different assets.  
- The study provides new methods for addressing the challenges of modeling small-tick stocks, pointing directions for future research on LOB dynamics.

The figure shows a log-log plot of average bid-ask spreads versus relative tick size, with different stocks (large tick and medium/small tick) exhibiting different slopes and linear relationships.

**(Page 27/65)**

---

## Multi-Task Dynamic Pricing in Credit Markets with Contextual Information

**Authors:**  
A Javanmard, J Ji, R Xu - arXiv:2410.14839 (2024)  
NYU, USC

**Research Findings and Key Points**

The TSMT algorithm improves financial pricing accuracy by leveraging structural similarities between securities, outperforming individual or pooled pricing strategies.

- In a piecewise experimental setting, the TSMT algorithm achieves superior performance in a linear contextual model of competitor pricing by utilizing similarities between securities.  
- Maximum likelihood method is used for parameter estimation, effectively addressing data sparsity and censored feedback issues.  
- Experiments on synthetic and real data (including US corporate bond pricing) show TSMT can adapt to similar structures across different securities and heterogeneous conditions, achieving lower regret.

The figure shows the regret comparison of TSMT strategy relative to individual learning and pooled strategies under different problem configurations, with TSMT performing excellently under moderate similarity conditions.

**(Page 28/65)**

---

## Do Maker-Taker Limit Order Rebates Improve Market Outcomes? Evidence from a Quasi-Natural Experiment

**Authors:**  
Y Lin, PL Swan, FHB Harris - Journal of Banking & Finance (2024)  
UNSW, Wake Forest University

**Research Findings and Key Points**

The study shows that Maker-Taker rebates improve market efficiency but increase trading costs. When rebates are removed, market quality deteriorates, affecting market behavior.

Here is the English translation of the provided text, maintaining technical accuracy and formatting:

- Maker-Taker rebates increase market depth and efficiency, but also extend limit order queues and increase trading costs.
- NASDAQ fee pilot shows that removing rebates reduced market share and worsened market quality, refuting the "washout theory".
- By integrating regulatory frameworks, emphasizing raw price data without fees, and using proprietary NASDAQ data with difference-in-differences analysis, the impact of fee structures on market microstructure is revealed.

Figure B shows a comparison of NASDAQ's price impact over 5-second intervals, annotating the time series comparison of price effects when rebates were reduced and restored.

**(Page 29/65)**

---

## Optimal Execution under Time-Varying Liquidity: Well-Posedness and Price Manipulation Issues

**Authors:**  
G Palmari, F Lillo, Z Eisler - arXiv:2410.04867 (2024)  
Imperial College London, University of Bologna

**Research Results and Key Findings**

The study shows that the optimal execution problem under time-varying liquidity conditions has well-posed solutions and avoids price manipulation under certain conditions.

- Defines strong and weak well-posedness conditions, using B-matrix theory to ensure non-negative trading costs.
- Proposes new conditions to avoid trade-induced price manipulation, proving the robustness of the Almgren-Chriss model under time-dependent impact.
- Validates theoretical results using variational methods and numerical simulations, emphasizing the importance of controlling liquidity change rates to maintain well-posedness, providing reference for practical trading strategies.

Figure 1 shows the intraday temporary and permanent impact dynamics for Microsoft stock in June 2021, as well as the permanent impact changes on June 10, 2021, providing empirical context.

**(Page 30/65)**

---

## Simulation and Analysis of Sparse Order Books: Application to Intraday Electricity Markets

**Authors:**  
P Bergault, E Cognéville - arXiv:2410.06839 (2024)  
Université Paris Dauphine-PSL, EDF R&D

**Research Results and Key Findings**

The study uses a non-homogeneous Poisson process model to simulate order flow in low-liquidity markets, providing a more realistic characterization of LOB dynamics.

- Applied to European intraday electricity markets, analyzing EPEX Spot data (Germany, France), focusing on hourly delivery periods.
- Simulations show sporadic nature of order arrivals and cancellations, increased spreads and price volatility as markets approach delivery points, consistent with empirical behavior.
- While unable to fully capture extreme events, the model provides a reference basis for order book modeling in low-liquidity markets.

Figure 1 shows the intraday mid-price evolution curves for different products on a trading day, January 7, 2021. Figure 2 shows the average change in market interaction intensity at different times for products in January 2021.

**(Page 31/65)**

---

## The Impact of Liquidity on the Feasibility of "Spoofing" in Financial Markets

**Authors:**  
A Gu, Y Wang, C Mascioli, M Chakraborty, R Savani - 2024  
University of Michigan, University of Liverpool

**Research Results and Key Findings**

High market liquidity reduces the effectiveness of "spoofing", indicating that maintaining sufficient liquidity helps resist market manipulation.

- Develops advanced spoofing strategies using reinforcement learning and parameter optimization, achieving higher profitability and impact in agent models compared to existing methods.
- Identifies two spoofing behavior patterns: high-liquidity markets require multiple entries for low-profit, high-frequency transactions; low-liquidity markets favor high-profit, low-frequency strategies.
- Suggests regulatory bodies can naturally weaken spoofing behavior by increasing market liquidity.

Figure 2 compares the surplus impact of spoofing on strategy agents and background traders (HBL, ZI) across different market configurations (A1,A2,A3,B1,B2,B3,C1,C2,C3), comparing baseline with R-Learned and Tuned strategies.

**(Page 32/65)**

---

## Inventory, Market Making, and Liquidity in OTC Markets

**Authors:**  
A Cohen, M Kargar, B Lester, PO Weill - Journal of Economic Theory (2024)  
Federal Reserve Bank of Philadelphia, UCLA

**Research Results and Key Findings**

The study models market makers' inventory costs and regulatory impacts through a search theory framework, exploring liquidity and welfare effects in OTC markets.

- Market makers in OTC markets need to hold inventory to facilitate trades, affecting liquidity indicators such as bid-ask spreads and trading volumes.
- Uses a calibrated model to analyze post-crisis era regulations and their impact on dealer behavior and market welfare, emphasizing the key role of inventory costs on liquidity.
- The study assumes dealers can only sell assets they own, showing that regulations increasing inventory costs reduce liquidity and welfare.

The figure compares the target asset holdings q*() under conditions with and without inventory constraints (CKLW vs LR).

**(Page 33/65)**

---

## Realized Volatility Forecasting with Spillover Effects: A Graph Neural Network Perspective

**Authors:**  
C Zhang, X Pu, M Cucuringu, X Dong - International Journal of Forecasting (2024)  
Oxford-Man Institute, Alan Turing Institute, HKUST(GZ)

**Research Results and Key Findings**

Predicts multivariate realized volatility using Graph Neural Networks (GNN), incorporating spillover effects into the model, significantly improving prediction accuracy.

- Considering spillover effects from multi-hop neighbors does not consistently improve prediction accuracy; direct neighbor information is often sufficient to enhance performance.
- GNN-based nonlinear spillover effect modeling performs better in short-term (intra-week) volatility prediction.
- Training with likelihood-like loss functions improves handling of heteroscedasticity, outperforming traditional HAR models.

The figure uses IBM as an example to illustrate volatility diffusion paths to other stocks through network structure (0-hop, 1-hop, 2-hop neighbors), emphasizing comparisons between direct and multi-level propagation effects.

**(Page 34/65)**

---

## Accelerating Deep Hedging with Second-Order Optimization

**Authors:**  
K Mueller, A Akkari, L Gonon, B Wood - arXiv:2410.22568 (2024)  
Imperial College London, J.P. Morgan

**Research Results and Key Findings**

A new second-order optimization method (KFAC) accelerates deep hedging training by 75%, converging faster in high-curvature loss regions and improving hedging performance.

- Implements a second-order optimization scheme using KFAC with shrinkage-type damping, accelerating neural network training, reducing optimization steps by 75% compared to Adam.
- Introduces dynamically evolving hedging operation spaces, validated on cliquet option hedging under stochastic volatility models.
- Experiments show option hedging is crucial; second-order optimization methods perform better in high-curvature loss regions, converging quickly and improving hedging performance.

Figure 1 illustrates the randomness of implied volatility surfaces in a floating grid and the available positions of call/put options.

**(Page 35/65)**

---

## Global Stock Market Volatility Prediction Based on Graph Signal Processing

**Authors:**  
Z Chi, J Gao, C Wang - arXiv:2410.22706 (2024)  
The University of Sydney

**Research Results and Key Findings**

Here is the English translation of the provided text, maintaining technical accuracy and formatting:

Fusion of Graph Signal Processing (GSP) and Heterogeneous Autoregression (HAR) models (GSPHAR) to improve multi-market volatility prediction through graph Fourier transform and convolutional filtering.

- Construct a volatility spillover network of 24 global stock indices based on spectral graph theory and magnetic Laplacian, capturing complex inter-market correlations.  
- GSPHAR introduces learnable convolutional filters to aggregate past information more dynamically, exhibiting more flexible decay patterns.  
- Compared to traditional HAR models, GSPHAR performs better in short, medium, and long-term prediction tasks, emphasizing the importance of directional and nonlinear spillover effects.

The model architecture diagram shows the process from input multivariate RV time series to magnetic Laplacian decomposition, graph Fourier transform, convolutional filtering, and final prediction output.

**(Page 36/65)**

---

## Hedging with Perpetual Derivatives: Trinomial Option Pricing and Implied Parameter Surface Analysis

**Authors:**  
J Gnawali, WB Lindquist, ST Rachev - arXiv:2410.04748 (2024)  
Texas Tech University

**Research Results and Key Findings**

The study proposes a pricing method using trinomial tree models and multi-asset portfolio analysis that can simultaneously estimate risk-neutral and real-world parameters.

- Derive risk-neutral dynamics using replicating portfolios and calibrate real-world parameters through hypothesis testing.  
- Introduce new methods to calibrate price movement probabilities and calculate implied parameter surfaces, including volatility, mean, risk-free rate, and probability distribution parameters.  
- In analyzing tech giant stock data, the study constructs trinomial tree models and empirically demonstrates market expectations for future stock performance, bridging the gap between risk-neutral and real-world parameters.

Figure 1 shows the basic trinomial tree structure with indexing examples for time step k and level i.

**(Page 37/65)**

---

## Modeling Monthly Average VIX Based on Log Heston Model

**Authors:**  
J Park, A Sarantsev - arXiv:2410.22471 (2024)  
University of Michigan, University of Nevada, Reno

**Research Results and Key Findings**

By taking the logarithm of VIX and applying the Heston model (Log Heston model), monthly stock index returns, when standardized, become closer to Gaussian i.i.d., improving the modeling accuracy of volatility and returns.

- When monthly stock index returns Rt are standardized as Rt/VIXt, their distribution becomes closer to Gaussian i.i.d., reducing skewness and kurtosis.  
- The Log Heston model applies AR(1) modeling to log(VIXt), fitting better than the original Heston model.  
- Data covers 1986 to 2024, with residuals showing non-Gaussian distribution; variance-gamma distribution fits the innovations better.

The figure shows a comparison of VIX time series and standardized returns from 1986 to June 2024, with VIX fluctuating between 10 and 60, and small price returns fluctuating around zero.

**(Page 38/65)**

---

## GARCH-Assisted Neural Networks for Financial Market Volatility Prediction

**Authors:**  
Z Xu, J Liechty, S Benthall, N Skar-Gislinge - arXiv:2024  
Carnegie Mellon University, NYU

**Research Results and Key Findings**

GARCH-Informed Neural Networks (GINN) combine the strengths of GARCH patterns and LSTM in volatility prediction, outperforming traditional models in accuracy and generalization.

- Incorporate GARCH empirical rules into LSTM neural networks, balancing model accuracy and generalization ability.  
- GINN and its variant GINN-0 outperform traditional GARCH and GAS models in predicting global multi-market index data.  
- By adding GARCH predictions as a regularization term in the loss function, GINN models capture both short-term and long-term market characteristics, reducing overfitting.

Figure 4 illustrates the variance prediction process of the GINN model, showing the relationships between Log Return, AR+GARCH, GINN, and true variance, using MSE to measure the difference between GINN and GARCH predictions.

**(Page 39/65)**

---

## Factors Driving Liquidity in China's Credit Bond Market

**Authors:**  
J Mo, MG Subrahmanyam - The Journal of Finance and Data Science (2024)  
NYU, NYU Shanghai

**Research Results and Key Findings**

Analysis of China's credit bond market from 2010-2019 reveals significant differences in liquidity effects across markets and products, influenced by policy interventions and macroeconomic conditions.

- Using principal component analysis to measure liquidity, finds stronger liquidity effects in exchange markets compared to other markets.  
- Bond risk and macroeconomic channels significantly impact liquidity, while company information channels have relatively weak effects.  
- Counterfactual analysis around policy shocks shows changes in liquidity levels and pricing methods, highlighting the impact of market segmentation, regulatory changes, and macro conditions on liquidity.

The figure shows monthly aggregate liquidity levels (represented by the first principal component of 5 illiquidity proxies) for four types of credit bonds (enterprise bonds, medium-term notes, exchange-traded corporate bonds, and corporate bonds).

**(Page 40/65)**

---

## Artificial Intelligence and Large-Scale Holdings Data: Central Bank Opportunities

**Authors:**  
X Gabaix, RSJ Koijen, R Richmond, M Yogo - 2024 - bis.org  
Harvard, NYU Stern

**Research Results and Key Findings**

Utilizing asset demand systems combined with AI and large holdings data can provide central banks with deeper insights into financial stability and policy interventions.

- Introduce AI-driven embeddings and large-scale holdings data to measure asset and investor similarities, improving the precision of asset demand systems.  
- Helps central banks understand financial contagion, asset price fluctuations, and the impact of unconventional monetary policies, and optimize climate stress tests and foreign exchange reserve management.  
- Using advanced econometric tools and high-quality portfolio data, the study emphasizes the inelastic characteristics of investor demand, challenging traditional financial models.

This BIS paper explores the role of AI and big data in central bank policy, asset pricing, and financial stability.

**(Page 41/65)**

---

## GMM Estimation with Brownian Kernels and Income Inequality Measures

**Authors:**  
JS Cho, PCB Phillips - 2024  
Yale University, Yonsei University

**Research Results and Key Findings**

This study introduces Brownian motion and Brownian bridge kernels into infinite-dimensional GMM estimation for income inequality analysis, proposing a new U-test.

- Introduce BM-GMM and BB-GMM methods to handle infinite-dimensional GMM estimation problems, and propose a U-test to complement the traditional J-test.  
- Analysis using the Continuous Work History Sample database shows that labor income inequality peaks early in careers, suggesting early intervention policies to reduce inequality.  
- The method expands the ability to handle high-dimensional moment conditions, emphasizing overall computational robustness and robust inference under distributional assumptions.

This study provides new econometric methods for measuring income inequality and demonstrates their policy implications.

**(Page 42/65)**

---

## Taming the Curse of Dimensionality: Deep Learning for Quantitative Economics

**Authors:**  
J Fernández-Villaverde, G Nuño, J Perla - 2024 - nber.org

**Research Results and Key Findings**

Deep neural networks can overcome the curse of dimensionality in solving high-dimensional dynamic equilibrium models, improving computational efficiency in economics.

Here is the English translation of the provided text, maintaining technical accuracy, formatting, and precision for financial documentation:

- Deep learning methods outperform traditional numerical methods in solving complex dynamic equilibrium models such as high-dimensional stochastic neoclassical growth models.
- Neural networks generalize new function approximation forms from existing economic methods, providing new perspectives for applications in macroeconomics, finance, and game theory.
- Using simulated data to train neural networks to approximate policy functions and equilibrium conditions provides a feasible path for solving high-dimensional economic problems that were difficult to handle in the past.

This research shows that deep neural networks can change the research paradigm of quantitative economics and expand the scope of applicable research.

**(Page 43/65)**

---

## Negative Mean Output Gaps and the Symmetry Bias of Statistical Filters

**Authors:**  
S Aiyar, S Voigts - IMF Economic Review (2024)  
IMF, Johns Hopkins University

**Research Findings and Key Points**

The symmetry bias causes standard filters to underestimate potential output during deep recessions, leading to weaker policy responses and increased output losses.

- Standard statistical filters assume zero-mean output gaps, which leads to underestimation of potential output during deep recessions when this assumption is biased.
- Using New Keynesian model simulations, it is found that downward wage rigidity exacerbates employment declines during recessions, and symmetry bias causes policymakers to tighten policy prematurely.
- In the deepest 25% of recessions, symmetry bias leads to an additional one-third increase in output losses, emphasizing the importance of more accurate output gap measurements for countercyclical policies.

This study provides reference for improving potential output estimates and avoiding policy errors.

**(Page 44/65)**

---

## Stylized Facts of Money Markets: An Empirical Analysis of Euro Area Data

**Authors:**  
VL Coz, N Allaire, M Benzaquen, D Challet - arXiv:2024  
Ecole Polytechnique, European Central Bank

**Research Findings and Key Points**

LCR (Liquidity Coverage Ratio) regulation has driven an increase in "evergreen repos", making the euro area interbank network denser, more stable, and more inclined towards secured lending.

- Evergreen repo agreements increased significantly after LCR regulation, reflecting the transition from unsecured to secured transactions in the euro area money market.
- Underlying data shows that the collateral reuse rate is about 1, consistent with literature, and the euro area interbank network is denser and more symmetric than the unsecured market.
- Analysis of financing activities of 47 large euro area banks using ECB's MMSR data illustrates the key role of evergreen repos in addressing LCR constraints.

Figure 1 shows the trend of changes in transaction volumes in unsecured and secured money markets aggregated quarterly, comparing historical data to MMSR data.

**(Page 45/65)**

---

## A Minimalist Model of Money Creation Under Regulatory Constraints

**Authors:**  
VL Coz, M Benzaquen, D Challet - arXiv:2410.18145 (2024)  
École Polytechnique, CentraleSupélec

**Research Findings and Key Points**

Using an agent-based model to study bank liquidity management under regulatory constraints reveals that asymmetric responses to payment shocks lead to excess liquidity in the money market.

- Banks adopt asymmetric strategies to manage LCR when facing payment shocks, leading to an increase in evergreen repos in the money market.
- As collateral scarcity increases, collateral reuse rates rise; evergreen repos allow banks to meet liquidity needs without affecting LCR.
- Simulation results highlight the importance of collateralized transactions in maintaining financial stability and provide new perspectives for understanding the impact of regulation on money market dynamics.

Figure 7 shows changes in average regulatory ratios, collateral reuse, and network density under different deposit outflow rates.

**(Page 46/65)**

---

## Can Competition Increase Factor Investing Profits?

**Authors:**  
V DeMiguel, A Martin-Utrera - Management Science (2024)  
London Business School, Iowa State University

**Research Findings and Key Points**

The study finds that competition reduces profits for the same factor strategy, but if competitors use different factors, multi-factor diversification can help increase profits.

- Multiple investors simultaneously using the same factor leads to price impact and reduced profits; using different factors can increase profits through trade diversification.
- Diversification can offset the negative effects of factor competition, producing positive externalities.
- Using 18 factors and mutual fund holdings data, game theory models, and empirical analysis prove the dual impact of competition on factor returns.

The figure shows total profit change curves under different factors and investment scales, with different colored lines indicating the impact of multiple investor numbers.

**(Page 47/65)**

---

## Conditional Forecasting of Variation Margin Calls with Dynamic Graph Neural Networks

**Authors:**  
M Citterio, M D'Errico, G Visentin - arXiv:2410.23275 (2024)  
European Central Bank, ETH Zurich

**Research Findings and Key Points**

A new DGNN architecture can accurately predict net variation margin (NVM) demands in financial networks up to 21 days ahead, providing a forward-looking tool for systemic risk monitoring.

- Incorporates network dynamics into stress testing, extending traditional risk assessment methods by constructing dynamic financial networks based on overnight index swaps.
- Uses GC-LSTM model to extract spatiotemporal patterns, training DGNN models with simulated data to enable generalization and prediction capabilities in stress test scenarios.
- The study marks a shift from ex-post to ex-ante systemic risk assessment, helping central banks and regulators monitor market reactions under interest rate shocks.

The figure compares 1-step and 10-step NVM prediction result curves with benchmarks, showing that DGNN maintains high accuracy even in longer-term predictions.

**(Page 48/65)**

---

## Foundation Models for Time Series for Value at Risk

**Authors:**  
A Goel, P Pasricha, J Kanniainen - arXiv:2410.11773 (2024)  
Tampere University, IIT Ropar

**Research Findings and Key Points**

Fine-tuning TimesFM (Google's pre-trained time series foundation model) outperforms traditional econometric models, providing a data-driven solution for Value at Risk (VaR) estimation.

- Fine-tuned TimesFM surpasses traditional models like GARCH and GAS in VaR prediction and is applicable to various confidence levels.
- The study shows that the data-driven approach of foundation models plus fine-tuning is more flexible and generalizable compared to pure econometric methods.
- Using 19 years of daily return data from the S&P 100 index, backtesting through actual-expected ratio and quantile scores supports the shift towards data-driven methods.

The figure compares the number of assets for which the null hypothesis is not rejected at 1%, 2.5%, 5%, and 10% VaR levels for different models, with higher numbers indicating better consistency between expected and actual default rates.

**(Page 49/65)**

---

## Model Validation Practices in Banking: A Structured Approach

**Authors:**  
A Sudjianto, A Zhang - arXiv:2410.13877 (2024)  
Wells Fargo

**Research Findings and Key Points**

Reviews key implementation aspects of model validation in banking, including conceptual soundness, outcome analysis, and ongoing monitoring, to ensure model compliance and reliability.

- Provides a structured model validation framework emphasizing three pillars: conceptual reasonableness assessment, outcome analysis, and ongoing monitoring.
- Reviews SR11-7/OCC11-12 regulatory guidance emphasizing model risk management, with no new terminology but reaffirming the importance of long-term practical experience.
- Emphasizes the importance of ongoing monitoring and evaluation in ensuring model credibility and decision support.

This study provides clear, structured guidance on the importance and practical operations of bank model validation.

Here is the English translation of the text, maintaining technical accuracy, formatting, and precision for financial documentation:

**(Page 50/65)**

---

## Liquidity Drivers in Decentralized Exchange Uniswap

**Authors:**  
BZ Zhu, D Liu, X Wan, G Liao, CC Moallemi - arXiv:2024  
Columbia University, Uniswap Labs

**Research Findings and Key Insights**

The study identifies core factors influencing Uniswap v3 liquidity, including gas fees, token returns, and volatility, and introduces new metrics for refined analysis.

- Liquidity concentration is driven by gas prices, underlying token returns, and volatility; fee income and markout simultaneously affect TVL and liquidity concentration.  
- Introduces a v2 counterfactual spread metric for in-depth analysis of liquidity concentration changes and influencing factors.  
- Increased competition and external liquidity sources lead to liquidity dispersion, affecting Uniswap v3's market depth.

The research provides data-driven evidence for understanding DeFi liquidity dynamics, competitive landscape, and pricing mechanisms.

**(Page 51/65)**

---

## AgileRate: Bringing Adaptivity and Robustness to DeFi Lending Markets

**Authors:**  
M Bastankhah, V Nadkarni, X Wang - arXiv:2024  
UIUC, Princeton University

**Research Findings and Key Insights**

The AgileRate dynamic model significantly improves lending utilization and reduces liquidation risk through an adaptive interest rate controller (RLS algorithm), outperforming static models.

- Introduces an adaptive interest rate controller using the Recursive Least Squares (RLS) algorithm, proposing new guarantees for interest rate convergence and utilization stability.  
- Validates AgileRate's superior performance over static protocols on Aave data, excelling in maintaining optimal utilization and reducing liquidation risk.  
- The method offers theoretical guarantees, resists adversarial manipulation, balances adaptivity and robustness, and performs well under dynamic market conditions.

The figure compares the RLS controller with Aave's static curve in utilization rate over time, as well as utilization error under high transfer noise, with RLS consistently maintaining robustness.

**(Page 52/65)**

---

## XForecast: Evaluating Natural Language Explanations for Time Series Forecasting

**Authors:**  
T Aksu, C Liu, A Saha, S Tan, C Xiong - arXiv:2024  
NUS, Salesforce Research

**Research Findings and Key Insights**

Proposes new evaluation metrics for natural language explanations of time series forecasts, finding that numerical reasoning ability is more important than model size.

- Introduces two new metrics: direct and synthetic simulability, to assess how explanation text helps in predicting model outputs and generalizing to new data.  
- Experiments show that numerical reasoning ability is crucial for explanation quality, with model size not being the determining factor.  
- Through experiments across multiple datasets and models, these metrics align with human judgment and effectively distinguish between good and poor explanations.

Figure 2 illustrates the two metrics: direct simulability and synthetic simulability, used to evaluate the consistency and extensibility of explanations for predictions.

**(Page 53/65)**

---

## Interval Estimation for Multi-step Time Series Forecasting Using Online Isotonic Inference

**Authors:**  
X Wang, RJ Hyndman - arXiv:2410.13115 (2024)  
Monash University

**Research Findings and Key Insights**

The AcMCP method provides more effective prediction intervals for multi-step forecasts by considering the autocorrelation of multi-step forecast errors in non-stationary AR processes.

- Optimizes the structure of h-step forecast errors, showing that in non-stationary autoregressive models, forecast errors have autocorrelation up to lag (h-1) at most.  
- Introduces the AcMCP method to incorporate these autocorrelations, obtaining long-term coverage guarantees without distributional assumptions.  
- In electricity demand and restaurant expenditure forecasting, the AcMCP method shows greater statistical efficiency and reliable coverage rates compared to traditional methods.

Figure 3 shows boxplots comparing coverage rates and interval widths for different methods across forecast horizons in AR(2) simulations, with AcMCP performing more stably around the target coverage rate.

**(Page 54/65)**

---

## Cutting-Edge Research Beyond Selected Papers

The following is a list of noteworthy papers beyond this curated selection, considered based on topic, impact, authors, publication, and citation status.

**AI and LLM Applications in Finance and Trading**

1. GPT-Signal: Generative AI for Semi-automated Feature Engineering in the Alpha Research Process  
2. Generative AI in Financial Reporting  
3. Aligning LLMs with Human Instructions and Stock Market Feedback in Financial Sentiment Analysis  
4. CustomizedFinGPT Search Agents Using Foundation Models  
5. Large Language Models in Economics  
6. The macroeconomic implications of the Gen-AI economy  
7. What Role Does AI Play In Modern Financial Transactions?  
8. Efficient Training of Neural Stochastic Differential Equations by Matching Finite Dimensional Distributions  
9. Generation of synthetic financial time series by diffusion models  
10. Financial Time Series Forecasting Based on Adversarial Training and Dynamic Weight Design  
11. A scoping review of ChatGPT research in accounting and finance  
12. Opportunities and Challenges of Generative-AI in Finance

**(Page 55/65)**

---

## Frontier Exploration: Research Beyond the Selection (Continued)

Here's the English translation of the provided text, maintaining all formatting and technical accuracy:

13. Multiple Objectives Escaping Bird Search Optimization and Its application in Stock Market Prediction Based on Transformer Model  
14. FinTeamExperts: Role Specialized MOEs For Financial Analysis  
15. Financemath: Knowledge-intensive math reasoning in finance domains  
16. Deep Learning in Finance: A Survey of Applications and Techniques  
17. Natural language processing in finance: A survey  
18. FLAG: Financial Long Document Classification via AMR-based GNN  
19. The Local Effects of Artificial Intelligence Labor Investments: Evidence from the Municipal Bond Market  
20. Enhancing LLM Trading Performance with Fact-Subjectivity Aware Reasoning  
21. The Role of Artificial Intelligence in Investment Decision-Making: Opportunities and Risks for Financial Institutions  
22. From Facts to Insights: A Study on the Generation and Evaluation of Analytical Reports for Deciphering Earnings Calls  
23. Temporal Relational Reasoning of Large Language Models for Detecting Stock Portfolio Crashes  
24. GraphVAE: Unveiling Dynamic Stock Relationships with Variational Autoencoder-based Factor Modeling  
25. Mapping Hong Kong's Financial Ecosystem: A Network Analysis of the SFC's Licensed Professionals and Institutions  
26. FAMMA: A Benchmark for Financial Domain Multilingual Multimodal Question Answering

**(Page 56/65)**

---

## Frontier Exploration: Research Beyond the Selection (Continued)

27. Exploiting Risk-Aversion and Size-dependent fees in FX Trading with Fitted Natural Actor-Critic  
28. Distilling Analysis from Generative Models for Investment Decisions  
29. Large Legislative Models: Towards Efficient AI Policymaking in Economic Simulations  
30. The effect of ESG divergence on the financial performance of Hong Kong-listed firms: an artificial neural network approach  
31. A comparative analysis of SHAP, LIME, ANCHORS, and DICE for interpreting a dense neural network in Credit Card Fraud Detection  
32. Hierarchical Reinforced Trader (HRT): A Bi-Level Approach for Optimizing Stock Selection and Execution  
33. The Perks and Perils of Machine Learning in Business and Economic Research  
34. Decrypting Corporate Speak: GPT-Assisted Measurement of Facts and Tones in Earnings Calls  
35. TraderTalk: An LLM Behavioural ABM applied to Simulating Human Bilateral Trading Interactions  
36. Enhancing Compliance And KYC Processes Through AI, OCR, And Automation: A Cost-effective Approach

**New Developments in Portfolio Strategies and Market Prediction**

37. Deep Learning Methods for S Shaped Utility Maximisation with a Random Reference Point

**(Page 57/65)**

---

## Frontier Exploration: Research Beyond the Selection (Continued)

Here's the English translation, maintaining the technical accuracy, formatting, and structure of the original text:

38. Two-fund separation under hyperbolically distributed returns and concave utility function  
39. Robust forward investment and consumption under drift and volatility uncertainties: A randomization approach  
40. Clustering Digital Assets Using Path Signatures: Application to Portfolio Construction  
41. Machine Learning for Real-Time Portfolio Rebalancing: A Novel Approach to Financial Optimization  
42. Time evaluation of portfolio for asymmetrically informed traders  
43. Conformal Predictive Portfolio Selection  
44. Predicting the stock market prices using a machine learning-based framework during crisis periods  
45. MFB: A Generalized Multimodal Fusion Approach for Bitcoin Price Prediction Using Time-Lagged Sentiment and Indicator Features  
46. Kendall Correlation Coefficients for Portfolio Optimization  
47. Delegated portfolio management with random default  
48. Deep prediction on financial market sequence for enhancing economic policies  
49. Economic Theory and Machine Learning Integration in Asset Pricing and Portfolio Optimization: A Bibliometric Analysis and Conceptual Framework  
50. Generalized Distribution Prediction for Asset Returns  
51. Unlocking predictive potential: the frequency-domain approach to equity premium forecasting

**(Page 58/65)**

---

## Frontier Exploration: Research Beyond the Selection (Continued)

52. Improving out-of-sample forecasts of stock price indexes with forecast reconciliation and clustering  
53. A Comparative Analysis of Deep Learning and Traditional Statistics for Stock Price and Return Forecasting  
54. A Fully Analog Pipeline for Portfolio Optimization

**Electronic Financial Markets and LOB**

55. Reinforcement Learning in Non-Markov Market-Making  
56. Double Auctions: Formalization and Automated Checkers  
57. A Financial Market Simulation Environment for Trading Agents Using Deep Reinforcement Learning  
58. Price impact and long-term profitability of energy storage  
59. Information Externalities, Free Riding, and Optimal Exploration in the UK Oil Industry

**Financial Derivatives Modeling and Volatility Frontier**

60. Graph-Based Methods for Forecasting Realized Covariances  
61. Discrete approximation of risk-based prices under volatility uncertainty  
62. A second order finite volume IMEX Runge-Kutta scheme for two dimensional PDEs in finance  
63. No arbitrage and the existence of ACLMMs in general diffusion models  
64. Numerical analysis of American option pricing in a two-asset jump-diffusion model

**(Page 59/65)**

---

## Frontier Exploration: Research Beyond the Selection (Continued)

Here's the English translation, maintaining all formatting and technical accuracy:

65. European Option Pricing in Regime Switching Framework via Physics-Informed Residual Learning  
66. Efficient calibration of the shifted square-root diffusion model to credit default swap spreads using asymptotic approximations  
67. A Data Driven Study on Fractional Black-Scholes-Merton Equation Using Physics Informed Neural Network  
68. Automated Volatility Forecasting  
69. Exploiting News Analytics for Volatility Forecasting  
70. Multi-model transfer function approach tuned by PSO for predicting stock market implied volatility explained by uncertainty indexes  
71. KANOP: A Data-Efficient Option Pricing Model using Kolmogorov-Arnold Networks  
72. Forecasting Day-Ahead Eurusd Tail Risk: Leveraging Machine Learning and the Volatility Surface  
73. Exact Simulation of Quadratic Intensity Models

**New Trends in Financial Markets and Macroeconomics**

74. Mean field equilibrium asset pricing model under partial observation: An exponential quadratic Gaussian approach  
75. Responsible Investing under Climate Change Uncertainty  
76. Fractional Moments by the Moment-Generating Function  
77. Distributionally Robust Instrumental Variables Estimation

**(Page 60/65)**

---

## Frontier Exploration: Research Beyond the Selection (Continued)

78. Macroeconomic Impacts of ETS Revenue Allocation: A Post-Keynesian Analysis of Decarbonization Strategies in the EU  
79. Note on Bubbles Attached to Real Assets  
80. A Run on Fossil Fuel? Climate Change and Transition Risk  
81. Dynamic treatment effect of capital controls on macroeconomic and financial stability in emerging market economies  
82. Heterogeneous Economies and Micro Data  
83. How Do Electoral Votes, Presidential Approval, and Consumer Sentiment Respond to Economic Indicators?  
84. A Hierarchical-Dealer-Centric Model of FX Swap Valuation  
85. Is Capital Structure Irrelevant with ESG Investors?  
86. Alternative Finance in the International Business Context: A Review and Future Research  
87. Dynamic graphical models: Theory, structure and counterfactual forecasting  
88. The Hallin-Liška criterion through the lens of the random matrix theory  
89. The effects of climate change-related risks on banks: A literature review  
90. Machine Learning Debiasing with Conditional Moment Restrictions: An Application to LATE  
91. Reforming the IMF Surcharge Rate Policy to Avoid Procyclical Lending  
92. Econometrics of Insurance with Multidimensional Types  
93. TimeBridge: Non-Stationarity Matters for Long-term Time Series Forecasting

**(Page 61/65)**

---

## Frontier Exploration: Research Beyond the Selection (Continued)

94. EXPRESS: Addressing Endogeneity Using a Two-stage Copula Generated Regressor Approach  
95. Empirical Insights into Financial Development and Climate Policy Uncertainty Paving the Path for Energy Diversification in the US  
96. Managerial Overextrapolation: Who and When

**Quantitative Risk Management**

Here's the English translation of the provided text, maintaining technical accuracy, formatting, and precision:

97. First order Martingale model risk and semi-static hedging
98. Optimal mutual insurance against systematic longevity risk
99. Corporate Non-Disclosure Disputes: Equilibrium Settlements with a Probabilistic Burden of Proof
100. Risk Aggregation and Allocation in the Presence of Systematic Risk via Stable Laws
101. Applications of the Second-Order Esscher Pricing in Risk Management
102. Worst-case values of target semi-variances with applications to robust portfolio selection
103. Machine learning technique to compute climate risk in finance
104. A dealer's funding liquidity risk and its money market trades in the 2007/08 crisis
105. Cryptocurrencies and Systemic Risk: The Spillover Effects Between Cryptocurrency and Financial Markets
106. Skew Index: a machine learning forecasting approach
107. Continuous Risk Factor Models: Analyzing Asset Correlations through Energy Distance

---

## Frontier Exploration: Research Beyond the Selection (Continued)

108. Quantum Monte Carlo Integration for Simulation-Based Optimisation
109. Tail risk and uncertainty in financial markets
110. Stochastic Loss Reserving: Dependence and Estimation
111. Examination of Bitcoin Hedging, Diversification and Safe-Haven Ability During Financial Crisis: Evidence from Equity, Bonds, Precious Metals and Exchange Rate
112. Measuring Market Risk in Asset Management
113. Computing Systemic Risk Measures with Graph Neural Networks
114. A Spatio-Temporal Machine Learning Model for Mortgage Credit Risk: Default Probabilities and Loan Portfolios
115. Forecasting VaR and Returns Distribution Using the Real-Time GARCH Models with Standardized Two-Sided Lindley Distribution
116. The Analytics of Robust Satisficing: Predict, Optimize, Satisfice, Then Fortify
117. Risk parity portfolio optimization under heavy-tailed returns and dynamic correlations
118. Are causal effect estimations enough for optimal recommendations under multi-treatment scenarios?
119. A One-Step Approach for Determining the Optimal Aggregate Capital Reserve and Allocation
120. On the mean-field limit of diffusive games through the master equation: extreme value analysis

---

## Frontier Exploration: Research Beyond the Selection (Continued)

**Decentralized Finance (DeFi)**

121. The Rise of Decentralised Finance (DeFi)
122. Lightning Network Economics: Topology
123. Competitive dynamics between decentralized and centralized finance lending markets
124. Ormer: A Manipulation-resistant and Gas-efficient Blockchain Pricing Oracle for DeFi
125. Improving DeFi Mechanisms with Dynamic Games and Optimal Control: A Case Study in Stablecoins
126. Security Perceptions of Users in Stablecoins: Advantages and Risks within the Cryptocurrency Ecosystem

**Time Series Forecasting**

Here's the English translation of the provided text, maintaining technical accuracy, formatting, and precision:

127. HiMTM: Hierarchical Multi-Scale Masked Time Series Modeling with Self-Distillation for Long-Term Forecasting  
128. FlexTSF: A Universal Forecasting Model for Time Series with Variable Regularities  
129. Novel Bayesian algorithms for ARFIMA long-memory processes: a comparison between MCMC and ABC approaches  
130. Recurrent Neural Goodness-of-Fit Test for Time Series  
131. xLSTM-Mixer: Multivariate Time Series Forecasting by Mixing via Scalar Memories  
132. Context is Key: A Benchmark for Forecasting with Essential Textual Information

**(Page 64/65)**

---

## Frontier Exploration: Research Beyond the Selection (Continued)

133. Graph Neural Flows for Unveiling Systemic Interactions Among Irregularly Sampled Time Series  
134. TimeMixer++: A General Time Series Pattern Machine for Universal Predictive Analysis  
135. Timer-XL: Long-Context Transformers for Unified Time Series Forecasting  
136. Inferring Latent Graphs from Stationary Signals Using a Graphical Autoregressive Model  
137. Metadata Matters for Time Series: Informative Forecasting with Transformers  
138. Learning Pattern-Specific Experts for Time Series Forecasting Under Patch-level Distribution Shift  
139. GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation  
140. Advancing Multivariate Time Series Anomaly Detection: A Comprehensive Benchmark with Real-World Data from Alibaba Cloud  
141. Diffusion Auto-regressive Transformer for Effective Self-supervised Time Series Forecasting  
142. LLM-Mixer: Multiscale Mixing in LLMs for Time Series Forecasting  
143. LLM-TS Integrator: Integrating LLM for Enhanced Time Series Modeling  
144. Scalable Signature-Based Distribution Regression via Reference Sets  
145. Robustness Auditing for Linear Regression: To Singularity and Beyond  
146. On Anticompetitive Third-Degree Price Discrimination

---

*The above is a selected index of papers and additional frontier research in the field of quantitative finance as of October 2024, covering areas such as AI, LLM, portfolio optimization, derivative pricing, risk management, DeFi, macroeconomics, and time series forecasting, providing references and insights for researchers, practitioners, and policymakers.*

## About LLMQuant

LLMQuant is a cutting-edge community composed of individuals from top global universities and quantitative finance professionals, dedicated to exploring the infinite possibilities in the fields of Artificial Intelligence (AI) and Quantitative Finance (Quant). Our team members come from world-renowned institutions such as the University of Cambridge, University of Oxford, Harvard University, ETH Zurich, Peking University, and the University of Science and Technology of China. Our external advisors are from leading companies including Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top private equity firms in China.