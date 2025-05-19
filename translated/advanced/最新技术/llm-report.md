---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# Quantitative Frontiers | Using Large Language Models to Uncover Bad News Hidden in Corporate Annual Reports

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## Introduction: Hidden Secrets in Annual Reports

**Corporate Annual Reports (10-K)** are investors' core source of information for understanding a company's financial and operational conditions. However, research from the University of Chicago Booth School of Business has found that many companies deliberately conceal unfavorable news through textual and paragraph sequencing techniques in their annual reports. This article reveals these hidden strategies through Large Language Models (LLMs) and Attention Mechanisms, and demonstrates how to improve information interpretation efficiency using AI tools.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2024/12/22/1734887309221-84b023dd-771a-4cdc-8eb1-e1a3bdeb4ea9.png)

## Research Background and Core Questions

Over the years, market participants have been trying to understand: which annual report information truly drives stock price fluctuations? While quantitative data (such as revenue and profit margins) is relatively straightforward, qualitative data (such as changes in business models, competitive dynamics, and strategic initiatives) is often difficult to quantify and analyze. The University of Chicago team developed a novel approach by introducing LLMs with attention mechanisms to directly capture what investors focus on most in annual reports.

The research team's core objectives are to answer the following questions:

1. **What information in annual reports does the market pay attention to?**
2. **Do companies intentionally arrange paragraph sequences to manipulate investor attention?**
3. **How do AI models extract key information from complex texts?**

## Research Findings

### 1. **Analysis of Strategies for Concealing Bad News**

- **Information Sequencing Strategy**: Companies place negative information towards the end of the Management Discussion and Analysis (MD&A) section rather than at the beginning of the report, reducing attention to negative information.
- **Concealment Conditions**: Companies with high earnings volatility, intense competitive pressure, or low profitability are more likely to adopt such concealment strategies.

### 2. **"Information Positioning Score": Revealing the Level of Information Disclosure Candor**

The research team developed the **Information Positioning Score** to measure the transparency of disclosed information:

- **High-scoring companies**: Mature, large enterprises tend to position important information upfront, demonstrating higher transparency.
- **Low-scoring companies**: Companies with losses or volatile earnings tend to position key information later, reducing disclosure transparency.

### 3. **Importance Ranking of Annual Report Sections**

Model analysis reveals the most and least important annual report sections that investors focus on:

- **Most Important Sections**:
  - **Item 7**: Management's Discussion and Analysis (MD&A)
  - **Item 8**: Financial Statements and Supplementary Notes
  - **Item 1**: Business Description
  - **Item 1A**: Risk Factors
- **Least Important Sections**:
  - **Item 13**: Certain Relationships and Related Transactions
  - **Item 12**: Security Ownership
  - **Item 10**: Directors and Corporate Governance

### 4. **Low Attention to ESG Content**

Despite ESG (Environmental, Social, and Governance) issues receiving significant attention in public discourse, research shows that markets respond relatively weakly to ESG-related information, focusing more on profitability, liquidity, and financial performance.

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2024/12/22/1734887357477-30ebb089-dffb-4797-97b3-29a92d7d543c.png)

## Technical Details: How Do LLMs Parse Annual Reports?

### 1. **Data Preprocessing and Modeling**

- **Dataset**: 76,929 10-K annual reports from 1996 to 2023, divided into over 20 million paragraphs.
- **Text Processing**: Remove charts, tables, and HTML tags; normalize and segment the text.

### 2. **Attention Mechanism**

The research employs the attention mechanism from the Transformer architecture to capture investor focus through the following steps:

1. **Paragraph Embedding Vector Generation**: Using OpenAI's text-embedding-3-large model to convert each text paragraph into a 64-dimensional embedding vector.
2. **Dual-Layer Attention Mechanism**:
   - First Attention Layer: Analyzes the correlation between paragraphs and their context, adjusting the semantic understanding of each paragraph.
   - Second Attention Layer: Aggregates paragraph importance through weights to form document-level importance scores.

### 3. **Portfolio and Model Performance**

- **Performance Metrics**: Build portfolios based on important passages predicted by LLM and analyze their market performance.  
- **Model Performance**:
  - **Sharpe Ratio**: LLM model achieves **1.56**, significantly higher than the traditional Logit model's **1.08**, demonstrating AI's notable advantage in risk-adjusted returns.

## Regulatory Impact: Enhancing Information Transparency

### **Case Study 1: SEC S-K Rule Modernization Reform**

- In August 2021, the Securities and Exchange Commission (SEC) modernized MD&A disclosure rules, emphasizing forward-looking information and relevance.
- After the reform, the materiality score of the MD&A section increased by approximately **18.8%** compared to the financial statements section.

### **Case 2: Intervention Effect of SEC Comment Letters**

- Companies that received SEC comment letters showed an average **10%** improvement in their annual report scores in the following year.  
- This indicates that regulatory intervention helps enhance the transparency and market relevance of information disclosure.

## Strategic Information Positioning Analysis

Further research reveals that companies exhibit the following characteristics when arranging paragraph sequences:

- **Positive Information Frontloading**: Attracts investor attention and enhances market confidence.
- **Negative Information Backloading**: Diminishes negative impact and prevents direct investor focus.

### **Quantitative Strategy**

1. **Paragraph Scoring Formula**:
   - Calculate paragraph scores through attention weights to evaluate information importance.
   - Analyze the relationship between paragraph position and importance to reveal information ordering strategies.

2. **Information Position Scoring Formula**:
   - Combine paragraph scores with position indices to quantify company disclosure transparency:

   $$信息位置评分 = \sum_k [(1 - \frac{位置_k}{总段落数}) \times 重要性评分_k] $$

   - Higher scores indicate greater transparency in company disclosures.

3. **Research Findings**:
   - Large enterprises show higher transparency with fewer concealed negative messages.
   - Companies with high earnings volatility or under pressure tend to hide important content.

## Conclusions and Implications

### **Investors**

LLM technology helps investors quickly identify key sections in annual reports, improving analysis efficiency and decision-making quality.

### **Regulators**

Reasonable regulatory measures (such as S-K reforms and comment letter system) significantly improve the quality of annual report disclosures and market transparency.

### **Companies**

Although hiding bad news may be effective in the short term, transparent disclosure is better for building market trust and investor confidence in the long run.

> **"Not all paragraphs are equally important. Focusing on the most valuable information is key to improving information processing efficiency."**  
— Alex Kim, Research Author
---

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。欢迎加入**知识星球**获取**内部资料**。