# -*- coding: utf-8 -*-


# LOG_ENABLED=False

COMMANDS_MODULE = 'myspider.commands'

BOT_NAME = 'myspider'     # Scrapy项目的名字,这将用来构造默认 User-Agent,同时也用来log

SPIDER_MODULES = ['myspider.spiders']     # Scrapy搜索spider的模块列表
NEWSPIDER_MODULE = 'myspider.spiders'     # 使用 genspider 命令创建新spider的模块

DOWNLOADER_MIDDLEWARES = {
    'myspider.middlewares.RandomUserAgentMiddleware': 543,
    # 'myspider.middlewares.ProxyMiddleware': 100
}

ITEM_PIPELINES = {'myspider.pipelines.MongoPipeline': 301}

MONGO_URI = 'mongodb://admin:123456@10.117.9.213:27017/'  # 账号,密码,ip,端口号
MONGO_DB = 'zxk_test_db'  # 数据库名字


# Obey robots.txt rules   是否遵守robots.txt
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16) 开启线程数量，默认16
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3   # 下载器在下载同一个网站下，一个页面前需要等待的时间,该选项可以用来限制爬取速度,减轻服务器压力

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16    # 对单个网站进行并发请求的最大值。
# CONCURRENT_REQUESTS_PER_IP = 16        # 对单个IP进行并发请求的最大值。

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False                # 禁用Cookie（默认情况下启用）

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False          # 禁用Telnet控制台（默认启用）

# Override the default request headers:   覆盖默认请求标头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares     启用或禁用蜘蛛中间件
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'myspider.middlewares.myspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares      启用或禁用下载器中间件
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'myspider.middlewares.myspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions           启用或禁用扩展程序
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines       配置项目管道
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'myspider.pipelines.myspiderPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)   启用和配置AutoThrottle扩展（默认情况下禁用）
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True

# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5         # 初始下载延迟

# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60       # 高并发请求时最大延迟时间

# The average number of requests Scrapy should be sending in parallel to each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0        # Scrapy请求的平均数量应该并行发送每个远程服务器
# Enable showing throttling stats for every response received:      #启用显示所收到的每个响应的调节统计信息：
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)   # 启用和配置HTTP缓存（默认情况下禁用）
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
