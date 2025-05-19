---
{}
---

# Replacing Quantitative Researchers? Using ChatGPT o1 to Automatically Backtest Trading Algorithms from Quantitative Papers

To better understand the community's AI+Quantitative projects, here we explore a novel AI-assisted workflow **aimed at using ChatGPT o1 to automatically generate code from quantitative finance articles and backtest trading algorithms using QuantConnect**. To explore the latest frontiers of AI and quantitative integration, welcome to follow our public account and join the LLMQuant community.

Quantitative finance heavily relies on data-driven strategies derived from extensive research. However, translating insights from dense academic papers into executable trading algorithms can be both time-consuming and error-prone. While creating a production-ready solution immediately might not be realistic, our goal is to generate boilerplate code for QuantConnect within seconds. This initial code can help determine whether an article presents a promising strategy worth further investigation or should be disregarded.

## Article Introduction

We will provide detailed instructions on how to run this code and present our preliminary testing results. For foundational principles, this article serves as a complement to my previous work "LLM Pair Programming in Algorithmic Trading." Notably, our approach adopts a linear workflow, temporarily setting aside the dual-agent architecture. This tool not only extracts and summarizes key trading strategies and risk management techniques from PDF articles but also generates syntactically correct QuantConnect Python code with easy-to-review syntax highlighting.

Initial testing indicates that the generated code is error-free, although achieving 100% accuracy across all tests has not yet been realized. The NLP components of the tool employ basic techniques that can be further refined in the future. However, I chose to release the code quickly as a proof of concept in this rapidly evolving field. The project is ongoing and will continue to improve. Let's consider what I'm describing here today as its beta version.

## How It Works

The core of this automation is the `ArticleProcessor` class, which organizes the entire workflow from PDF extraction to code generation. Here is a breakdown of its functionality:

### 1. Using pdfplumber for PDF Text Extraction

The process begins with using the pdfplumber library to load and extract text from PDF files. Unlike other PDF parsing tools, pdfplumber offers superior accuracy, particularly for complex layouts commonly found in academic articles.

```python
def load_pdf(self, pdf_path: str) -> str:
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        logging.info("PDF加载成功。")
        return text
    except Exception as e:
        logging.error(f"无法加载PDF：{e}")
        return ""
```

### 2. Text Preprocessing

Once text has been extracted, cleaning and preprocessing become crucial. This includes using regular expressions to remove URLs, headers, footers, standalone numbers (such as page numbers), and other irrelevant content.

```python
def preprocess_text(self, text: str) -> str:
    try:
        text = re.sub(r'https?://\S+', '', text)
        text = re.sub(r'Electronic copy available at: .*', '', text)
        text = re.sub(r'^\d+\s*$', '', text, flags=re.MULTILINE)
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'^\s*(Author|Title|Abstract)\s*$', '', text, flags=re.MULTILINE | re.IGNORECASE)
        text = text.strip()
        logging.info("文本预处理成功。")
        return text
    except Exception as e:
        logging.error(f"无法预处理文本：{e}")
        return ""
```

### 3. Using SpaCy for Heading Detection

Understanding the structure of an article is crucial. Using SpaCy's NLP capabilities, the tool identifies section headings based on heuristic methods such as sentence length and heading format. This segmentation helps organize content more effectively for analysis.

```python
def detect_headings(self, text: str) -> List[str]:
    try:
        doc = self.nlp(text)
        headings = []
        for sent in doc.sents:
            sent_text = sent.text.strip()
            if len(sent_text.split()) < 10 and sent_text.istitle():
                headings.append(sent_text)
        logging.info(f"检测到{len(headings)}个标题。")
        return headings
    except Exception as e:
        logging.error(f"无法检测标题：{e}")
        return []
```

### 4. Section Splitting and Keyword Analysis

After identifying the headings, the text is split into corresponding sections. Then, the tool performs keyword analysis, classifying sentences into `trading_signal` and `risk_management`. This classification is based on predefined lists of relevant keywords, ensuring that only relevant information is processed further.

```python
def keyword_analysis(self, sections: Dict[str, str]) -> Dict[str, List[str]]:
    keyword_map = defaultdict(list)
    
    risk_management_keywords = [
        "drawdown", "volatility", "reduce", "limit", "risk", "risk-adjusted", 
        "maximal drawdown", "market volatility", "bear markets", "stability", 
        "sidestep", "reduce drawdown", "stop-loss", "position sizing", "hedging"
    ]
    trading_signal_keywords = [
        "buy", "sell", "signal", "indicator", "trend", "SMA", "moving average", 
        "momentum", "RSI", "MACD", "bollinger bands", "Rachev ratio", "stay long", 
        "exit", "market timing", "yield curve", "recession", "unemployment", 
        "housing starts", "Treasuries", "economic indicator"
    ]
    
    irrelevant_patterns = [
        r'figure \d+',  
        r'\[\d+\]',     
        r'\(.*?\)',     
        r'chart',       
        r'\bfigure\b',  
        r'performance chart',  
        r'\d{4}-\d{4}',  
        r'^\s*$'        
    ]
    
    processed_sentences = set()
    
    for section, content in sections.items():
        doc = self.nlp(content)
        for sent in doc.sents:
            sent_text = sent.text.lower().strip()
            
            if any(re.search(pattern, sent_text) for pattern in irrelevant_patterns):
                continue
            if sent_text in processed_sentences:
                continue
            processed_sentences.add(sent_text)
            
            if any(kw in sent_text for kw in trading_signal_keywords):
                keyword_map['trading_signal'].append(sent.text.strip())
            elif any(kw in sent_text for kw in risk_management_keywords):
                keyword_map['risk_management'].append(sent.text.strip())
    
    for category, sentences in keyword_map.items():
        unique_sentences = list(set(sentences))
        keyword_map[category] = sorted(unique_sentences, key=len)
    
    logging.info("关键词分析完成。")
    return keyword_map
```

### 5. Using OpenAI's GPT-4 to Generate Summaries and QuantConnect Code

Leveraging the powerful capabilities of OpenAI's GPT-4, the tool generates concise summaries of strategies and risk management techniques. Even more impressively, it transforms these insights into fully functional QuantConnect Python algorithms, ensuring they follow best practices and maintain syntactic correctness.

```python
def generate_qc_code(self, extracted_data: Dict[str, List[str]]) -> str:
    trading_signals = '\n'.join(extracted_data.get('trading_signal', []))
    risk_management = '\n'.join(extracted_data.get('risk_management', []))

    prompt = f"""
    你是一位专家级的QuantConnect算法开发者。将以下交易策略和风险管理描述转换为完整、无错误的QuantConnect Python算法。

    ### 交易策略：
    {trading_signals}

    ### 风险管理：
    {risk_management}

    ### 要求：
    1. **Initialize方法**：
        - 设置开始和结束日期。
        - 设置初始资金。
        - 定义选股逻辑。
        - 初始化所需指标。
    2. **OnData方法**：
        - 根据指标实施买/卖逻辑。
        - 确保指标正确更新。
    3. **风险管理**：
        - 实施15%的回撤限制。
        - 应用所描述的头寸规模或止损机制。
    4. **确保合规**：
        - 仅使用QuantConnect支持的指标和方法。
        - 代码必须语法正确且无错误。

    ### 示例结构：
    ```python
    from AlgorithmImports import *

    class MyAlgorithm(QCAlgorithm):
        def Initialize(self):
            self.SetStartDate(2020, 1, 1)
            self.SetEndDate(2023, 1, 1)
            self.SetCash(100000)
            # Define stock selection, indicators, etc.

        def OnData(self, data):
            # Trading logic

        def OnEndOfDay(self):
            # Risk management
    ```

    ### 生成的代码：
    ```
    # LLM will generate code after this line
    ```
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一名专门用Python生成QuantConnect算法的助理。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2500,
            temperature=0.3,
            n=1
        )
        generated_code = response['choices'][0]['message']['content'].strip()
        code_match = re.search(r'```python(.*?)```', generated_code, re.DOTALL)
        if code_match:
            generated_code = code_match.group(1).strip()
        logging.info("LLM生成了代码。")
        return generated_code
    except Exception as e:
        logging.error(f"无法生成代码：{e}")
        return ""
```

### 6. Display Results Using Tkinter and Pygments

To provide a user-friendly experience, the tool uses Tkinter to display article summaries and generated code in separate windows. The Pygments library enhances readability by adding syntax highlighting to Python code.

```python
def display_summary_and_code(self, summary: str, code: str):
    # 创建主Tkinter根
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 摘要窗口
    summary_window = tk.Toplevel()
    summary_window.title("文章摘要")
    summary_window.geometry("800x600")

    summary_text = scrolledtext.ScrolledText(summary_window, wrap=tk.WORD, font=("Arial", 12))
    summary_text.pack(expand=True, fill='both')
    summary_text.insert(tk.END, summary)
    summary_text.configure(state='disabled')  # 设为只读

    # 代码窗口
    code_window = tk.Toplevel()
    code_window.title("生成的QuantConnect代码")
    code_window.geometry("1000x800")

    code_text = scrolledtext.ScrolledText(code_window, wrap=tk.NONE, font=("Consolas", 12), bg="#2B2B2B", fg="#F8F8F2")
    code_text.pack(expand=True, fill='both')

    # 应用语法高亮
    self.apply_syntax_highlighting(code, code_text)

    code_text.configure(state='disabled')  # 设为只读

    # 启动Tkinter事件循环
    root.mainloop()
```

### 7. Initial Testing

We used L. Durian and R. Vojtko's article "Using Market Timing Strategy to Avoid Bear Markets" from Quantpedia. The output results are as follows:

![View of code and summary](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2024/10/12/1728730721023-f1a5f810-c487-4c2e-a6a4-acc2b63df7a8.png)

The code generated during the first run produced the following backtest results:

![Backtest results of generated code - powered by QuantConnect](https://cdn-images-1.readmedium.com/v2/resize:fit:800/1*X_7QwYDI7EZOvwRS1Y8UIg.png)

We can see that the algorithm maintained a cash position in 2020, which, as expected, helped avoid the bear market during the COVID-19 pandemic. The article indeed seems to have successfully managed bear market avoidance and is definitely worth further investigation.

## Conclusion

The automation of transforming quantitative finance research into executable trading algorithms can significantly improve efficiency. Through the integration of powerful libraries such as pdfplumber, SpaCy, OpenAI's GPT-4, Tkinter, and Pygments, this Python-based tool provides a seamless solution that bridges the gap between research and implementation.

---

**Observations**

- We believe that the current process of converting financial papers into trading algorithms is time-consuming and error-prone, emphasizing the necessity for automation.
- The preliminary nature of the tool is highlighted, with the authors acknowledging that while the generated code is largely error-free, achieving complete accuracy remains a goal for future development.
- The tool's ability to classify sentences into trading signals and risk management is viewed as a key feature, ensuring that only relevant information is used for code generation.
- The use of GPT-4 for code generation is considered particularly innovative, demonstrating the potential of AI in quantitative finance.
- We are optimistic about the project's continuous improvement and its potential to become a valuable asset for quantitative analysts and traders.
- The use of Tkinter to create a user-friendly interface and Pygments for syntax highlighting demonstrates attention to user experience and the readability of generated code.