---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# Still Writing Research Papers by Hand in 2025? Learn How to Auto-Generate Stock Research Papers Using ChatGPT

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

2025 will be a year when artificial intelligence is widely applied to finance and quantitative analysis. LLMQuant teaches you how to automatically generate academic papers for stock research using ChatGPT. This educational article is based on the paper "AI-Powered (Finance) Scholarship" by **Novy-Marx & Velikov (2024)**, introducing how to utilize Large Language Models (LLMs) to achieve automated academic research production, covering the entire process from data mining to paper writing. This article will also incorporate some mathematical formulas and discuss the applications and potential impacts of this technology in financial research, particularly in stock return prediction.

## 1. Background and Motivation

### 1.1 Large Language Models and Academic Research

In academic research, the traditional "research-theory-submission" process often requires researchers to spend considerable time and energy exploring data, formulating hypotheses, writing papers, and responding to peer review comments. With the rise of large language models like **ChatGPT and Claude**, AI is transforming this process:

1. **Automatic Generation of Research Ideas**: Using the "generative" capabilities of LLMs, potential research directions can be mined from vast literature or data.
2. **Accelerated Paper Writing**: LLMs can quickly generate initial paper drafts, abstracts, and other supporting textual materials based on specific prompts.
3. **Data Mining and Result Interpretation**: After "filtering" effective signals from large-scale data, LLMs can "automatically" match these signals with reasonable economic theoretical explanations.

However, this automation process also brings new challenges, such as the risk of "industrialized" **HARKing** (Hypothesizing After Results are Known) on a massive scale. The article emphasizes that the technology itself can both "improve research efficiency" and be "misused."

### 1.2 Stock Return Prediction and "Anomaly" Research

In finance, searching for "signals" or "factors" that can predict cross-sectional stock returns is a classic and important topic. Since Fama-French proposed their three-factor and five-factor models, hundreds or even thousands of "anomalies" have been discovered by academia.

- **What is an "Anomaly"**: It refers to a significant pattern of excess returns that cannot be easily explained by traditional risk factors under the classical Efficient Market Hypothesis (EMH) framework.
- **Common Methods**: Combining various accounting items from financial statements (such as balance sheets, income statements, etc.) in different ways (like ratios, differences, etc.), then observing the predictive power of these signals on future returns through portfolio formation or regression analysis.

Due to the massive number of possible signals, there are risks of **multiple testing** and **data snooping**. Traditional research requires rigorous statistical methods to reduce the false discovery rate, such as applying Fama-MacBeth adjustments to cross-sectional regressions and FDR (False Discovery Rate) corrections for multiple factors. **Novy-Marx & Velikov (2024)** proposed a systematic method called **"Assaying Anomalies"** to filter and evaluate discovered factors through multiple layers.

---

## 2. Overview of Automated Research Process

The paper introduces a complete "automated research production line" that covers:

1. **Large-scale Signal Mining**
2. **Statistical Significance and Robustness Testing**
3. **Using LLMs to Automatically Generate Research Hypotheses, Name Signals, and Write Complete Papers**

Below, we will provide detailed introductions to each component, with mathematical formulas inserted to enhance understanding.

---

### 2.1 Large-Scale Signal Mining

The research first extracted **31,460** potential accounting signals from the **COMPUSTAT** database, with each signal derived from combinations or differences of various accounting items. For example:

- **Ratio-type signals**:  
  $$
  \text{Signal}_{i,t} = \frac{\text{AccountingVar1}_{i,t}}{\text{AccountingVar2}_{i,t}}
  $$

- **Difference-type signals**:  
  $$
  \text{Signal}_{i,t} = \frac{\text{AccountingVar1}_{i,t} - \text{AccountingVar1}_{i,t-1}}{\text{AccountingVar2}_{i,t-1}}
  $$

Here, \(i\) represents the company, and \(t\) represents time (typically year or quarter). Subsequently, to ensure data quality, the research filtered these 31,460 initial signals through processes such as deduplication and elimination of items with severe missing data, ultimately resulting in **17,074** candidate signals.

---

### 2.2 Statistical Significance and Robustness Tests

To avoid generating numerous "false positive" signals, the research employs multiple methods to examine each signal:

1. **Portfolio Sorts**  
   - Sort into groups based on signal values from small to large (e.g., 5 groups, 10 groups), and examine the performance differences in future returns across groups.  
   - Use traditional **t-statistics** to determine whether return differences between groups are significant:  
     $$
     t = \frac{\overline{r}_\text{High} - \overline{r}_\text{Low}}{\sqrt{\mathrm{Var}\bigl(\overline{r}_\text{High} - \overline{r}_\text{Low}\bigr)}}
     $$  

2. **Factor Model Regression**  
   - Perform multi-factor regression on excess returns (e.g., Fama-French 6-factor model) to determine whether the signal remains statistically significant after controlling for existing risk factors:  
     $$
     r_{i,t} - r_{f,t}
     = \alpha
       + \beta_1 \cdot \text{MKT}_{t}
       + \beta_2 \cdot \text{SMB}_{t}
       + \cdots
       + \beta_6 \cdot \text{Factor6}_{t}
       + \epsilon_{i,t}
     $$  
   - If the estimated \(\alpha\) remains significantly positive or negative, it indicates the signal contains additional information content.

3. **"Assaying Anomalies" Protocol**  
   - **Novy-Marx & Velikov (2024)** introduced a systematic "assaying" process that compares each signal against hundreds of existing anomalies in the literature to see if it can succeed in a series of rigorous robustness tests and differentiation tests from "similar signals."

Ultimately, very few signals pass all tests, with only **96** remaining. These signals are considered to have genuine potential for predicting cross-sectional returns.

---

### 2.3 Using LLMs to Automatically Generate Papers

After completing the empirical analysis, researchers used LLMs such as **GPT-3.5-turbo** or **Claude 3.5-Sonnet** to automatically write papers based on these 96 "surviving" signals. This includes:

1. **Naming System**  
   - Prompting LLMs to generate academic "signal names" such as *Operating Liquidity Margin*, *Tax Efficiency*, etc., avoiding generic terms like "ratio" or "difference".  
2. **Paper Body Generation**  
   - Following pre-designed prompts, LLMs generate complete paper texts including **abstract, introduction, data methodology, results, and conclusion**.  
   - The introduction section "fabricates" or cites some real literature to construct theoretical motivation, with moderate embellishment.  
3. **Large-scale Batch Production**  
   - For each signal, automatically generate 3 versions of complete papers (with different theoretical explanations), totaling **288 papers**. This can be completed in an extremely short time, equivalent to an unimaginable "paper production line" compared to traditional research methods.

While demonstrating AI's potential, this also emphasizes its potential risks, such as **"Industrial HARKing"** - writing various rationalizations after seeing significant results, neglecting the pursuit of genuine economic mechanisms.

---

## 3. Key Findings and Implications

### 3.1 Efficiency and Scale

- **Extremely Efficient**: Traditional academic papers often require months or even years of incubation and writing, but through AI automation, once the data mining and statistical analysis processes are completed, the generation phase can produce large quantities of "academic papers" in just minutes.
- **Potential Abuse**: Without additional quality oversight, this method could lead to a flood of low-quality or highly repetitive papers, seriously impacting the traditional peer review system.

### 3.2 Researcher Reputation and Peer Review

- **Reputation Mechanism**: Researchers in finance and other disciplines often rely on consistently high-quality research to build academic influence. **Short-term pursuit of quantity** may not lead to genuine academic standing.  
- **Peer Review Pressure**: When large numbers of "automated papers" flood journals, reviewers and editors face a significant burden of discrimination. How to quickly assess paper quality and how to prevent "fake citations" or "self and mutual citations" have become new challenges.

### 3.3 Evolution of the "Hypothesis-Empirical" Paradigm

- In the traditional paradigm, researchers typically first propose hypotheses based on economic principles, then conduct data testing. In current processes, the approach of "first mining data to discover patterns, then using AI to generate hypotheses" is becoming increasingly prevalent.
- **Does this truly violate scientific methodology?** In fact, historically, many important discoveries were not made by first having a complete theory followed by verification. The real question is: **how to ensure that post-hoc hypotheses are not merely "hindsight wisdom" but possess extensible or predictive capabilities.**

---

## 4. Mathematical Example: How to Evaluate the Validity of "Automated Hypotheses"

Suppose we evaluate the impact of an automatically generated signal 
$$
\text{SIGNAL}_{i,t-1}
$$
on next-period returns
$$
r_{i,t}
$$
within the traditional "Fama-MacBeth" regression framework:

$$
r_{i,t}
= \alpha_t
+ \beta_t \cdot \text{SIGNAL}_{i,t-1}
+ \gamma_t \cdot \mathbf{X}_{i,t-1}
+ \epsilon_{i,t},
$$

where
$$
\mathbf{X}_{i,t-1}
$$
is a set of control variables or other classic factors (such as SIZE, BM, MOM, RMW, CMA, etc.).

1. **Cross-sectional Regression**: Perform cross-sectional regression for each period \(t\) to obtain a series of
$$
\hat{\beta}_t
$$.
2. **Time Series Mean and Variance**:
   $$
   \overline{\beta} = \frac{1}{T}\sum_{t=1}^{T} \hat{\beta}*t,
   \quad
   SE(\overline{\beta}) = \sqrt{\frac{1}{T(T-1)}\sum*{t=1}^{T} \Bigl(\hat{\beta}_t - \overline{\beta}\Bigr)^2}.
   $$

If the final
$$
  \text{Signal}_{i,t} = \frac{\text{AccountingVar1}_{i,t} - \text{AccountingVar1}_{i,t-1}}{\text{AccountingVar2}_{i,t-1}}
  $$0
is significantly greater than zero and the t-statistic is also significant, we can consider that the signal has predictive power for cross-sectional returns.

However, if
$$
\text{SIGNAL}_{i,t-1}
$$
is obtained through blind data mining from tens of thousands of variables, theoretically, multiple testing corrections should be applied; otherwise, we might underestimate the false positive probability. This issue becomes even more prominent in AI-automated mass paper production, therefore both **statistical significance** and **economic interpretation** must undergo dual scrutiny.

---

## 5. Risks and Prospects

1. **Academic Integrity**:  
   - Large-scale automated paper generation may lead to **widespread "fabricated literature"** or **self-citation manipulation**, affecting academia's evaluation of quality and originality.  
   - Need to establish **citation identification and verification systems**, similar to plagiarism detection tools or database validation, to reduce the harm of LLM "hallucinated citations".

2. **Peer Review Reform**:  
   - May need more explicit **review standards**, such as requiring authors (or AI) to **automatically submit retrievable data and code with paper submissions** for quick replication and verification of research results.  
   - Increase requirements for innovation in **economic mechanisms**, rather than just satisfying statistical significance.

3. **Future Research Directions**:  
   - As **LLMs** continue to iterate, researchers can integrate **automated verification modules**, such as automated verification of reference authenticity and automatic assessment of theoretical consistency.  
   - Develop "AI laboratories" for financial research—providing comprehensive "one-stop" services from big data cleaning, factor detection, to paper formatting, but requiring stricter supervision and review mechanisms.

---

## 6. Conclusion

**Novy-Marx & Velikov (2024)**'s research demonstrates a new landscape of AI technology in financial research:
- Through large-scale mining of accounting data, thousands of candidate signals can be screened in a short time;
- Using new testing protocols and multi-factor models to "separate the wheat from the chaff";
- Finally, having LLMs generate "academic papers" at scale for the "surviving" signals, including abstract economic theoretical motivations and paradigms.

While bringing a **qualitative leap** to academic research, it also poses new serious challenges to **academic integrity**, **research quality**, and **peer review**. Machines can help us "discover" and "explain" anomalies more quickly, but only the human academic community can determine which findings and explanations truly advance the frontiers of financial knowledge.

In the future, academia may need to establish a new set of standards to balance research efficiency with academic rigor. At this critical moment of transformation, we need to be clear about our principles: **while embracing technology, we cannot abandon our commitment to academic truth and research quality**.

---

## References (Examples)

- Chen, A. Y., Lopez-Lira, A. & Zimmermann, T. (2024). *Does peer-reviewed research help predict stock returns? Working Paper.*  
- Fama, E. F. & French, K. R. (2018). *Choosing factors.* Journal of Financial Economics, 128(2), 234–252.  
- Kerr, N. L. (1998). *HARKing: Hypothesizing After the Results are Known.* Personality and Social Psychology Review, 2(3), 196–217.  
- Novy-Marx, R. & Velikov, M. (2024). *Assaying Anomalies.* Working Paper.  
- Yan, X. & Zheng, L. (2017). *Fundamental analysis and the cross-section of stock returns: A data-mining approach.* The Review of Financial Studies, 30(4), 1382–1423.  

For more details, access to original papers and **code**, welcome to join **LLMQuant Knowledge Circle**.

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。