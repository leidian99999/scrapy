# -*- coding: utf-8 -*-
# import scrapy

from scrapy.spiders import Spider
from douban_movie.items import Dou



class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        pass
