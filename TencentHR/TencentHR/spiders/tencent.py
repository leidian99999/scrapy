# -*- coding: utf-8 -*-
import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        pass
