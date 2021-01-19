from scrapy.cmdline import execute
import os
import sys

# 添加当前项目的绝对地址
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# execute('scrapy crawl qidian'.split())
# execute('scrapy crawl zongheng'.split())

# 执行所有的爬虫
execute('scrapy crawlall --nolog'.split())
