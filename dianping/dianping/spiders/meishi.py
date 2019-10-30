# -*- coding: utf-8 -*-
import scrapy
import json
import re
from bs4 import BeautifulSoup
from scrapy.http import Request
from dianping.items import DianpingItem


class MeishiSpider(scrapy.Spider):
    name = 'meishi'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/beijing/ch10/g112']


    def parse(self, response):
        print("*"*50)
        # print(response.body)
        nodeList = response.xpath('//div[@class="tit"]')
        for node in nodeList:
            # item = DianpingItem()
            # name = node.xpath("//h4")
            # item['name'] = node.xpath("./h4")
            print("*" * 50)
            print(node)
        #     # yield item
        # pass

