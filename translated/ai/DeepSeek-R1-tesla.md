---
{}
---

Here's the English translation of the Chinese text, maintaining technical accuracy, markdown formatting, math expressions, and code elements:

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# In-Depth Analysis: How to Use DeepSeek-R1 for Sentiment Analysis of Tesla-Related News and Generate Investment Advice

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

In stock investment, **news sentiment** often has a significant impact on stock prices. Real-time monitoring and analysis of news information can help us gauge market sentiment and optimize investment decisions. This article uses Tesla (**TSLA**) as an example, combining **Yahoo Finance**, **MarkItDown**, and the **DeepSeek-R1** model to demonstrate the complete practical process from "obtaining news → extracting content → sentiment analysis → investment advice."

> **Target audience**: Quantitative engineers, data scientists, fund managers interested in automated financial news analysis, or learners who want to quickly get started with news sentiment analysis.

## Functionality Overview

1. **Scrape Tesla-related news**: Use `yfinance` to obtain the latest news for TSLA.
2. **Extract and clean content**: Use the MarkItDown library to parse webpage content and perform simple regex cleaning on the text.
3. **Sentiment analysis and recommendations**: Based on the DeepSeek-R1 model, score multiple news articles and output investment advice.

Through these steps, you can quickly build a "mini sentiment radar" that analyzes multiple news articles combined.

## I. Prepare the Environment

1. Install Python dependencies:
   ```
   pip install yfinance markitdown langchain-ollama
   ```
2. Ensure that the **DeepSeek-R1** model has been successfully deployed locally or on a server and can be called via [Ollama](https://ollama.ai/) or similar methods.

> If you don't have the DeepSeek-R1 model yet, you can try installing the corresponding environment locally or replace it with other compatible models.

---

## II. Obtain Tesla (TSLA) Related News

### 2.1 Write the `get_tesla_news` Function

The following function uses the `Ticker` object from the `yfinance` library to scrape Tesla-related news and extract key fields (title, summary, link, publication date):

```python
import yfinance as yf

def get_tesla_news(limit=5):
    tesla = yf.Ticker("TSLA")
    news = tesla.news
    return [{'title': item['title'],
             'summary': item['summary'],
             'link': item['link'],
             'published': item['providerPublishTime']} 
            for item in news[:limit]]
```

#### Example Call

```python
tesla_news = get_tesla_news()
print(tesla_news)
```

The structure obtained is like:

```python
[
    {
        'title': 'Tesla Q4 Earnings: A Beat on Estimates?',
        'summary': 'Tesla is set to report Q4 earnings...',
        'link': 'https://finance.yahoo.com/news/tesla-q4-earnings-beat-estimates-123456789.html',
        'published': 1642524000
    },
    # More news items...
]
```

## III. Extract and Clean News Content

### 3.1 Use MarkItDown to Parse Webpages

`MarkItDown` can help us convert webpage HTML into plain text, including titles and body content. While extracting the text, we will remove some **links** and **special characters** to make subsequent analysis cleaner.

```python
import re
from markitdown import MarkItDown

def extract_content(url):
    md = MarkItDown()
    content = md.from_url(url)
    # Remove links and special characters
    clean_content = re.sub(r'\[.*?\]|\(.*?\)|[^\w\s]', '', content)
    return clean_content.strip()
```

### 3.2 Obtain and Integrate All News Texts

With `get_tesla_news` and `extract_content`, we can extract all news at once. Example as follows:

```python
def get_all_news_content(limit=5):
    news_list = get_tesla_news(limit)
    for item in news_list:
        item['content'] = extract_content(item['link'])
    return news_list

all_news = get_all_news_content()
```

The resulting `all_news` is the integrated result containing all fields (title, summary, URL, content, etc.).

![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2025/02/26/1740600002331-9d6ca907-4b79-48d9-bb67-94245f893670.png)

## IV. Use DeepSeek-R1 for Sentiment Analysis and Investment Advice

### 4.1 Bind DeepSeek-R1 with LangChain

This example uses [OllamaLLM](https://pypi.org/project/langchain-ollama/) as the interface to call DeepSeek-R1. Multiple news articles are combined and sent to the LLM for sentiment analysis.

```python
from langchain_ollama import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="deepseek-r1")
```

### 4.2 Write Prompt Template

We want the model to provide "Positive/Negative/Neutral" sentiment evaluations for each article, and give investment advice based on a summary of all articles. This requirement can be written as a `PromptTemplate` prompt to be passed to the LLM:

```python
template = """
Analyze the sentiment of each news article about Tesla and provide an overall investment recommendation:

{news_texts}

For each article, provide a sentiment label (Positive/Negative/Neutral).
Then, summarize the overall sentiment and give an investment recommendation.

Format your response as follows:
```json
{{
   "Article Title 1": "Sentiment",
   "Article Title 2": "Sentiment",
   ...
}}
```
### Summary
[Your summary here]
### Investment Recommendation
[Your recommendation here]
"""

prompt = PromptTemplate(
    input_variables=["news_texts"],
    template=template
)
```

### 4.3 Call the Model and Output Results

Combine the extracted content texts (`all_news`) into a list, pass it as `news_texts` to the PromptTemplate, and finally call the LLM:

```python
news_texts = "\n\n".join([f"Title: {item['title']}\nContent: {item['content']}" for item in all_news])
chain = prompt | llm
result = chain.invoke({"news_texts": news_texts})
print(result)
```

When DeepSeek-R1 completes generation, you will see results similar to the following:

```json
{
   "Tesla Q4 Earnings: A Beat on Estimates?": "Positive",
   "Elon Musk's Latest Statement Sparks Controversy": "Neutral",
   ...
}
```
### Summary
Based on the articles, Tesla's expansion in Europe...
### Investment Recommendation
Tesla continues to demonstrate strong performance...
"
```

This information includes **sentiment scores for each article**, an **overall summary**, and **investment advice**, giving us an intuitive understanding of recent Tesla news and providing more references for decision-making.

---

## V. Further Advanced Ideas

1. **Combine Technical and Fundamental Analysis**: You can combine the "news sentiment" obtained in this tutorial with the stock's technical indicators and financial indicators to build a multi-factor analysis agent.
2. **Automated Scheduling**: Use tools like Airflow or Cron to regularly execute this script, keeping track of the latest news; push results to custom notifications or visualization dashboards.
3. **Integrate Other LLMs or Plugins**: If you want to try the analysis effects of different models, you can also replace DeepSeek-R1 with others such as ChatGPT, LLaMA, etc., to compare the accuracy and speed of sentiment judgments.

---

## Conclusion

By using **yfinance** to scrape Tesla news, **MarkItDown** to extract webpage content, and then **DeepSeek-R1** for sentiment analysis and investment advice generation, we can implement a simple prototype of "**real-time news sentiment analysis**".
- **Automation**: Can scrape the latest news on a large scale and continuously.
- **Scalability**: Can flexibly replace models or further integrate results into more complex financial decision-making processes.

We believe that through the above steps, you have mastered a complete set of ideas from "data acquisition" to "model analysis". Feel free to combine this approach with more **factor analysis** and **visualization** tools to build a more comprehensive and intelligent "multi-dimensional financial analysis" workflow!

If you have any questions about the operations or ideas in this article, or want to further discuss the differences and practical experiences of various models, please leave a comment. Let's explore more possibilities of **AI applications in finance** together!

## About LLMQuant

Here's the English translation, maintaining the technical accuracy and formatting:

LLMQuant is a cutting-edge community composed of individuals from the world's top universities and quantitative finance professionals, dedicated to exploring the infinite possibilities in the fields of Artificial Intelligence (AI) and Quantitative Finance (Quant). Our team members come from renowned global institutions such as the University of Cambridge, University of Oxford, Harvard University, ETH Zurich, Peking University, and the University of Science and Technology of China. Our external advisors are from leading companies including Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top-tier private equity firms in China.