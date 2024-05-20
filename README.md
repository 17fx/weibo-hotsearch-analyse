# 微博热搜历史记录分析
本项目利用**腾讯云**提供的自然语言处理技术对微博热搜进行**文本分类**
*本项目纯属试用腾讯云api*
## 项目功能
根据已有项目的微博热搜历史数据进行自动化文本分类，并导出成csv格式数据
## 食用方法
- nlp.py中填入您的腾讯云API密钥
- raw 目录
  用于存放来自[weibo-trending-hot-search](https://github.com/justjavac/weibo-trending-hot-search)的raw文件，以备分析
- output 目录
  用于输出来自**腾讯云**的NLP文本分类分析的结果，以json格式输出
