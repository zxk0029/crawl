# -*- coding: utf-8 -*-

import pymongo


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod  # 类方法（不需要实例化类就可以被类本身调用）  eg: MongoPipeline.from_crawler()
    # cls : 表示没用被实例化的类本身   实际调用的是 init()函数，如果init接受参数，cls就需要参数
    def from_crawler(cls, crawler):  # from_crawler函数的目的是从settings.py获取全局变量
        return cls(
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_uri=crawler.settings.get('MONGO_URI'),
            # # 从settings.py获取全局变量，如果没获取，返回"BOT_NAME"
            # coll_name=crawler.settings.get('COLL_NAME', crawler.settings.get('BOT_NAME'))
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        coll_name = spider.name                 # 获取xxxSpider类中定义的全局变量name
        # coll_name = item.__class__.__name__   # 获取item类的名字
        # coll_name = item.coll_name
        # spider.log(f"coll_name: {coll_name}")

        self.db[coll_name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
