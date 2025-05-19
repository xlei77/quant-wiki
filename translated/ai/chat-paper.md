---
{}
---

Here's the English translation of the provided Chinese text, maintaining technical accuracy, markdown formatting, math expressions, and code elements:

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Still Handwriting Papers in 2025? Learn How to Use ChatGPT to Automatically Generate Academic Papers on Stock Research

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

2025 will be a year when artificial intelligence is widely applied to finance and quantitative analysis. LLMQuant teaches you how to use ChatGPT to automatically generate academic papers on stock research. This article is based on the paper "AI-Powered (Finance) Scholarship" by **Novy-Marx & Velikov (2024)**, introducing how to use large language models (LLMs) to achieve automated academic research production, including the entire process from data mining to paper writing. This article will also incorporate some mathematical formulas and discuss the application and potential impact of this technology in financial research, especially in stock return prediction.

## 1. Background and Motivation

### 1.1 Large Language Models and Academic Research

In the field of academic research, the traditional "research-theory-submission" process often requires researchers to spend a lot of time and energy exploring data, proposing hypotheses, writing papers, and responding to review comments. With the rise of large language models such as **ChatGPT and Claude**, AI is changing this process:

1. **Automatic generation of research ideas**: Using the "generative" capability of LLMs, potential research ideas can be mined from massive literature or data.
2. **Accelerated paper writing**: LLMs can quickly generate initial drafts of papers, abstracts, and other auxiliary textual materials based on specific prompts.
3. **Data mining and result interpretation**: After "filtering" effective signals from large-scale data, LLMs can also "automatically" match these signals with reasonable economic theory explanations.

However, this automation process also brings new challenges, such as the risk of "industrialization" of **HARKing** (Hypothesizing After Results are Known) on a large scale. The article emphasizes that the technology itself can both "improve research efficiency" and be "misused".

### 1.2 Stock Return Prediction and "Anomaly" Research

In finance, finding "signals" or "factors" that can predict cross-sectional stock returns is a classic and important topic. Since the three-factor and five-factor models proposed by Fama-French, hundreds or even thousands of "anomalies" have been discovered by academia.

- **What is an "anomaly"**: It refers to a significant pattern of excess returns that cannot be easily explained by traditional risk factors under the classic Efficient Market Hypothesis (EMH) framework.
- **Common approaches**: By combining various accounting items (such as ratios, differences, etc.) from financial statements (such as balance sheets, income statements, etc.), and then observing the predictive power of these signals on future returns through portfolio or regression methods.

Due to the risks of **multiple testing** and **data snooping** brought by massive possible signals, traditional research requires strict statistical methods to reduce the false discovery rate, such as Fama-MacBeth adjustments for cross-sectional regressions, FDR (False Discovery Rate) corrections for multi-factor models, etc. **Novy-Marx & Velikov (2024)** proposed a systematic method called **"Assaying Anomalies"** to filter and evaluate the mined factors layer by layer.

---

## 2. Overview of Automated Research Process

The paper introduces a complete "automated research production line", covering:

1. **Large-scale signal mining**
2. **Statistical significance and robustness tests**
3. **Using LLMs to automatically generate research hypotheses, name signals, and write complete papers**

The following will provide a detailed introduction to each link, with some mathematical formulas inserted to deepen understanding.

---

### 2.1 Large-scale Signal Mining

The research first extracted **31,460** potential accounting signals from the **COMPUSTAT** database, each signal coming from combinations or differences of different accounting items. For example:

- **Ratio-type signals**:
  $$
  \text{Signal}_{i,t} = \frac{\text{AccountingVar1}_{i,t}}{\text{AccountingVar2}_{i,t}}
  $$

- **Difference-type signals**:
  $$
  \text{Signal}_{i,t} = \frac{\text{AccountingVar1}_{i,t} - \text{AccountingVar1}_{i,t-1}}{\text{AccountingVar2}_{i,t-1}}
  $$

Here, \(i\) represents the company, and \(t\) represents time (usually year or quarter). Subsequently, to ensure data quality, the research filtered these 31,460 initial signals, such as deduplication and excluding items with severe data missing, finally leaving **17,074** candidate signals.

---

### 2.2 Statistical Significance and Robustness Tests

To avoid a large number of "false positive" signals, the research uses multiple methods to examine each signal:

1. **Portfolio Sorts**
   - Group by signal values from small to large (e.g., 5 groups, 10 groups), and examine the performance differences in future returns between different groups.
   - Use traditional **t-statistics** to determine if the return differences between groups are significant:
     $$
     t = \frac{\overline{r}_\text{High} - \overline{r}_\text{Low}}{\sqrt{\mathrm{Var}\bigl(\overline{r}_\text{High} - \overline{r}_\text{Low}\bigr)}}
     $$

2. **Factor Model Regression**
   - Perform multi-factor regression on excess returns (e.g., Fama-French 6-factor model) to determine if the signal still has statistical significance after controlling for existing risk factors:
     $$
     r_{i,t} - r_{f,t}
     = \alpha
       + \beta_1 \cdot \text{MKT}_{t}
       + \beta_2 \cdot \text{SMB}_{t}
       + \cdots
       + \beta_6 \cdot \text{Factor6}_{t}
       + \epsilon_{i,t}
     $$
   - If the estimated \(\alpha\) is still significantly positive or negative, it indicates that the signal contains additional information.

3. **"Assaying Anomalies" Protocol**
   - **Novy-Marx & Velikov (2024)** introduced a systematic "assay" process, comparing each signal with hundreds of existing anomalies in the literature to see if it can win in a series of stringent robustness and differentiation tests from "similar signals".

In the end, very few signals can pass all tests, with only **96** remaining. These signals are considered to have real potential in predicting cross-sectional returns.

---

### 2.3 Using LLMs to Automatically Generate Papers

After completing the empirical analysis, researchers use LLMs such as **GPT-3.5-turbo** or **Claude 3.5-Sonnet** to automatically write papers based on these 96 "surviving" signals. This mainly includes:

1. **Naming System**
   - Prompt the LLM to generate academic "signal names", such as *Operating Liquidity Margin*, *Tax Efficiency*, etc., avoiding the use of overly generic terms like "ratio" or "difference".
2. **Paper Body Generation**
   - According to pre-designed prompts, LLMs will generate complete paper text including **abstract, introduction, data methods, results, and conclusion**.
   - The introduction part will "automatically fabricate" or cite some real literature to construct theoretical motivation and make appropriate embellishments.
3. **Large-scale Batch Production**
   - For each signal, automatically generate 3 versions of complete papers (with different angles of theoretical explanations), totaling **288 papers**. This can be completed in an extremely short time, equivalent to an unimaginable "paper assembly line" in the traditional research model.

Here is the English translation of the Chinese text, maintaining technical accuracy, markdown formatting, and mathematical expressions:

This move, while demonstrating the potential of AI, also highlights the risks it may bring, such as **"industrialized HARKing"**, which involves writing various rationalizations after seeing significant results, ignoring the pursuit of true economic mechanisms.

---

## 3. Key Findings and Impacts

### 3.1 Efficiency and Scale

- **Extremely Efficient**: Traditional academic papers often require months or even years of incubation and writing, while through AI automation, once the data mining and statistical analysis processes are completed, the generation phase can produce large quantities of "academic papers" in just minutes.
- **Potential Abuse**: Without additional quality supervision, this method could lead to a flood of low-quality or highly repetitive papers, seriously impacting the traditional peer review system.

### 3.2 Researcher Reputation and Peer Review

- **Reputation Mechanism**: Researchers in finance or other disciplines often rely on consistently high-quality research to establish academic influence. **Short-term success based on quantity** may not lead to true academic standing.
- **Pressure on Peer Review**: When a large number of "automated papers" flood into journals, reviewers and editors face a huge burden of discrimination. How to quickly judge paper quality and how to prevent "fake citations" or "self-citation and mutual citation" become new issues.

### 3.3 Evolution of the "Hypothesis-Empirical" Paradigm

- In the traditional paradigm, researchers often first propose hypotheses based on economic principles and then conduct data tests. In the current process, "first mining data to discover patterns, then using AI to create hypotheses" is becoming increasingly popular.
- **Does this truly violate the scientific method?** In fact, many important discoveries in history were not made with a complete theory first and then tested. The real question is: **How to ensure that post-hoc hypotheses are not just "hindsight wisdom" but have expandable or predictable capabilities.**

---

## 4. Mathematical Example: How to Evaluate the Reasonability of "Automatic Hypotheses"

Suppose we evaluate the impact of an automatically generated signal $$
\text{SIGNAL}_{i,t-1}
$$ on next-period returns $$
r_{i,t}
$$ under the traditional "Fama-MacBeth" regression framework:

$$
r_{i,t}
= \alpha_t
+ \beta_t \cdot \text{SIGNAL}_{i,t-1}
+ \gamma_t \cdot \mathbf{X}_{i,t-1}
+ \epsilon_{i,t},
$$

where $$
\mathbf{X}_{i,t-1}
$$ is a set of control variables or other classic factors (such as SIZE, BM, MOM, RMW, CMA, etc.).

1. **Cross-sectional Regression**: Perform cross-sectional regression for each period \(t\) to obtain a series of $$
\hat{\beta}_t
$$.
2. **Time Series Mean and Variance**:
   $$
   \overline{\beta} = \frac{1}{T}\sum_{t=1}^{T} \hat{\beta}*t,
   \quad
   SE(\overline{\beta}) = \sqrt{\frac{1}{T(T-1)}\sum*{t=1}^{T} \Bigl(\hat{\beta}_t - \overline{\beta}\Bigr)^2}.
   $$

If the final $$
  \text{Signal}_{i,t} = \frac{\text{AccountingVar1}_{i,t} - \text{AccountingVar1}_{i,t-1}}{\text{AccountingVar2}_{i,t-1}}
  $$0 is significantly greater than zero and the t-statistic is also significant, then the signal can be considered to have predictive power for cross-sectional returns.

However, if $$
\text{SIGNAL}_{i,t-1}
$$ is obtained from blind data mining of tens of thousands of variables, theoretically, multiple testing correction should be done; otherwise, we may underestimate the probability of false positives. This point becomes more prominent in AI large-scale automated paper production, so a dual review of **statistical significance** and **economic explanation** is necessary.

---

## 5. Risks and Prospects

1. **Academic Integrity**:
   - Large-scale automatic generation of papers may lead to **widespread "fictitious literature"** or **self-citation manipulation**, affecting the academic community's assessment of quality and originality.
   - Need to establish a **citation identification and verification system**, similar to plagiarism detection tools or database verification, to reduce the harm of LLM "hallucination-type citations".

2. **Peer Review Reform**:
   - May need more explicit **review standards**, such as requiring authors (or AI) to **automatically attach searchable data and code when submitting papers** for quick replication and verification of research results.
   - Increase requirements for innovation in **economic mechanisms**, rather than just satisfying statistical significance.

3. **Future Research Directions**:
   - As **LLMs** further iterate, researchers can integrate **automatic verification modules**, such as automated checking of reference authenticity, automatic judgment of theoretical consistency.
   - Develop "AI laboratories" for financial research - providing a full suite of services from big data cleaning, factor detection, to paper formatting, but requiring stricter regulatory and review mechanisms.

---

## 6. Conclusion

The research by **Novy-Marx & Velikov (2024)** showcases a new landscape of AI technology in financial research:
- Through large-scale mining of accounting data, tens of thousands of candidate signals can be screened in a short time;
- Use new testing protocols and multi-factor models for "separating the wheat from the chaff";
- Finally, hand over the "surviving" signals to LLM for large-scale generation of "academic papers", including abstract economic theoretical motivations and paradigms.

While bringing a **qualitative leap** to academic research, it also poses new severe challenges to **academic integrity**, **research quality**, and **peer review**. Machines can help us "discover" and "explain" anomalies faster, but only the human academic community can decide which discoveries and explanations truly advance the frontiers of financial knowledge.

In the future, the academic community may need to construct a new set of standards to balance research efficiency and academic rigor. At this critical moment of transformation, we need to clarify principles: **While embracing technology, we cannot abandon our commitment to academic truth and research quality**.

---

## References (Examples)

- Chen, A. Y., Lopez-Lira, A. & Zimmermann, T. (2024). *Does peer-reviewed research help predict stock returns? Working Paper.*
- Fama, E. F. & French, K. R. (2018). *Choosing factors.* Journal of Financial Economics, 128(2), 234–252.
- Kerr, N. L. (1998). *HARKing: Hypothesizing After the Results are Known.* Personality and Social Psychology Review, 2(3), 196–217.
- Novy-Marx, R. & Velikov, M. (2024). *Assaying Anomalies.* Working Paper.
- Yan, X. & Zheng, L. (2017). *Fundamental analysis and the cross-section of stock returns: A data-mining approach.* The Review of Financial Studies, 30(4), 1382–1423.

For more details, to obtain the original paper and **code**, welcome to join the **LLMQuant Knowledge Planet**.

## About LLMQuant

LLMQuant is a cutting-edge community composed of a group of professionals from top universities and quantitative finance practitioners worldwide, dedicated to exploring the infinite possibilities in the fields of Artificial Intelligence (AI) and Quantitative Finance (Quant). Our team members come from world-renowned universities such as Cambridge University, Oxford University, Harvard University, ETH Zurich, Peking University, USTC, etc., and our external advisors are from top companies like Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading private equity firms in China.