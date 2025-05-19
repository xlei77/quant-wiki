---
{}
---

Here's the English translation of the provided Chinese text, maintaining technical accuracy, markdown formatting, math expressions, and code elements:

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Quantitative Frontier | Using Large Language Models to Uncover Bad News Hidden in Corporate Annual Reports

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## Introduction: Secrets Hidden in Annual Reports

**Corporate annual reports (10-K)** are the core source of information for investors to obtain a company's financial and operational status. However, research from the University of Chicago's Booth School of Business found that many companies deliberately conceal unfavorable news using text and paragraph ordering techniques in their annual reports. This article reveals these hidden strategies through large language models (LLMs) and attention mechanisms, and demonstrates how to improve information interpretation efficiency using AI tools.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2024/12/22/1734887309221-84b023dd-771a-4cdc-8eb1-e1a3bdeb4ea9.png)

## Research Background and Core Questions

For years, market participants have been trying to understand: which information in annual reports truly drives stock price fluctuations? While quantitative data (such as revenue, profit margins) is relatively straightforward, qualitative data (such as changes in business models, competitive landscape, strategic initiatives) is often difficult to quantify and analyze. The University of Chicago team developed a novel method by introducing LLMs with attention mechanisms to directly capture what investors focus on most in annual reports.

The research team's core objectives were to answer the following questions:

1. **What information in annual reports does the market focus on?**
2. **Do companies intentionally arrange paragraph order to manipulate investor attention?**
3. **How can AI models extract key information from complex text?**

## Research Findings

### 1. **Analysis of Strategies to Hide Bad News**

- **Information Ordering Strategy**: Companies place negative information in the latter part of the Management's Discussion and Analysis (MD&A) section, rather than at the beginning of the report, reducing attention to negative information.
- **Concealment Conditions**: Companies with high earnings volatility, competitive pressure, or low profitability are more likely to adopt this concealment strategy.

### 2. **"Information Positioning Score": Revealing the Frankness of Information Disclosure**

The research team developed an **Information Positioning Score** to measure the transparency of disclosed information:

- **High-scoring Companies**: Mature, large enterprises tend to prioritize important information, demonstrating higher transparency.
- **Low-scoring Companies**: Loss-making or high earnings volatility companies tend to place key information later, reducing disclosure transparency.

### 3. **Importance Ranking of Annual Report Sections**

The model analysis found that the most and least important annual report sections for investors are:

- **Most Important Sections**:
  - **Item 7**: Management's Discussion and Analysis (MD&A)
  - **Item 8**: Financial Statements and Supplementary Data
  - **Item 1**: Business Description
  - **Item 1A**: Risk Factors
- **Least Important Sections**:
  - **Item 13**: Certain Relationships and Related Transactions
  - **Item 12**: Security Ownership of Certain Beneficial Owners and Management
  - **Item 10**: Directors and Executive Officers

### 4. **Low Attention to ESG Content**

Despite the high public attention to ESG (Environmental, Social, and Governance) issues, the research shows that the market reacts weakly to ESG-related information, focusing more on profitability, liquidity, and financial performance.

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2024/12/22/1734887357477-30ebb089-dffb-4797-97b3-29a92d7d543c.png)

## Technical Details: How Do LLMs Parse Annual Reports?

### 1. **Data Preprocessing and Modeling**

- **Dataset**: 76,929 10-K annual reports from 1996 to 2023, divided into over 20 million paragraphs.
- **Text Processing**: Removed charts, tables, and HTML tags; normalized and segmented the text.

### 2. **Attention Mechanism**

The research uses the attention mechanism from the Transformer architecture to capture investor focus through the following steps:

1. **Paragraph Embedding Vector Generation**: Using OpenAI's text-embedding-3-large model to convert each paragraph into a 64-dimensional embedding vector.
2. **Two-layer Attention Mechanism**:
   - First Layer Attention: Analyzes the relevance between paragraphs and context, adjusting the semantic understanding of each paragraph.
   - Second Layer Attention: Aggregates paragraph importance weights to form document-level importance scores.

### 3. **Portfolio and Model Performance**

- **Performance Metrics**: Constructed portfolios based on LLM-predicted important paragraphs and analyzed their market performance.
- **Model Performance**:
  - **Sharpe Ratio**: The LLM model achieved **1.56**, significantly higher than the traditional Logit model's **1.08**, demonstrating AI's significant advantage in risk-adjusted returns.

## Regulatory Impact: Enhancing Information Transparency

### **Case 1: SEC S-K Rule Modernization Reform**

- In August 2021, the U.S. Securities and Exchange Commission (SEC) modernized the MD&A disclosure rules, emphasizing forward-looking and information relevance.
- After the reform, the importance score of the MD&A section increased by about **18.8%** compared to the financial statement section.

### **Case 2: Intervention Effect of SEC Comment Letters**

- Companies that received SEC comment letters saw an average increase of **10%** in the scores of relevant annual report sections the following year.
- This indicates that regulatory intervention helps improve the transparency and market relevance of information disclosure.

## Strategic Information Positioning Analysis

The research further reveals that companies have the following characteristics when arranging paragraph order:

- **Prioritizing Positive Information**: Attracts investor attention and increases market trust.
- **Postponing Negative Information**: Downplays negative impacts and avoids direct investor focus.

### **Quantitative Strategy**

1. **Paragraph Scoring Formula**:
   - Calculate paragraph scores through attention weights to assess information importance.
   - Analyze the relationship between paragraph position and importance to reveal information ordering strategies.

2. **Information Positioning Score Formula**:
   - Combine paragraph scores with position indices to quantify company disclosure transparency:

   $$信息位置评分 = \sum_k [(1 - \frac{位置_k}{总段落数}) \times 重要性评分_k] $$

   - Higher scores indicate more transparent company information disclosure.

3. **Research Findings**:
   - Large enterprises have higher transparency and less concealment of negative news.
   - Companies with high earnings volatility or facing pressure tend to hide important content.

## Conclusions and Implications

### **For Investors**

LLM technology helps investors quickly identify key paragraphs in annual reports, improving analysis efficiency and decision quality.

### **For Regulators**

Appropriate regulatory measures (such as S-K reform and comment letter system) significantly improve annual report disclosure quality and market transparency.

### **For Companies**

While hiding bad news may be effective in the short term, transparent disclosure is more conducive to building market trust and investor confidence in the long run.

> **"Not all paragraphs are equally important. Focusing on the most valuable information is key to improving information processing efficiency."**
— Alex Kim, Research Author

Here's the English translation, maintaining the technical accuracy, formatting, and style of the original text:

## About LLMQuant

LLMQuant is a cutting-edge community composed of individuals from the world's top universities and quantitative finance professionals, dedicated to exploring the infinite possibilities in the fields of Artificial Intelligence (AI) and Quantitative Finance (Quant). Our team members come from renowned global institutions such as the University of Cambridge, University of Oxford, Harvard University, ETH Zurich, Peking University, University of Science and Technology of China, and other world-class universities. Our external advisors are from leading companies including Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top-tier private equity firms in China. We welcome you to join our **Knowledge Planet** to access **internal resources**.