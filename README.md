# 小说网爬虫

1. 该爬虫使用Scrapy框架，实现了单项目多爬虫一起执行，定义了随机UserAgent的中间件，入库mongo和mysql数据库的Pipeline
2. Wordcloud文件夹里面的Wordcloud.py提供了生成词云功能，可以根据爬取下来的描述，生成词云。

## 注意事项

1. 使用前请确定Mongodb已安装并打开。
2. 如需使用代理，更改myspider.middlewares.ProxyMiddleware中的IP地址，并在settings的DOWNLOADER_MIDDLEWARES中，把注释打开
## 使用方法
请直接运行

```
python main.py
```


## scrapy框架流程图
![scrapy](.\scrapy.jpg)

