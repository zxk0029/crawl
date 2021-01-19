# -*- coding: utf-8 -*-

import scrapy
from ..items import QidianscrapyItem
from pyquery import PyQuery as pq
from io import BytesIO
from fontTools.ttLib import TTFont
import requests
import re
from lxml import etree


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['www.qidian.com']
    # custom_settings = {
    #     "item_pipelines": {"myspider.pipelines.MongoPipeline"}
    # }

    def start_requests(self):
        urls = []
        for page in range(1, 6):
            boy_url = f'https://www.qidian.com/all?&page={page}'
            girl_url = f'https://www.qidian.com/mm/all?&page={page}'
            urls.extend([boy_url, girl_url])

            yield scrapy.Request(boy_url, callback=self.parse)
            yield scrapy.Request(girl_url, callback=self.parse)

        # for url in urls:
        #     yield scrapy.Request(url, callback=self.parse)
            # yield Request(url, callback=self.parse, meta={"proxy": "https://221.229.173.129:2867"})

    def parse(self, response):
        self.logger.info(response.url)
        datas = response.xpath('//div[@class="book-mid-info"]')
        for data in datas:
            item = QidianscrapyItem()
            item['Name'] = data.xpath('h4/a/text()').extract_first()
            item['Author'] = data.xpath('p[1]/a[1]/text()').extract_first()
            item['Url'] = 'https:' + data.xpath('h4/a/@href').extract_first()
            item['FictionClass1'] = data.xpath('p[1]/a[2]/text()').extract_first()
            item['FictionClass2'] = data.xpath('p[1]/a[3]/text()').extract_first()
            item['State'] = data.xpath('p[1]/span/text()').extract_first()
            item['Content'] = data.xpath('p[2]/text()').extract_first().strip()
            # try:
            #     item['Number'] = self.get_encode(self.cmap, numberlist[i][:-1])
            # except KeyError:
            #     self.cmap = self.get_font(response.url)
            #     item['Number'] = self.get_encode(self.cmap, numberlist[i][:-1])
            # i += 1

            yield item
