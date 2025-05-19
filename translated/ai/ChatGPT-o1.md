---
{}
---

Here's the English translation of the provided Chinese text, maintaining technical accuracy, markdown formatting, math expressions, and code elements:

# Replacing Quantitative Researchers? Using ChatGPT o1 to Automatically Backtest Trading Algorithms from Quantitative Papers

To better understand the community's AI+Quantitative projects, we explore here a novel AI-assisted workflow **aimed at using ChatGPT o1 to automatically generate code from quantitative finance articles and use QuantConnect to automatically backtest trading algorithms**. To explore the latest frontiers of AI and quantitative integration, welcome to follow the public account and join the LLMQuant community.

Quantitative finance heavily relies on data-driven strategies derived from extensive research. However, translating insights from dense academic papers into executable trading algorithms can be both time-consuming and error-prone. While creating a production-ready solution immediately may not be realistic, our goal is to generate boilerplate code for QuantConnect within seconds. This initial code can help determine whether an article proposes a promising strategy worth further investigation or should be disregarded.

## Article Overview

We will detail how to run this code and showcase our preliminary tests. For foundational principles, this article serves as a complement to my previous work "LLM Pair Programming in Algorithmic Trading". Notably, our approach adopts a linear workflow, temporarily setting aside the dual-agent architecture. The tool not only extracts and summarizes key trading strategies and risk management techniques from PDF articles but also generates syntactically correct QuantConnect Python code with easy-to-review syntax highlighting.

Initial tests indicate that the generated code is error-free, although achieving 100% accuracy in all tests has not yet been realized. The NLP component of the tool employs basic techniques that can be further refined in the future. However, I chose to release the code promptly as a proof of concept for this rapidly evolving field. The project is ongoing and will be continuously improved. Let's consider what I describe here today as its beta version.

## How It Works

The automation's core is the `PDFToQuantConnectCode` class, which orchestrates the entire workflow from PDF extraction to code generation. Here's a breakdown of its functionality:

### 1. PDF Text Extraction Using pdfplumber

The process begins by loading and extracting text from PDF files using the pdfplumber library. Unlike other PDF parsing tools, pdfplumber offers superior accuracy, especially for complex layouts common in academic articles.

```python
import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages)
```

### 2. Text Preprocessing

Once the text is extracted, cleaning and preprocessing are crucial. This includes removing URLs, headers, footers, standalone numbers (like page numbers), and other irrelevant content using regular expressions.

```python
import re

def preprocess_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove standalone numbers (e.g., page numbers)
    text = re.sub(r'\n\d+\n', '\n', text)
    # Additional preprocessing steps...
    return text
```

### 3. Title Detection Using SpaCy

Understanding the article's structure is vital. Leveraging SpaCy's NLP capabilities, the tool identifies section titles based on heuristics such as sentence length and title formatting. This segmentation helps organize content more effectively for analysis.

```python
import spacy

nlp = spacy.load("en_core_web_sm")

def detect_titles(text):
    doc = nlp(text)
    titles = []
    for sent in doc.sents:
        if len(sent.text.split()) <= 5 and sent.text.isupper():
            titles.append(sent.text)
    return titles
```

### 4. Section Splitting and Keyword Analysis

After identifying titles, the text is split into corresponding sections. The tool then performs keyword analysis, categorizing sentences as `trading_signals` and `risk_management`. This categorization is based on predefined lists of relevant keywords, ensuring that only pertinent information is processed further.

```python
def split_sections(text, titles):
    sections = {}
    current_title = "Introduction"
    for line in text.split('\n'):
        if line in titles:
            current_title = line
            sections[current_title] = []
        else:
            sections[current_title].append(line)
    return sections

def analyze_keywords(sections):
    trading_signals = []
    risk_management = []
    # Logic to categorize sentences based on keywords
    return trading_signals, risk_management
```

### 5. Summary and QuantConnect Code Generation Using OpenAI's GPT-4

Leveraging the power of OpenAI's GPT-4, the tool generates concise summaries extracting strategies and risk management techniques. More impressively, it translates these insights into fully functional QuantConnect Python algorithms, ensuring they adhere to best practices and syntactic correctness.

```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

def generate_summary_and_code(trading_signals, risk_management):
    prompt = f"""
    Based on the following trading signals and risk management techniques, generate a QuantConnect algorithm:

    Trading Signals:
    {trading_signals}

    Risk Management:
    {risk_management}

    Generate Python code for a QuantConnect algorithm:
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

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
# LLM will generate code after this line
```

### 6. Displaying Results Using Tkinter and Pygments

To provide a user-friendly experience, the tool uses Tkinter to display the article summary and generated code in separate windows. The Pygments library enhances readability by adding syntax highlighting to the Python code.

```python
import tkinter as tk
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def display_results(summary, code):
    root = tk.Tk()
    summary_window = tk.Toplevel(root)
    summary_window.title("Article Summary")
    summary_text = tk.Text(summary_window)
    summary_text.insert(tk.END, summary)
    summary_text.pack()

    code_window = tk.Toplevel(root)
    code_window.title("Generated QuantConnect Code")
    code_text = tk.Text(code_window)
    highlighted_code = highlight(code, PythonLexer(), HtmlFormatter())
    code_text.insert(tk.END, highlighted_code)
    code_text.pack()

    root.mainloop()
```

### 7. Initial Testing

We used the article "Avoiding Bear Markets Using Market Timing Strategy" by L. Durian and R. Vojtko on Quantpedia. The output results are as follows:

![View of code and summary](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2024/10/12/1728730721023-f1a5f810-c487-4c2e-a6a4-acc2b63df7a8.png)

The code generated on the first run produced the following backtest results:

![Backtest results of generated code - Powered by QuantConnect](https://cdn-images-1.readmedium.com/v2/resize:fit:800/1*X_7QwYDI7EZOvwRS1Y8UIg.png)

We can see that the algorithm was out of the market in 2020, as expected, avoiding the bear market during the COVID-19 pandemic. The article indeed seems to have successfully managed bear market avoidance and is definitely worth further investigation.

## Conclusion

Automating the transformation of quantitative finance research into executable trading algorithms can significantly improve efficiency. By integrating powerful libraries such as pdfplumber, SpaCy, OpenAI's GPT-4, Tkinter, and Pygments, this Python-based tool provides a seamless solution that bridges the gap between research and implementation.

---

**Opinions**

- We believe that the current process of translating financial papers into trading algorithms is time-consuming and error-prone, emphasizing the necessity for automation.
- The preliminary nature of the tool is emphasized, with the author acknowledging that while the generated code is largely error-free, achieving complete accuracy remains a goal for future development.
- The tool's ability to categorize sentences into trading signals and risk management is viewed as a key feature, ensuring that only relevant information is used for code generation.
- The use of GPT-4 for code generation is considered particularly innovative, showcasing the potential of AI in the quantitative finance domain.
- We are optimistic about the project's ongoing improvements and its potential to become a valuable asset for quantitative analysts and traders.
- The use of Tkinter to create a user-friendly interface and Pygments for syntax highlighting indicates a focus on user experience and readability of the generated code.