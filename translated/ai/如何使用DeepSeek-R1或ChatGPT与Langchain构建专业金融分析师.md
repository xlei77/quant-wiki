---
{}
---

Here's the English translation of the provided text, maintaining technical accuracy, markdown formatting, math expressions, and code elements:

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Code Open Source! How to Build a Professional Financial Analyst Using DeepSeek-R1 or ChatGPT with Langchain

In the rapidly changing financial markets, **how to use artificial intelligence to aid investment decisions** is becoming a focus of attention for more and more investors. Using large models for **stock analysis** and **news insights** not only allows us to efficiently obtain key data but also generates more valuable investment advice. This article will guide you step by step to build two practical scenarios:

1. **Part One**: Create a **stock analysis agent** using **DeepSeek-R1**, including obtaining stock prices, calculating technical indicators, evaluating financial indicators, and outputting actionable conclusions.
2. **Part Two**: Focus on **news content analysis** using **ChatGPT**, extracting real-time news and conducting sentiment analysis to provide more comprehensive references for investment decisions.

> If you are a financial professional, quantitative engineer, or data scientist, this article will provide you with almost complete sample code to help you quickly build your own intelligent analysis Agent.

## Part One: Building a Stock Analysis Agent Using DeepSeek-R1

In this part, we will use the **DeepSeek-R1** model to complete the analysis of **stock prices and financial data**. The main steps include:

1. Environment preparation and installation
2. Obtaining historical stock prices and key technical indicators (RSI, MACD, VWAP, etc.)
3. Obtaining financial indicators (such as P/E ratio, P/B ratio, debt-to-equity ratio, profit margin, etc.)
4. Process orchestration using **LangChain** and **LangGraph**, and using **DeepSeek-R1** for analysis generation

### 1. Environment Installation

First, install the required libraries (note that DeepSeek-R1 depends on [Ollama](https://ollama.ai/) or the corresponding local deployment environment):

```bash
pip install yfinance pandas ta langchain langchain-openai langchain-community langchain-experimental langchain_core langgraph python-dotenv
```

And create a `.env` file in your project directory to store your custom environment variables (if any):

```
OPENAI_API_KEY=your_openai_api_key
```

If you don't need private APIs, you can ignore this.

### 2. Obtaining Stock and Technical Indicators

Before starting, make sure you have installed `yfinance` to get stock data and `ta` to calculate common technical indicators. The following example tool function will obtain the price data of the specified stock for the **last 24 weeks** and calculate common technical indicators such as **RSI**, **MACD**, **Stochastic Oscillator**, and **VWAP**.

```python
import yfinance as yf
import pandas as pd
import ta

def get_stock_data_and_indicators(symbol, period="24wk"):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    
    # Calculate RSI
    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    
    # Calculate MACD
    macd = ta.trend.MACD(df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    df['MACD_Histogram'] = macd.macd_diff()
    
    # Calculate Stochastic Oscillator
    stoch = ta.momentum.StochasticOscillator(df['High'], df['Low'], df['Close'])
    df['Stoch_K'] = stoch.stoch()
    df['Stoch_D'] = stoch.stoch_signal()
    
    # Calculate VWAP
    df['VWAP'] = ta.volume.VolumeWeightedAveragePrice(df['High'], df['Low'], df['Close'], df['Volume']).volume_weighted_average_price()
    
    return df
```

### 3. Obtaining Financial Indicators

Financial health indicators include **P/E, Price-to-Book, Debt-to-Equity, Profit Margins**, etc.:

```python
def get_financial_indicators(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    
    pe_ratio = info.get('trailingPE', 'N/A')
    pb_ratio = info.get('priceToBook', 'N/A')
    debt_to_equity = info.get('debtToEquity', 'N/A')
    profit_margins = info.get('profitMargins', 'N/A')
    
    return {
        'P/E Ratio': pe_ratio,
        'Price-to-Book Ratio': pb_ratio,
        'Debt-to-Equity Ratio': debt_to_equity,
        'Profit Margins': profit_margins
    }
```

### 4. Comprehensive Analysis Using LangGraph + DeepSeek-R1

#### 4.1 Environment Configuration

We use **LangGraph** to chain the conversation flow and tool calls. The large model we'll use is **DeepSeek-R1**, which needs to be used in conjunction with [OllamaLLM](https://pypi.org/project/langchain-ollama/) to call the local or server-side large model.

```python
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langgraph.graph import StateGraph, END
```

#### 4.2 Binding the DeepSeek-R1 Model

```python
llm = Ollama(model="deepseek-coder:6.7b")
```

#### 4.3 Building Prompt and Binding Tools

We want the agent to:
1. Obtain stock history and technical indicators
2. Obtain financial indicators
3. Comprehensively analyze and output readable conclusions

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional stock analyst. Analyze the given stock data and provide investment advice."),
    ("human", "Please analyze the stock {symbol}. Here's the data:\n\nTechnical Indicators:\n{technical_data}\n\nFinancial Indicators:\n{financial_data}"),
    ("human", "Based on this data, what's your analysis and investment recommendation?")
])

chain = prompt | llm | StrOutputParser()
```

#### 4.4 Integrating Tool Nodes and Analysis Nodes into the Workflow

```python
def analyze(state):
    symbol = state['symbol']
    technical_data = get_stock_data_and_indicators(symbol)
    financial_data = get_financial_indicators(symbol)
    
    result = chain.invoke({
        "symbol": symbol,
        "technical_data": technical_data.to_string(),
        "financial_data": str(financial_data)
    })
    
    return {"result": result}

workflow = StateGraph(initial_state={"symbol": None})

workflow.add_node("analyze", analyze)
workflow.set_entry_point("analyze")
workflow.add_edge('analyze', END)

app = workflow.compile()
```

#### 4.5 Execution Example

```python
inputs = {"symbol": "AAPL"}
result = app.invoke(inputs)
print(result['result'])
```

The output might look like:

```
Based on the provided technical and financial data for Apple Inc. (AAPL), here's my analysis and investment recommendation:

1. Technical Analysis:
   - The stock is currently trading at $173.50, which is above its 50-day moving average of $170.86 and its 200-day moving average of $165.94, indicating a bullish trend.
   - The RSI (Relative Strength Index) is at 59.37, suggesting that the stock is neither overbought nor oversold.
   - The MACD line is above the signal line, which is a bullish signal.
   - The Stochastic Oscillator shows a reading of 80.23 for %K and 74.54 for %D, indicating that the stock might be approaching overbought territory.

2. Financial Indicators:
   - P/E Ratio: 28.61, which is relatively high compared to the overall market but not uncommon for a tech giant like Apple.
   - Price-to-Book Ratio: 44.75, indicating that the stock is trading at a premium to its book value.
   - Debt-to-Equity Ratio: 261.45, which is high and suggests the company is using significant leverage.
   - Profit Margins: 25.31%, showing strong profitability.

Investment Recommendation:
Given the current data, I would recommend a HOLD position on Apple stock with a cautiously bullish outlook. Here's why:

Positives:
- The stock is in an uptrend, trading above key moving averages.
- Strong profit margins indicate efficient operations and pricing power.
- The MACD suggests positive momentum.

Cautions:
- The high P/E and P/B ratios suggest the stock might be somewhat overvalued.
- The high debt-to-equity ratio is a concern and should be monitored.
- The stock is approaching overbought levels according to the Stochastic Oscillator.

For long-term investors, Apple remains a solid company with strong financials and market position. However, given the current valuation and technical indicators, it might be wise to wait for a pullback before adding to positions.

For short-term traders, the current momentum could provide opportunities, but be cautious of potential overbought conditions and keep tight stop-losses.

As always, this recommendation should be considered in the context of your overall investment strategy and risk tolerance. Keep an eye on upcoming earnings reports and any significant news that could impact the stock's performance.
```

---

## Part Two: Building a News Analysis Agent Using ChatGPT

After completing the stock and financial data analysis, we also need to pay attention to **market sentiment** and **real-time news dynamics**. This section will introduce how to use **ChatGPT** (or OpenAI GPT-4) to analyze relevant news, provide sentiment judgments, and investment advice.

### 1. Main Features

- **Scrape news related to the stock** (using Yahoo Finance)
- **Extract full text from web pages** (using tools like MarkItDown)
- **Conduct sentiment analysis on news** (Positive, Negative, Neutral)
- **Provide investment advice based on comprehensive news views**

### 2. Installation and Environment Preparation

If you have already installed `yfinance`, `pandas`, etc., you can skip this step and only need to confirm that the **OpenAI** dependency is installed:

```bash
pip install openai
```

And add to the `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

### 3. Obtaining Relevant News Links

```python
import yfinance as yf

def get_news_links(symbol, limit=5):
    stock = yf.Ticker(symbol)
    news = stock.news
    return [item['link'] for item in news[:limit]]
```

### 4. Extracting and Cleaning News Content

```python
import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Get text
    text = soup.get_text()
    
    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text
```

### 5. Getting Complete News Content

```python
def get_full_news_content(symbol, limit=5):
    links = get_news_links(symbol, limit)
    news_contents = []
    for link in links:
        content = extract_article_text(link)
        news_contents.append({"url": link, "content": content})
    return news_contents
```

### 6. Using ChatGPT for Sentiment Analysis and Investment Advice

Now we have the **complete news**. Let's use **LangChain** + **OpenAI** for sentiment analysis.

```python
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a financial news analyst. Analyze the given news articles and provide sentiment analysis and investment advice."),
    ("human", "Here are some recent news articles about {symbol}:\n\n{news_content}\n\nPlease analyze these articles and provide:\n1. Sentiment analysis for each article (Positive, Negative, or Neutral)\n2. Key points from each article\n3. Overall summary of the news\n4. Investment advice based on this news"),
])

chain = prompt | llm | StrOutputParser()
```

Example usage:

```python
symbol = "AAPL"
news = get_full_news_content(symbol)
news_content = "\n\n".join([f"Article {i+1}:\n{item['content'][:500]}..." for i, item in enumerate(news)])

result = chain.invoke({"symbol": symbol, "news_content": news_content})
print(result)
```

ChatGPT will output a JSON structure containing sentiment judgments for each news item, main points, overall summary, and investment advice. You can then parse this result and integrate it into the workflow built earlier to achieve a three-in-one agent analysis of **news sentiment + technical analysis + fundamental analysis**.

---

## Summary and Future Extensions

In this tutorial, we demonstrated in two main parts how to:

1. **Use DeepSeek-R1** to create a stock analysis agent:
   - Obtain stock prices and technical indicators
   - Obtain financial data
   - Use LangGraph to orchestrate the process and generate readable analysis reports

2. **Use ChatGPT** for news content analysis agent:
   - Obtain news links related to the stock
   - Extract and clean webpage content
   - Output sentiment analysis and investment advice

### What can you do further?

- **Multi-Agent Integration**: Combine the "stock analysis agent" and "news analysis agent" into one LangGraph workflow, outputting comprehensive analysis including **stock prices, financials, and news**.
- **Enhance Factor Model**: Add more factors such as industry comparisons and macroeconomic data based on market characteristics.
- **Visualization and Automation**: Deploy analysis results in a web interface or automated task flow, generating analysis reports periodically.
- **Use Other Open-Source Large Models**: Such as BLOOM, LLaMA, ChatGLM, etc., to compare analysis effects and performance differences.

> **Whether it's DeepSeek-R1 or ChatGPT, they can be flexibly replaced or complemented according to actual needs**. We hope this tutorial can help you quickly get started and build your own "agent-type financial analyst" to gain more insights and opportunities in the competitive market.

If you have questions about the related code or want to share more ideas, feel free to discuss in the comments section. **Let's explore more possibilities of large models in the financial market together!**

Here's the English translation, maintaining the technical accuracy and formatting:

## About LLMQuant

LLMQuant is a cutting-edge community composed of individuals from the world's top universities and quantitative finance professionals, dedicated to exploring the infinite possibilities in the fields of Artificial Intelligence (AI) and Quantitative Finance (Quant). Our team members come from renowned global institutions such as the University of Cambridge, University of Oxford, Harvard University, ETH Zurich, Peking University, University of Science and Technology of China, and other world-class universities. Our external advisors are from leading companies including Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top-tier private equity firms in China.