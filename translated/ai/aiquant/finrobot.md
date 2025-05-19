---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Note: These appear to be image references/links that don't contain actual text to translate. I've preserved them exactly as they appear in the original format. If there is additional text you'd like translated, please provide it.

## FinRobot: A Stock Research and Valuation Framework Based on Large Language Models

In today's increasingly complex financial markets, efficient sell-side securities research often requires the support of automated tools. However, many existing AI solutions focus solely on technical indicators and lack flexible subjective analysis capabilities, making it difficult to adapt to new data in real-time or accurately assess risks, thus limiting their value in practical investment.


![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/01/29/1738120002722-a681f3a4-f2b3-4c73-91d7-24fe80ded644.png)


**FinRobot introduced in this article** is the first AI agent framework specifically designed for **stock research**. It employs a **multi-agent Chain of Thought (CoT) system** that combines quantitative and qualitative analysis, simulating the comprehensive reasoning process of human analysts. The overall structure includes three major functional agents:

1. **Data-CoT Agent**: Integrates multi-source data, enabling comprehensive collection and intermediate summarization of information from financial statements, company announcements, and third-party databases.
2. **Concept-CoT Agent**: Conducts in-depth analysis of key financial indicators and industry environment, simulating human analyst research approaches to form actionable analytical conclusions.
3. **Thesis-CoT Agent**: Finally integrates analysis results into investment recommendation reports, providing comprehensive judgments including data information, valuation metrics, and risk assessments.

Unlike existing automated research platforms (such as CapitalCube, Wright Reports), FinRobot possesses both **real trading value** and **institutional-grade quality**, with continuous updating capabilities for market trends and more realistic risk assessment. The framework is now open-source, available at: https://github.com/AI4Finance-Foundation/FinRobot

![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/01/22/1737589546535-0f621a57-2c2f-492d-ae3d-d9ef8b0a98d1.png)

> **Keywords**: AI-agent, Large Language Models, Equity Research, Financial Analysis, Chain of Thought

---

## 1. Introduction

**Financial analysis** is a core component of the financial services industry, influencing various investor decisions (Abarbanell and Bushee, 1997; Greenwald et al., 2004; Penman, 2010; Berman and Knight, 2013; Subramanyam, 2014). Within this field, **equity research** is particularly important, especially in sell-side research departments of major investment banks and securities firms. Traditional research reports typically require analysts to possess deep quantitative modeling skills and industry knowledge, but this process is often time and labor-intensive.

With the rise of **Artificial Intelligence (AI)** and **Large Language Models (LLM)** (Medhat et al., 2014; Brown et al., 2020; Wu et al., 2023; Yang et al., 2023; Kim et al., 2024), the financial sector has begun exploring automated securities research. However, existing tools largely focus on technical analysis or simple models, neglecting the combination of expert judgment and substantive qualitative analysis. **FinRobot**, introduced in this study, combines quantitative analysis while maintaining the flexibility of subjective judgment through multi-agent and Chain of Thought mechanisms, capable of meeting institutional-grade research depth.

**Key Contributions**:

- **First AI Securities Research Framework Applying Multi-Agent Chain of Thought (CoT)**: FinRobot breaks down the research process into three levels: data processing (Data-CoT), concept analysis (Concept-CoT), and research report generation (Thesis-CoT), simulating human analysts' thought chains.
- **Integration of Subjective Judgment, Real-time Data, and New Evaluation Metrics**: FinRobot features real-time data integration and multi-dimensional report quality assessment (Accuracy, Logicality, Storytelling).
- **Open-source Platform Promoting Financial AI Democratization**: FinRobot's source code is open, encouraging exchange and collaboration between the financial sector and AI community.

---

## 2. Related Research

### 2.1 LLM and Financial Applications
Large Language Models (LLMs), due to their powerful understanding and expression capabilities of natural language, are playing an increasingly important role in **financial analysis**, including tasks such as **sentiment analysis** (Medhat et al., 2014; Huang et al., 2023; Zhang et al., 2023) and **market prediction** (Henrique et al., 2019; Nabipour et al., 2020; Kumar et al., 2022; Jiang, 2021). However, LLMs often lack real-time data and industry-specific knowledge, making it difficult to meet the demanding requirements of real-time securities research. This project focuses on addressing this pain point.

### 2.2 Applications of AI Agents and Chain of Thought in Financial Analysis
Multi-agent collaboration frameworks have brought more efficient decision-making processes to financial analysis, such as FinAgent (Zhang et al., 2024) and FinMem (Yu et al., 2023), which can utilize real-time market data to assist trading strategies. Meanwhile, **Chain-of-Thought** (CoT) prompting can simulate human thinking steps and significantly improve analysis quality (Wei et al., 2022; Kim et al., 2024). Building on this foundation, FinRobot has specifically designed a dedicated CoT framework for sell-side research needs, achieving more comprehensive financial analysis depth and adaptive flexibility.

## 3. Methodology

### 3.1 Overall Framework
Figure 1 below shows FinRobot's multi-layer CoT structure, which divides the entire financial research process into three sequential Agent levels, enhancing both analytical professionalism and the logic and readability of the final report.


![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/01/29/1738120339772-d962baa5-31f2-475a-8079-03411ce161c0.png)


1. **Data Processing Layer (Data-CoT Agent)**  
   - Responsible for gathering information from multiple channels including SEC filings, earnings calls, and company announcements, followed by cleaning, formatting, and extracting key financial metrics.  
   - This Agent can simultaneously obtain both quantitative and qualitative data, laying the foundation for subsequent conceptual analysis.

2. **Financial Concept Layer (Concept-CoT Agent)**  
   - Transforms processed data into actionable financial concepts and forecasts, including **revenue growth**, **EBITDA trends**, **market positioning**, etc.  
   - Evaluates competitive landscape, sentiment factors, and potential risks through thinking patterns similar to human analysts.

3. **Equity Research Template Layer (Thesis-CoT Agent)**  
   - Integrates the above analysis results to produce complete **investment research reports**, including investment theses, risk assessments, valuation models, and conclusive investment ratings (such as buy/hold/sell).  
   - This Agent uses professional sell-side report templates to ensure the final report meets industry standards.

### 3.2 Data Processing Layer
The **Data-CoT Agent** aggregates multi-channel data and performs preprocessing to ensure information **accuracy** and **comprehensiveness**. Major data sources include:

- **Databases**: Oceanbase, PostgreSQL, etc., for storing structured financial data.
- **Unstructured documents**: Such as PDF, DOCX, images, etc., for extracting text and key information.
- **Third-party interfaces**: Chart visualization configuration, API real-time data retrieval, etc.
- **Internet search**: Integration of multi-dimensional market information and industry dynamics.
- **Distributed file storage**: DFS, Minio, etc., to ensure high availability and robustness of massive data.

Additionally, FinRobot performs detailed key point extraction from **SEC filings** (10-K, 10-Q, etc.) and **earnings conference calls**, including key figures such as **revenue, operating costs, SG&A**, to further calculate **revenue growth, contribution profit, EBITDA and its margin** (see table below). These metrics are crucial foundations for subsequent analysis and valuation.

**Common Financial Formula Examples**:

| **Formula** | **Description** |
| --- | --- |
| **Revenue Growth** = $(\text{Revenue}_{current} - \text{Revenue}_{previous}) / \text{Revenue}_{previous}$ | Calculates revenue growth relative to previous period |
| **Contribution Profit** = Revenue $-$ Operating Expense | Measures profitability after deducting operating costs |
| **EBITDA Margin** = $ \text{EBITDA} / \text{Revenue} $ | EBITDA as percentage of revenue, measures operational efficiency |
| **CAGR** = $((\text{EV}/\text{BV})^{1/n}-1)\times 100$ | Compound Annual Growth Rate |
| **Enterprise Multiple** = $ \text{EV} / \text{EBITDA} $ | Common valuation multiple for assessing company value |

### 3.3 Fin-Concept Layer
In the **Concept-CoT Agent**, FinRobot conducts further analysis of the financial indicators generated in the previous step, addressing deeper questions closely related to investment logic:

- **Revenue Forecast**: Sets optimistic and conservative growth scenarios for enterprises by considering historical growth, backlog, inflation, and market pricing factors.
- **EBITDA and Profit Margins**: Obtains more accurate profitability levels by excluding one-time items, and compares profit margin trends with industry benchmarks.
- **Key Metrics like ROIC, WACC**: Used to evaluate company's capital efficiency and cost of capital, providing support for valuation models such as DCF.
- **Financial Q&A**: Addresses topics such as the company's competitive advantages over peers, impact of external environment on profitability, and profit expansion potential in subsequent years.

### 3.4 Research Report Layer
The **Thesis-CoT Agent** presents the above analysis results in the format of a **sell-side research report**, including the following key components:

- **Investment Thesis**: Provides clear buy/sell/hold investment ratings based on financial forecasts and industry trends.  
- **Risk Analysis**: Lists major risk factors affecting company valuation and growth, helping investors balance opportunities and challenges.
- **Valuation and Financial Forecasts**: Includes revenue, EBITDA, and profit margin projections for future years, providing target prices using models such as DCF or P/E.
- **Competitor Analysis**: Assesses the target company's relative market position by comparing revenue growth, gross margins, EBITDA, and SG&A expense ratios with peers.


![](https://fastly.jsdelivr.net/gh/bucketio/img0@main/2025/01/29/1738121121008-bf853eb2-10f3-4495-8f66-ff4e1c8c618f.png)

## 4. Experiment

### 4.1 Task Description
FinRobot is applicable to stock reports across multiple industries. This example uses **Waste Management, Inc.** (North American waste management and environmental services giant) as a case study. It provides a comprehensive analysis of the company's financial performance, valuation methods, risk factors, and industry comparisons, supported by clear tables and charts. For more details, please refer to the complete research report in the appendix.

### 4.2 Implementation Details
1. **Data Processing (Data-CoT Layer)**: Collected SEC filings, company announcements, and historical financial data.  
2. **Concept Analysis (Concept-CoT Layer)**: Adopted analyst approach to address core questions about earnings drivers, competitive landscape, and potential risks.  
3. **Report Integration (Thesis-CoT Layer)**: Compiled the above points into a formal research report format, including charts and summaries for investors' quick comprehension.

### 4.3 Evaluation

#### 4.3.1 Expert Review
We invited several investment banking analysts to score FinRobot-generated reports on three dimensions: **Accuracy**, **Logicality**, and **Storytelling** on a scale of 0-10 (detailed criteria provided in Table 3). As shown in Table 2, most reviewers gave high scores of **9 or 10** for accuracy, indicating highly reliable numbers and analysis. Logicality also received high ratings, though some reviewers saw minor room for improvement. Storytelling performance was generally good, with some reviewers suggesting enhancements in readability or narrative quality.

#### 4.3.2 Large Model Evaluation
In addition to experts, we also used **GPT-4** to score the reports along the same dimensions (see Figure 3). The results were largely consistent with expert reviews (Figure 4 shows the specific comments), further demonstrating that the report has received widespread recognition for its **data accuracy, clear structure, and content readability**.

#### 4.3.3 Stability Testing
To verify FinRobot's stability, we generated multiple reports for the same company and used GPT-4 to score the consistency of each report, comparing the results with zero-shot, few-shot, and pure Chain-of-Thought prompting approaches. We found that FinRobot consistently outperformed other prompting methods in terms of **Accuracy, Logicality, and Storytelling** (see Figure 5), with minimal fluctuation, demonstrating stable and reliable report generation.

## 5. Conclusion

The proposed **FinRobot** leverages a multi-agent Chain of Thought system to perfectly integrate quantitative and qualitative analysis, greatly enhancing the practical value of AI in sell-side securities research. It possesses **real-time data pipeline** and **professional risk assessment** capabilities, producing accurate, detailed reports that facilitate decision-making.

Looking ahead, we will further expand FinRobot's applications across different industries and asset classes, such as covering more securities, enhancing reinforcement learning and sentiment analysis capabilities, aiming to provide the financial industry with more diverse and innovative research tools.

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。