---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# Code Open Source! How to Build a Professional Financial Analyst Using DeepSeek-R1 or ChatGPT with Langchain




In the rapidly changing financial markets, **how to leverage artificial intelligence for investment decisions** is becoming a focus of attention for more and more investors. Using large language models for **stock analysis** and **news insights** not only enables us to efficiently obtain key data but also generates more valuable investment recommendations. This article will guide you through building two practical scenarios step by step:

1. **Part One**: Creating a **stock analysis agent** using **DeepSeek-R1**, including retrieving stock prices, calculating technical indicators, evaluating financial metrics, and outputting actionable conclusions.  
2. **Part Two**: Focusing on **news content analysis** using **ChatGPT**, extracting real-time news and conducting sentiment analysis to provide more comprehensive reference for investment decisions.



> If you are a finance professional, quantitative engineer, or data scientist, this article will provide you with nearly complete example code to help you quickly build your own intelligent analysis Agent.

## Part 1: Building Stock Analysis Agent Using DeepSeek-R1

In this section, we will complete the analysis of **stock prices and financial data** using the **DeepSeek-R1** model. This includes the following steps:

1. Environment preparation and installation
2. Obtaining historical stock prices and key technical indicators (RSI, MACD, VWAP, etc.)
3. Obtaining financial metrics (such as P/E ratio, P/B ratio, debt-to-equity ratio, profit margins, etc.)
4. Process orchestration through **LangChain** and **LangGraph**, using **DeepSeek-R1** for analysis generation

### 1. Environment Setup

Please first install the required libraries (note that DeepSeek-R1 depends on [Ollama](https://ollama.ai/) or corresponding local deployment environment):

```bash
pip install -U langgraph langchain langchain-ollama pandas ta python-dotenv yfinance
```

And create a `.env` file in your project directory to store your custom environment variables (if any):

```
# 可选
DEEPSEEK_API_KEY=your_deepseek_api_key
```

If you don't need private APIs, you can ignore this.

### 2. Obtaining Stock Data and Technical Indicators

Before starting, ensure you have installed `yfinance` for retrieving stock data and `ta` for calculating common technical indicators. The following example utility function will obtain price data for the specified stock from the **last 24 weeks** and calculate common technical indicators including **RSI**, **MACD**, **Stochastic Oscillator**, and **VWAP**.

```python
from typing import Union, Dict, TypedDict
import pandas as pd
import yfinance as yf
import datetime as dt

# TA 库
from ta.momentum import RSIIndicator, StochasticOscillator
from ta.trend import MACD
from ta.volume import volume_weighted_average_price

def get_stock_prices(ticker: str) -> Union[Dict, str]:
    """获取指定股票的历史价格数据和关键技术指标。"""
    try:
        data = yf.download(
            ticker,
            start=dt.datetime.now() - dt.timedelta(weeks=24*3),
            end=dt.datetime.now(),
            interval='1wk'
        )
        df = data.copy()
        data.reset_index(inplace=True)
        data.Date = data.Date.astype(str)
        
        indicators = {}
        
        rsi_series = RSIIndicator(df['Close'], window=14).rsi().iloc[-12:]
        indicators["RSI"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in rsi_series.dropna().to_dict().items()
        }
        
        sto_series = StochasticOscillator(
            df['High'], df['Low'], df['Close'], window=14
        ).stoch().iloc[-12:]
        indicators["Stochastic_Oscillator"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in sto_series.dropna().to_dict().items()
        }
        
        macd = MACD(df['Close'])
        macd_series = macd.macd().iloc[-12:]
        indicators["MACD"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in macd_series.to_dict().items()
        }
        
        macd_signal_series = macd.macd_signal().iloc[-12:]
        indicators["MACD_Signal"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in macd_signal_series.to_dict().items()
        }
        
        vwap_series = volume_weighted_average_price(
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            volume=df['Volume'],
        ).iloc[-12:]
        indicators["vwap"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in vwap_series.to_dict().items()
        }
        
        return {
            'stock_price': data.to_dict(orient='records'),
            'indicators': indicators
        }

    except Exception as e:
        return f"Error fetching price data: {str(e)}"
```

### 3. Obtaining Financial Indicators

Financial health indicators include **P/E, Price-to-Book, Debt-to-Equity, Profit Margins** and others:

```python
def get_financial_metrics(ticker: str) -> Union[Dict, str]:
    """获取指定股票的关键财务比率。"""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            'pe_ratio': info.get('forwardPE'),
            'price_to_book': info.get('priceToBook'),
            'debt_to_equity': info.get('debtToEquity'),
            'profit_margins': info.get('profitMargins')
        }
    except Exception as e:
        return f"Error fetching ratios: {str(e)}"
```

### 4. Comprehensive Analysis Using LangGraph + DeepSeek-R1

#### 4.1 Environment Configuration

We use **LangGraph** to connect conversation flows and tool calls. For this implementation, we will use **DeepSeek-R1** as our large language model, which needs to be used in conjunction with [OllamaLLM](https://pypi.org/project/langchain-ollama/) to call the large model either locally or on the server side.

```python
import dotenv
dotenv.load_dotenv()

from langgraph.graph import StateGraph, START, END
from langchain_core.nodes import ToolNode
from typing import TypedDict

class State(TypedDict):
    messages: list
    stock: str

graph_builder = StateGraph(State)
```

#### 4.2 Binding the DeepSeek-R1 Model

#### 4.3 Building Prompts and Binding Tools

We want the agent to be able to:
1. Obtain stock history and technical indicators
2. Obtain financial indicators
3. Perform comprehensive analysis and output readable conclusions

```python
from langchain.schema import SystemMessage
from langchain_core.tools import tool

FUNDAMENTAL_ANALYST_PROMPT = """
You are a fundamental analyst specializing in evaluating company performance based on stock prices, technical indicators, and financial metrics.
Your task: Provide a comprehensive summary for {company}.

Steps to follow:
1. Use get_stock_prices and get_financial_metrics to gather data.
2. Analyze trends, potential support/resistance, and financial health.
3. Provide a concise, objective summary in JSON with:
   - "stock": <symbol>
   - "price_analysis": ...
   - "technical_analysis": ...
   - "financial_analysis": ...
   - "final_summary": ...
   - "recommendation": ...
"""

def fundamental_analyst(state: State):
    system_message = SystemMessage(
        content=FUNDAMENTAL_ANALYST_PROMPT.format(company=state['stock'])
    )
    messages = [system_message] + state["messages"]
    # 直接调用 llm.invoke
    result = llm.invoke(messages)
    return {"messages": result}
```

#### 4.4 Connecting Tool Nodes and Analysis Nodes to the Workflow

#### 4.5 Implementation Example

```python
events = graph.stream({
    "messages": [("user", "Should I buy this stock?")],
    "stock": "AAPL"
}, stream_mode='values')

for event in events:
    if 'messages' in event:
        print(event['messages'][-1].content)
```

The output may look like:

```json
{
  "stock": "AAPL",
  "price_analysis": "Recent price shows an upward trend with moderate volatility...",
  "technical_analysis": "RSI is around 62 indicating slightly overbought range...",
  "financial_analysis": "PE ratio is 28.5, which is higher than industry median...",
  "final_summary": "Apple maintains strong fundamentals but currently trades at a premium...",
  "recommendation": "Consider a partial buy if you anticipate continued revenue growth."
}
```

---

## Part Two: Building News Analysis Agents Using ChatGPT

After completing stock and financial data analysis, we also need to pay attention to **market sentiment** and **real-time news developments**. This section will introduce how to use **ChatGPT** (or OpenAI GPT-4) to analyze relevant news, provide sentiment judgments, and investment recommendations.

### 1. Main Functions

- **Fetch stock-related news** (using Yahoo Finance)
- **Extract full webpage content** (using tools like MarkItDown)
- **Perform sentiment analysis on news** (Positive, Negative, Neutral)
- **Provide investment recommendations based on aggregated news sentiment**

### 2. Installation and Environment Setup

If you have already installed `langgraph`, `langchain`, etc., you can skip this step and only need to confirm that the **OpenAI** dependency is installed:

```
# 可选
DEEPSEEK_API_KEY=your_deepseek_api_key
```0

And add the following to the `.env` file:

```
# 可选
DEEPSEEK_API_KEY=your_deepseek_api_key
```1

### 3. Obtain Related News Links

```
# 可选
DEEPSEEK_API_KEY=your_deepseek_api_key
```2

### 4. Extract and Clean News Content

### 5. Retrieve Complete News Content

```
# 可选
DEEPSEEK_API_KEY=your_deepseek_api_key
```4

### 6. Using ChatGPT for Sentiment Analysis and Investment Recommendations

Now that we have the **complete news**, let's use **LangChain** + **OpenAI** for sentiment analysis.

```
# 可选
DEEPSEEK_API_KEY=your_deepseek_api_key
```5

Example usage:

```
# 可选
DEEPSEEK_API_KEY=your_deepseek_api_key
```6

ChatGPT will output a JSON structure containing sentiment analysis for each news item, key highlights, overall summary, and investment recommendations. You can parse this result and integrate it into the previously built workflow to achieve a trinity of analysis combining **sentiment factors + technical analysis + fundamental analysis**.

---

## Summary and Future Extensions

In this tutorial, we demonstrated in two main parts how to:

1. **Use DeepSeek-R1** to create a stock analysis agent:
   - Retrieve stock prices and technical indicators
   - Obtain financial data
   - Use LangGraph to orchestrate workflows and generate readable analysis reports

2. **Use ChatGPT** for news content analysis agent:
   - Obtain news links related to stocks
   - Extract and clean webpage content
   - Output sentiment analysis and investment recommendations

### What else can you do?

- **Multi-Agent Integration**: Merge the "Stock Analysis Agent" with the "News Analysis Agent" into a single LangGraph workflow, outputting comprehensive analysis that includes **stock prices, financials, and news**.
- **Enhanced Factor Model**: Add more factors based on market characteristics, such as industry comparisons and macroeconomic data.
- **Visualization and Automation**: Deploy analysis results in a web interface or automated workflow to generate periodic analysis reports.
- **Alternative Open-Source Models**: Try other models like BLOOM, LLaMA, ChatGLM, etc., to compare analysis effectiveness and performance differences.

> **Whether it's DeepSeek-R1 or ChatGPT, they can be flexibly substituted or complemented based on actual needs**. We hope this tutorial helps you quickly get started and build your own "agent-based financial analyst" to gain more insights and opportunities in the competitive market.

If you have questions about the code or want to share more ideas, feel free to discuss in the comments section. **Let's explore more possibilities of large language models in financial markets together!**

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。