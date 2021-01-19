# -*- coding: utf-8 -*-

import scrapy
from ..items import ZonghengItem
import re


class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['book.zongheng.com']

    # start_urls = ['http://book.zongheng.com/']

    def start_requests(self):
        for page in range(1, 2):
            url = f"http://book.zongheng.com/store/c0/c0/b0/u0/p{page}/v9/s9/t0/u0/i1/ALL.html"
            yield scrapy.Request(url, self.parse)
            # yield scrapy.Request(url, self.parse, meta={"proxy": "http://221.229.173.244:3100"})

    def parse(self, response):
        # print(response.request.url)
        datas = response.xpath('//div[@class="bookinfo"]')
        for data in datas:
            item = ZonghengItem()
            item['name'] = data.xpath('./div[@class="bookname"]/a/text()').extract_first()
            item['author'] = data.xpath('./div[@class="bookilnk"]/a[1]/text()').extract_first()
            item['fiction_class'] = data.xpath('./div[@class="bookilnk"]/a[2]/text()').extract_first()
            item['status'] = data.xpath('./div[@class="bookilnk"]/span/text()').extract_first().strip()
            item['content'] = re.sub(r'\u200b|\s', '', data.xpath('./div[@class="bookintro"]/text()').extract_first())
            item['link'] = data.xpath('./div[@class="bookname"]/a/@href').extract_first()
            yield item

