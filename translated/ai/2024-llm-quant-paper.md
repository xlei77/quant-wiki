---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# 2024 Review of Key Literature on Artificial Intelligence in Finance

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Over the past two years, with the rapid development of Generative AI and Large Language Models (LLMs), cutting-edge research and applications in the financial sector have also ushered in a new round of innovation. This article aims to summarize, organize, and showcase **key academic papers** and **practical cases** representative of the intersection between quantitative finance and LLMs in the past two years. Through a systematic introduction to historical evolution, methodological challenges, application scenarios, and evaluation benchmarks, this review provides readers with a clear roadmap, helping practitioners and researchers better understand and utilize LLM technology to drive innovation and transformation in the financial field.

## Table of Contents

1. Brief History of LLM Development
2. General Application Scenarios of LLMs
3. Methodology, Applications, and Challenges of FinLLMs
4. Panorama of Financial LLMs
5. Directory of 48 Key Papers on Generative AI in Finance
   - Financial Forecasting, Investment Strategies, and Risk Management
   - Sentiment Analysis and Text Mining
   - Time Series Analysis and Prediction
   - LLM Development (Fine-tuning) and Financial Data Integration
   - Evaluation and Benchmarking of Financial LLMs

---

### Brief History of LLM Development

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/12/14/1734186113125-da5c35e4-7718-45c6-9e72-e60a09c42d87.png)

---

### General Application Scenarios of LLMs

![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2024/12/14/1734186140553-0f9c1d40-6c10-4dd6-857e-5edd165fb9e3.png)

- **Fine Tuning**:
  Adjusting a general LLM to become a domain-specific expert. Starting with an LLM possessing broad knowledge, then training it with domain-specific data to understand specialized documents (e.g., medical records, legal documents) and excel in related tasks.

- **Prompt Engineering**:
  When insufficient fine-tuning data is available, designing clever instructions and prompts for the model to guide it in efficiently executing specific tasks despite data limitations.

- **RAG (Retrieval-Augmented Generation)**:
  When lacking suitable fine-tuning or prompt data, providing LLMs with a large, retrievable data repository. LLMs search for text similar to the query content using text embedding and encoding techniques to find relevant information, filling knowledge gaps and enhancing the reference value of responses.

- **COT (Chain of Thoughts)**:
  Helping LLMs break down complex problems into several small steps for more in-depth logical reasoning.

- **Agent CodeLLM (LLM with Solver)**:
  Such as Code Interpreter, capable of directly processing code and data.

- **Agent LLM Integration with Search Engines**:
  Like "perplexity", enabling LLMs to use search engines to obtain real-time information for answering complex queries.

- **Self-Reflection**:
  LLMs evaluate their own outputs, selecting the most appropriate result from different answers to improve accuracy and relevance.

- **Multishot Prompting**:
  Providing multiple examples within the same prompt to help LLMs better understand tasks and generate higher quality, more precise responses.

- **Hallucinations/Machine Unlearning/Safety**:
  Due to factors such as data quality, generation method bias, probabilistic nature, high temperature settings, or misleading prompts, LLMs may produce responses that do not align with facts. Safety strategies and model improvements are needed to reduce such risks.

### Methodology, Applications, and Challenges of FinLLMs

- **Application Scenarios**:
  - Market news sentiment analysis
  - Financial report risk assessment
  - Automated financial advice
  - Automated trading strategies
  - Fraud detection
  - Customer service chatbots
  - Market trend analysis

- **Challenges**:
  - Data privacy and security
  - Model interpretability
  - Bias reduction
  - Seamless integration with existing systems
  - Accurate backtesting (avoiding GPT model temporal information leakage)

- **Future Directions**:
  - Enhancing model transparency
  - Exploring unsupervised learning opportunities
  - Establishing ethical standards for AI in finance

Choosing appropriate methods will significantly impact the model's effectiveness in specific financial tasks.

### Panorama of Financial LLMs

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2024/12/14/1734187108044-881dd1ac-af20-447a-bc58-511eb0d6941c.png)

### Financial Forecasting, Investment Strategies, and Risk Management

- [ChatGPT Stock Forecasting](): Using ChatGPT to analyze news sentiment for predicting stock returns, significantly outperforming traditional methods.

- [FinancialStatementAnalysis](): LLMs using financial report text to predict corporate earnings changes, performing better than human analysts.

- [Ploutos](): Introducing a financial LLM framework that can integrate text and numerical data, improving stock prediction accuracy and interpretability.

- [QuantAgent](): A self-improving quantitative investment LLM Agent, enhancing financial forecasting and signal mining through a dual-layer learning process.

- [MarketSenseAI](): Utilizing GPT-4 to analyze multi-dimensional data, providing superior performance for stock selection.

- [RiskLabs](): LLM-based risk models outperforming traditional and AI models in predicting market volatility and VaR.

- [LOB-LLM](): Predicting order book information through an end-to-end autoregressive model, showing excellent correlation performance.

- [Alpha-GPT](): Incorporating humans into the decision loop for efficient and precise quantitative investment.

- [LLMFinAdvice](): In providing actionable investment advice, base and large models outperform small fine-tuned models.

- [LLMsCostROI](): Using decision theory to evaluate LLM costs and benefits, analyzing return on investment and profit potential.

- [SystemicRisk](): Utilizing LLM embeddings and knowledge graphs to assess systemic risk in financial news, finding low interconnectedness among U.S. financial institutions.

### Sentiment Analysis and Text Mining

Here is the English translation, maintaining all formatting and technical accuracy:

- [FinLlama](): Financial sentiment analysis model fine-tuned on Llama 2 7B, with better context understanding and robustness in volatile markets.

- [BioFinBERT](): Financial sentiment analysis focused on the impact of biotech press releases on stock prices.

- [SALLMRef](): Evaluates the performance of LLMs like ChatGPT in sentiment analysis, showing LLMs' advantages in few-shot learning but limitations in complex tasks.

- [SentiEval](): Proposes the SENTIEVAL benchmark for comprehensive evaluation of LLMs in sentiment analysis tasks.

- [FinSentGPT](): Financial sentiment model fine-tuned on ChatGPT, supporting multiple languages and outperforming existing models.

- [CryptoSentiment](): Fine-tuned GPT-4 outperforms BERT and FinBERT in cryptocurrency sentiment analysis.

- [FinancialTextAnalytics](): JPMorgan research assessing the strengths and weaknesses of ChatGPT and GPT-4 in financial text analysis.

- [NumLLM](): Model trained on Chinese financial textbooks, significantly outperforming existing models in understanding numerical financial problems.

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2024/12/14/1734186490555-6ddcb578-42e2-4925-a748-e5df8030cc69.png)

### Time Series Analysis and Forecasting

- [LLM-TimeSeries](): JPMorgan's systematic evaluation and taxonomy study of LLMs' ability to understand time series.

- [TimeGPT-1](): Pre-trained foundation model for time series forecasting, surpassing traditional statistical, machine learning, and deep learning methods in zero-shot settings.

- [TiMaGPT](): Time Machine GPT, employs time-adaptive training on historical data to avoid future data leakage.

- [SEEDS-GEE-WeatherForecast](): Weather prediction simulation using diffusion models, offering new insights for commodity trading.

- [LLMsStochasticFiltering](): MoE-F algorithm dynamically fuses predictions from multiple pre-trained LLMs, significantly improving F1 scores.

- [LLMsDistributionalShifts](): JPMorgan proposes a framework using LLMs and APIs to collect multivariate time series data, addressing distributional shifts.

- [AnomalyDetection](): Utilizes LLM embeddings to improve the accuracy of financial anomaly detection.

### LLM Development (Fine-tuning) and Financial Data Integration

- [BloombergGPT](): The first specialized financial LLM combining financial and textual data.

- [FinGPT](): Open-source financial LLM, fine-tuned using RLHF techniques.

- [FinMEM](): LLM Agent with human-aligned memory mechanisms for automated trading.

- [FinAgent](): Multimodal financial trading foundation Agent, integrating multi-source data, tool extensions, and advanced reasoning.

- [FinTextQA](): Financial Q&A dataset, where Baichuan2-7B performs close to GPT-3.5-turbo.

- [FinGPT-RLSP](): FinGPT uses RLSP to automatically collect and fine-tune from multivariate real-time data, enhancing real-time processing capabilities.

- [FinTral](): Mistral-7b-based multimodal financial LLM suite, adaptable to diverse data types and domain training.

- [Shai](): 10B parameter-level LLM focused on asset management.

- [FinVerse](): Financial Agent system with 600+ APIs, leveraging LLM-driven SFT to enhance data analysis.

- [FinRobot](): Open-source platform integrating specialized AI Agents with financial analysis to improve analysis and decision-making efficiency.

- [BlackScholesInDiffusionModels](): Incorporates Black-Scholes algorithm into diffusion model prompts to generate more realistic images.

- [FLAN-FinXC](): Based on FLAN-T5 and LoRA fine-tuning, excelling in financial numerical annotation tasks.

### Evaluation and Benchmarking of Financial LLMs

- [LLM-InvestingRationality](): Proposes economic rationality evaluation methods, with GPT-4 Turbo performing best among 14 LLMs. See [Are Large Language Models Rational Investors?]().

- [FinBen](): Open-source LLM evaluation benchmark for the financial domain, including 35 datasets and 23 tasks.

- [FinLLMs](): Survey research on LLMs in the financial domain.

- [LLMsRiskProfile](): LLMs aligned with human ethics show more risk aversion, affecting economic decisions and investment behavior.

- [LLMsEffectOnCryptoLiquidity](): AI revolution enhances efficiency and liquidity in cryptocurrency markets, especially after ChatGPT-3 release.

- [AutoGPT](): Extends LLM capabilities to complex reasoning and collaborative tasks.

- [FinGPT-Benchmark](): Evaluates the integration and benchmarking diversity and performance of open-source financial LLMs through instruction fine-tuning.

- [Portfolio with GenAI](): Uses graph models for cost-effective portfolio replication, meeting investor preferences while maintaining high correlation and stability.

- [FinGen](): Proposes three forward-looking financial argument generation tasks, utilizing evidence, charts, and news, highlighting current challenges.

- [AIinFinance](): Bank for International Settlements (BIS) research on the impact of generative AI on financial intermediation, insurance, asset management, and payments, while raising new challenges for financial stability and regulation.

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and quantitative finance practitioners, dedicated to exploring the infinite possibilities in artificial intelligence (AI) and quantitative (Quant) fields. Our team members come from world-renowned institutions such as Cambridge University, Oxford University, Harvard University, ETH Zurich, Peking University, USTC, etc. External advisors are from leading companies including Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top private equity firms in China.