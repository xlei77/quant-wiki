---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# Deep Analysis: How to Perform Sentiment Analysis on Tesla-Related News and Generate Investment Advice Using DeepSeek-R1

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

In stock investment, **news sentiment** often has a significant impact on stock prices. Real-time monitoring and analysis of news information helps us assess market sentiment and optimize investment decisions. Using Tesla (**TSLA**) as an example, this article demonstrates a complete practical workflow from "news acquisition → content extraction → sentiment analysis → investment advice" by combining **Yahoo Finance**, **MarkItDown**, and the **DeepSeek-R1** model.

> **Target Audience**: Quantitative engineers, data scientists, fund managers interested in automated financial news analysis, or learners who want to quickly get started with news sentiment analysis.

## Feature Overview

1. **Fetch Tesla-related News**: Use `yfinance` to obtain the latest TSLA news.  
2. **Extract and Clean Content**: Parse webpage content using the MarkItDown library, and perform simple regex cleaning on the text.  
3. **Sentiment Analysis and Recommendations**: Score multiple news articles and output investment advice based on the DeepSeek-R1 model.

Through these steps, you can quickly build a "mini sentiment radar" that analyzes multiple consolidated news articles.

## 1. Environment Setup

1. Install Python dependencies:
   ```bash
   pip install yfinance pandas markitdown requests langchain langchain-ollama
   ```
2. Ensure that the **DeepSeek-R1** model has been successfully deployed locally or on a server, and can be called through [Ollama](https://ollama.ai/) or similar methods.

> If you don't have the DeepSeek-R1 model yet, you can try installing the corresponding environment locally or replace it with other compatible models.

---

## 2. Obtaining Tesla (TSLA) Related News

### 2.1 Writing the `get_news` Function

The following function fetches Tesla-related news through the `Ticker` object from the `yfinance` library and extracts key fields (title, summary, link, publication date):

```python
import yfinance as yf
import pandas as pd

def get_news(stock: str) -> list:
    """
    获取与指定股票相关的新闻列表，返回包含标题、摘要、链接、发布日期的字典列表。
    """
    try:
        # 获取股票对象及其新闻
        ticker = yf.Ticker(stock)
        news = ticker.news

        # 如果没有新闻，则返回空列表
        if not news:
            print(f"No news found for {stock}.")
            return []

        # 只保留contentType='STORY'的新闻
        relevant_news = [
            item for item in news if item.get('content', {}).get('contentType') == 'STORY'
        ]

        all_news = []
        for i, item in enumerate(relevant_news):
            try:
                content = item.get('content', {})
                current_news = {
                    'title': content.get('title'),
                    'summary': content.get('summary'),
                    'url': content.get('canonicalUrl', {}).get('url'),
                    'pubdate': content.get('pubDate', '').split('T')[0],
                }
                all_news.append(current_news)
            except Exception as e:
                print(f"Error processing news {i}: {e}")
                continue

        return all_news

    except Exception as e:
        print(f"An error occurred while fetching news for {stock}: {e}")
        return []
```

#### Example Call

```python
news_list = get_news("TSLA")
print(len(news_list))  # 查看获取到的新闻数量
print(news_list[0])    # 输出其中一篇新闻的信息
```

The structure obtained is:

```python
{
    'title': 'Tesla Poised to Beat Q1 Earnings Estimates...',
    'summary': '...',
    'url': 'https://finance.yahoo.com/news/...',
    'pubdate': '2025-01-20'
}
```

## 3. Extract and Clean News Content

### 3.1 Using MarkItDown to Parse Webpages

`MarkItDown` helps us convert webpage HTML into plain text, including both headers and body content. While extracting the text, we remove certain **links** and **special characters** to make subsequent analysis cleaner.

```python
from markitdown import MarkItDown
import requests
import re

# 创建Session以提高稳定性
session = requests.Session()
session.headers.update({
    'User-Agent': 'python-requests/2.32.3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
})
md = MarkItDown(requests_session=session)

def remove_links(text: str) -> str:
    """
    去除URL、Markdown格式链接及多余字符
    """
    text = re.sub(r'http\S+', '', text)       # 移除URL
    text = re.sub(r'\[.*?\]', '', text)       # 移除Markdown链接
    text = re.sub(r'[#*()+\-\n]', '', text)   # 移除特殊字符
    text = re.sub(r'/\S*', '', text)          # 移除带斜线的内容
    text = re.sub(r'  ', '', text)            # 移除多余空格
    return text

def extract_news(link: str) -> str:
    """
    基于MarkItDown抽取页面标题与正文，并进行清洗后返回。
    """
    info = md.convert(link)
    text_title = info.title.strip()
    text_content = info.text_content.strip()
    return text_title + '\n' + remove_links(text_content)
```

### 3.2 Retrieving and Integrating All News Text

With `get_news` and `extract_news`, we can extract all news articles at once. Here's an example:

```python
def extract_full_news(stock: str) -> list:
    """
    以full_news字段的形式，把网页正文添加到每篇新闻中返回。
    """
    news_data = get_news(stock)
    for i, item in enumerate(news_data):
        try:
            content = extract_news(item['url'])
            item['full_news'] = content
        except Exception as e:
            print(f"Error extracting news {i}: {e}")
            continue
    return news_data

# 以TSLA为例
full_news_list = extract_full_news("TSLA")

print(full_news_list[0]['title'])       # 新闻标题
print(full_news_list[0]['full_news'])   # 提取后的完整正文
```

The resulting `full_news_list` contains the integrated results of all fields (title, summary, URL, body text, etc.).

![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2025/02/26/1740600002331-9d6ca907-4b79-48d9-bb67-94245f893670.png)

## IV. Using DeepSeek-R1 for Sentiment Analysis and Investment Recommendations

### 4.1 DeepSeek-R1 and LangChain Integration

This example uses [OllamaLLM](https://pypi.org/project/langchain-ollama/) as the interface to call DeepSeek-R1. Multiple news articles are combined and sent to the LLM for sentiment analysis.

```python
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from pprint import pprint

# 初始化DeepSeek-R1
llm = OllamaLLM(model="deepseek-r1:1.5b")
```

### 4.2 Writing the Prompt Template

We want the model to provide "Positive/Negative/Neutral" sentiment evaluations for each item, and then provide investment advice based on a summary of all articles. These requirements can be written as `system` prompts and passed to the LLM:

```python
PROMPT = """
You are an expert financial analyst. I will provide you with a list of news articles related to Tesla (TSLA). Your tasks:

1. **Sentiment Analysis:**
   - For each news article, evaluate its sentiment as 'Positive', 'Negative', or 'Neutral'.
   - Present your evaluation in a dictionary format like: {"Article Title": "Positive", ...}

2. **Comprehensive Summary & Recommendation:**
   - Summarize the overall sentiment and key points from all articles.
   - Advise if investing in TSLA is advisable, with reasons derived from the news analysis.

**News Articles:**

{articles}

**Output Format:**

1. Sentiment Analysis Dictionary (JSON)
2. Summary
3. Investment Recommendation
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', PROMPT),
        ('human', "I want to analyze TSLA's news articles in detail.")
    ]
)
```

### 4.3 Calling the Model and Outputting Results

Combine our extracted body text (`full_news`) into a list as `get_news`0 to pass into PromptTemplate, then call the LLM:

```python
structure = prompt_template | llm

result = structure.invoke({
    "articles": [item['full_news'] for item in full_news_list]
})

pprint(result)
```

After DeepSeek-R1 completes generation, you will see results similar to the following:

```txt
"<think>\n... [模型内部推理] ...\n</think>\n\n
### Sentiment Analysis Dictionary
```json
{
   "Tesla Q4 Earnings: A Beat on Estimates?": "Positive",
   "Elon Musk's Latest Statement Sparks Controversy": "Neutral",
   ...
}
```python
import yfinance as yf
import pandas as pd

def get_news(stock: str) -> list:
    """
    获取与指定股票相关的新闻列表，返回包含标题、摘要、链接、发布日期的字典列表。
    """
    try:
        # 获取股票对象及其新闻
        ticker = yf.Ticker(stock)
        news = ticker.news

        # 如果没有新闻，则返回空列表
        if not news:
            print(f"No news found for {stock}.")
            return []

        # 只保留contentType='STORY'的新闻
        relevant_news = [
            item for item in news if item.get('content', {}).get('contentType') == 'STORY'
        ]

        all_news = []
        for i, item in enumerate(relevant_news):
            try:
                content = item.get('content', {})
                current_news = {
                    'title': content.get('title'),
                    'summary': content.get('summary'),
                    'url': content.get('canonicalUrl', {}).get('url'),
                    'pubdate': content.get('pubDate', '').split('T')[0],
                }
                all_news.append(current_news)
            except Exception as e:
                print(f"Error processing news {i}: {e}")
                continue

        return all_news

    except Exception as e:
        print(f"An error occurred while fetching news for {stock}: {e}")
        return []
```0

Since the provided text is already in English, no translation is needed. The text appears to be a section header "Summary" followed by the beginning of a sentence about Tesla's European expansion. If you'd like me to translate something from Chinese to English, please provide the Chinese text.

### Investment Recommendation
This information includes **sentiment scoring for each article**, **overall summary**, and **investment recommendations**, giving us an intuitive understanding of Tesla's recent news and providing more references for decision-making.

---

## V. Advanced Development Ideas

1. **Combining Technical and Fundamental Analysis**: You can combine the "news sentiment" obtained from this tutorial with stock technical indicators and financial metrics to build a multi-factor analysis agent.  
2. **Automated Scheduling**: Use tools like Airflow or Cron to execute this script periodically to keep track of the latest news; push results to custom notifications or visualization dashboards.  
3. **Integrating Other LLMs or Plugins**: If you want to try different models' analysis effects, you can replace DeepSeek-R1 with others like ChatGPT, LLaMA, etc., to compare sentiment analysis accuracy and speed.  

---

## Conclusion

Using **yfinance** to scrape Tesla news, **MarkItDown** to extract webpage content, and **DeepSeek-R1** for sentiment analysis and investment advice generation, we can create a basic prototype for "**real-time news sentiment analysis**".  
- **Automation**: Capable of large-scale, continuous scraping of latest news.  
- **Scalability**: Flexible model replacement or further integration of results into more complex financial decision-making processes.  

Through these steps, you should now understand the complete workflow from "data acquisition" to "model analysis". Feel free to combine this approach with more **factor analysis** and **visualization** tools to build a more comprehensive and intelligent "multi-dimensional financial analysis" workflow!

If you have any questions about the operations or approaches discussed in this article, or would like to further explore the differences and practical experiences with various models, please leave a comment. Let's discover more possibilities for **AI applications in finance** together!

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。