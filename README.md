# Quant-Wiki 开源的中文量化百科

<img width="848" alt="image" src="https://github.com/user-attachments/assets/6d3b37b3-1bf3-4452-9833-f864c597c00d" />

## 👏欢迎访问 Quant Wiki 量化百科  [https://quant-wiki.com/](https://quant-wiki.com/)


> [!NOTE]
> 本项目正在开发中，欢迎大家参与贡献。

我们致力于量化知识的**开源**与**汉化**，打破国内外量化金融行业信息差。¶
量化投资（Quantitative Investing，简称 Quant）是一种以数学模型、统计分析和算法为基础的投资方式，是现代金融领域的重要分支。

Quant Wiki 致力于打造一个免费开放、持续更新的 量化金融（quantitative finance） 知识分享平台。在这里，大家可以学习量化交易的核心知识、常用模型、算法设计，以及交易中的实战策略。我们为大家准备了丰富的资料，包括因子模型、事件驱动策略、执行成本优化等内容，帮助大家快速掌握量化投资领域的核心技能，迈向专业化道路。

## **Content**

![Quant-Wiki框架](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/01/21/1737422354226-7661075b-8ae2-4716-9569-7c8ec95323ae.png)

## Contribution

如果您希望为 quant-wiki 做贡献，你需要做的是：

- fork 这个 repo。
- 在 `docs` 文件夹中增添对应的文件/文件夹。
- 在 `mkdocs.yml` 中的 `nav` 字段下进行更新。
- 提交 Pull Request 即可。

## Local Deploy

首先拉取代码，然后进入项目目录。

```bash
git clone https://github.com/LLMQuant/quant-wiki.git
cd quant-wiki
```

推荐使用 `venv` 创建虚拟环境，并安装依赖。

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

本地预览只需要运行如下命令即可：

```bash
mkdocs serve
```
