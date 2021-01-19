from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return "[options]"

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spiders.list()
        for name in spider_list or args:
            self.crawler_process.crawl(name, **opts.__dict__)
            print(f"此时启动的爬虫为：{name}")
        self.crawler_process.start()


''' 获取爬虫名字的另一种方式
from scrapy.utils.project import get_project_settings
from scrapy import spiderloader

settings = get_project_settings()
spider_loader = spiderloader.SpiderLoader.from_settings(settings)
spiders = spider_loader.list()
print(spiders)
'''