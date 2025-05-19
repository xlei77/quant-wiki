---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# Can ChatGPT Do Investment Analysis? A Step-by-Step Guide to Building a Stock Research Framework with LangChain
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Investment analysts are increasingly applying artificial intelligence to process financial data, identify trends, and gain deep insights. Among these tools, **LangChain**, as a highly promising open-source framework, can combine language models like GPT with investment analysis. This article will explore how to use LangChain to streamline preliminary investment research processes, including **integrating financial data sources**, **building advanced custom models**, and making smarter **investment decisions** based on predictive insights.

In this article, we will focus on:

> 1. Why choose LangChain?  
> 2. What is LangChain?  
> 3. Core components of LangChain  
> 4. How to use LangChain with OpenAI in Python for stock analysis  

## Why Choose LangChain?
Let's first try to have ChatGPT analyze the price performance of the NIFTY50 index over the past 5 years:

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/02/15/1739656021954-842a89c6-5f12-4a7a-827b-082257fc13e7.png)

> **"When we ask ChatGPT about NIFTY50's performance over the past 5 years, it doesn't have readily available data for analysis."**

This is where **LangChain** truly shines. LangChain can combine financial data sources with Large Language Models (LLMs), transforming how investors analyze and interpret market data. By analyzing vast amounts of textual data (such as news reports, financial statements, and social media sentiment), LangChain can provide analysts with richer, more timely insights to support better investment decisions.

## What is LangChain?
LangChain serves as an interface between large language models and external data sources, helping users build **AI-driven applications**. LangChain enables developers to connect to various databases, retrieve required information, process inputs, and output structured results.

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2025/02/15/1739656034346-533c4045-ea5a-4aac-9c0c-fc97eb728621.png)

> "LLM (Large Language Model) is a deep learning model trained on massive amounts of data that can generate responses based on user queries. LangChain provides tools and abstraction layers to enhance the customization, accuracy, and relevance of model outputs."
> "LangChain supports multiple mainstream LLM models, the specific list can be found at: [https://python.langchain.com/docs/integrations/llms/](https://python.langchain.com/docs/integrations/llms/)."

## Core Components of LangChain
In the following examples, we will demonstrate how to implement the main components of LangChain in Python.

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/02/15/1739656041606-31207779-b15e-4465-b329-c084e05150c4.png)

> **Note: Some code examples below use the langchain_openai version as shown in the text.**

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2025/02/15/1739656100104-857e381f-88f8-4102-99e7-98381a1ba038.png)

### 1. Using LLMs
LangChain can integrate multiple large language models through the **Prompting** mechanism to generate more complex and targeted responses based on specific tasks or queries.
![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/02/15/1739656110396-a8674285-0267-4917-946d-cba8c90867b2.png)
- **Temperature**: Represents the randomness of the model's output. If set to 0, you will get deterministic output, meaning the same result will be produced across multiple runs.

**Example Output:**

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656120414-4048f53d-2c01-4f8f-80d2-a72e7b3aeae4.png)


> **"Since the output contains multiple elements, we are more interested in the content part, so we can extract the content using the corresponding method."**

### 2. Prompt Templates
Prompt templates are **predefined structures or formats** used when generating prompts for language models like GPT-4. They help us quickly construct consistent, contextually relevant queries or instructions across different scenarios. Prompt templates can also include dynamic placeholders for passing specific data or parameters.


![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656145141-983ccd3b-1bd6-4836-a849-34bbffa730a0.png)

### 3. Chains
In LangChain, a "chain" refers to a series of ordered steps or operations that link together prompts, data processing steps, API calls, and other components to accomplish more complex natural language processing tasks.  
> **"chain = prompt | llm"**  
This indicates feeding the prompt into the language model (LLM) to generate corresponding responses.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656160804-ab734299-fdf2-48d9-bc4f-525efdcd48be.png)

- Batch Processing: Refers to inputting multiple data entries into the chain simultaneously for parallel processing, thereby improving efficiency.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656167462-5c38f475-0dee-4285-98ef-ce7d1d3523b6.png)

### 4. Agents
**Agent** is an automated entity that uses large language models to accomplish specific tasks. It can make decisions, execute actions, and dynamically interact with various data sources or APIs according to design requirements.  
In the example below, **PythonREPLTool()** is used as an Agent's tool to directly run Python code within the LangChain process for data processing, analysis, or computation.

> **Note:** The LangChain version used in the following example is "langchain-core<0.2".

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/02/15/1739656174967-f3151ffb-1663-4ad9-a0d7-2a411b5bc85e.png)


![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/02/15/1739656182025-0bdc16cc-55a1-49c3-9899-1af7be302c07.png)

## Stock Analysis Using LangChain and OpenAI (Python Case Study)
Next, we will build a simple application based on LLM (Large Language Model) to determine whether a stock is worth investing in. This application primarily uses the following data sources:

- **Google News**  
- **Historical stock price data**  
- **ChatGPT Agent** to integrate these data sources, make comprehensive judgments, and generate responses

In this example, we will use **agents** to generate responses. You can also use **function calling** to make the output more structured.

### 1. Preparation
- Need an **OpenAI API Key** (can be obtained by registering and purchasing from the OpenAI official website).
- Need a **SERP API Key** (obtain from [SERPAPI](https://serpapi.com/)) to fetch the latest news about specific stocks.

### 2. Import Libraries
Before starting, ensure you have the appropriate version of **Pydantic** library installed.

![](https://fastly.jsdelivr.net/gh/bucketio/img2@main/2025/02/15/1739656196722-23e2cba2-08cb-45dc-a34b-a1cb530fe7a8.png)




```python
# 安装 pydantic
!pip install pydantic==<相应版本>
```

Then import other required libraries and modules:
![](https://fastly.jsdelivr.net/gh/bucketio/img16@main/2025/02/15/1739656204753-b22580da-f346-4eb5-a138-88ef7f260212.png)

```python
import os
import requests
import datetime
import yfinance as yf
from typing import Dict
from langchain_core.tools import Tool
from langchain.agents import initialize_agent
from langchain_core.prompts import PromptTemplate
# ... 其它必要的导入
```

LangChain provides `langChain_core.tools` to define and manage tools that can be used by Agents. These tools can perform specific tasks such as calculations, database queries, web searches, or API calls.  
`langchain.agents` provides the framework for building and running Agents, enabling them to reason, make decisions, and invoke tools to complete tasks.  
`langchain_core.prompts` is used for designing and managing Prompts to guide how language models should respond.

### 3. Get Latest News
Below we define a function `get_news` that retrieves the latest news for the target stock using **SERP API**. Replace "YOUR_SERPAPI_API_KEY" with your actual API Key:
![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2025/02/15/1739656224205-d0288dfd-e4f6-4726-a82e-e6ac63d3700a.png)

```python
def get_news(ticker: str) -> str:
    # 通过SERP API获取新闻的示例代码
    ...
```

### 4. Retrieving Historical Stock Price Data
Obtain historical stock price information for the past year through **Yahoo Finance**:

```python
def get_historical_data(ticker: str) -> str:
    # 使用 yfinance 库获取股票的历史价格数据
    ...
```

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/02/15/1739656233507-63ea62a3-7096-4d48-bc62-115d2045df62.png)

### 5. Custom Analysis Functions
Define a function ``analyze_stock`` to determine whether an investment is worthwhile. This function provides analytical recommendations based on certain rules (such as data performance, news content, etc.):

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/02/15/1739656242065-6179ba65-adf0-44b0-a9cd-54109ca463c8.png)

```python
def analyze_stock(news: str, historical_data: str) -> str:
    # 根据自定义逻辑进行分析
    ...
```

### 6. Define Tools
Define the above three functions as three **Tools**: `get_news`, `get_historical_data`, and `analyze_stock`, making them convenient to call in subsequent Agents:

```python
tools = [
    Tool(
        name="get_news",
        func=get_news,
        description="获取目标股票的最新新闻"
    ),
    Tool(
        name="get_historical_data",
        func=get_historical_data,
        description="获取目标股票的历史价格信息"
    ),
    Tool(
        name="analyze_stock",
        func=analyze_stock,
        description="分析股票是否值得投资"
    )
]
```

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/02/15/1739656261255-d1e1ff87-d07a-400a-8ca3-43e07d158c53.png)

### 7. Define Prompt

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656271042-0aed56ef-505b-4812-a51b-6254c39eea96.png)

```python
prompt_template = PromptTemplate(
    input_variables=["ticker"],
    template="""
        我想要分析股票 {ticker} 的投资价值。 
        你可以使用以下工具：
        1. get_news：获取新闻
        2. get_historical_data：获取历史价格
        3. analyze_stock：综合分析
        请给出最终的结论。
    """
)
```

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/02/15/1739656278953-0c1fbbee-33e9-4576-915b-a92eff5e3d43.png)

### 8. Create Agent and Generate Results
Finally, we create an Agent to generate analysis results for the specified stock:

![](https://fastly.jsdelivr.net/gh/bucketio/img8@main/2025/02/15/1739656284236-f89caa6d-eb5d-4f3c-a709-384b3d2d0960.png)


```python
agent = initialize_agent(
    tools=tools,
    llm=OpenAI(temperature=0),
    prompt=prompt_template,
    # 其它所需参数
)

response = agent.run({"ticker": "AAPL"})
print(response)
```

#### Example Response 1:
> **"Based on historical data and latest news, Apple stock could be considered, but should still be evaluated against personal risk tolerance."**

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656292133-5bc8de64-3134-448b-9a17-5a6768ee9967.png)

#### Example Response 2:
> **"Recent news shows positive performance, historical trend shows steady growth, can be used as a reference for long-term investment."**


![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/02/15/1739656297603-2af17aa7-b9db-40c6-97b2-00ed934f9cd1.png)

The above example demonstrates a preliminary stock analysis process based on **LangChain**. It combines historical data with news information to generate simple analytical conclusions. It should be noted that these responses are based only on the data and context provided in the example, and **should not be considered as professional investment advice or final conclusions**. In real investment scenarios, more comprehensive data and research are still needed.

---

By integrating financial data sources (historical data and news) into **LLM**, LangChain can provide faster and deeper market insights to support investment decisions. In the future, as model capabilities and the number of data sources continue to improve, the efficiency and accuracy of investment analysis are expected to further increase.