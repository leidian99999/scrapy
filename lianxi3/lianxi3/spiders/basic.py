# -*- coding: utf-8 -*-
import scrapy
import datetime
# import urlparse
import socket
import re
from lianxi3.items import Lianxi3Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ('http://web:9312/properties/property_000000.html',)

    def parse(self, response):

        '''
        contract 内容要紧接着函数名的注释，以@开头




        '''

        '''
        # 抓取日志中的数据（DEBUG: ...）
        # self.log("title: %s" % response.xpath('//*[@itemprop="name"][1]/text()').extract())
        # self.log("price: %s" % response.xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+'))
        # self.log("description: %s" % response.xpath('//*[@itemprop="description"][1]/text()').extract())
        # self.log("address: %s" % response.xpath('//*[@itemtype="http://schema.org/Place"][1]/text()').extract())
        # self.log("image_urls: %s" % response.xpath('//*[@itemprop="image"][1]/@src').extract())

        '''

        '''
        # 使用item类
        # item = Lianxi3Item() # 实例化
        # item["title"] = response.xpath('//*[@itemprop="name"][1]/text()').extract()
        # item["price"] = response.xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+')
        # item["description"] = response.xpath('//*[@itemprop="description"][1]/text()').extract()
        # item["address"] = response.xpath('//*[@itemtype="http://schema.org/Place"][1]/text()').extract()
        # item["image_urls"] = response.xpath('//*[@itemprop="image"][1]/@src').extract()

        # return item
       
        '''



        # ItemLoader——替代杂乱的extract()和xpath()操作
        # http://doc.scrapy.org/en/latest/topics/loaders.html
        '''
        join():把多个结果联系在一起
        MapCompose(unicode.strip):去除首尾空白符
        MapCompose(unicode.strip, unicode.title):去除首尾空白符 + 单词首字母大写
        MapCompose(float):将字符串转为数值
        MapCompose(lambda i: i.replace(',', ''), float):将字符串转为数值，并忽略可能存在的','字符
        MapCompose(lambda i: urlparse.urljoin(response.url, i)) : 以response.url为基础,将相对路径转成绝对路径
        '''


        l = ItemLoader(item=Lianxi3Item(),response=response)

        l.add_xpath('title', '//*[@itemprop="name"][1]/text()',MapCompose(unicode.strip, unicode.title))
        l.add_xpath('price', './/*[@itemprop="price"][1]/text()',MapCompose(lambda i: i.replace(',', ''), float),re='[,.0-9]+')
        l.add_xpath('description', '//*[@itemprop="description"][1]/text()',MapCompose(unicode.strip), Join())
        l.add_xpath('address','//*[@itemtype="http://schema.org/Place"][1]/text()',MapCompose(unicode.strip))
        l.add_xpath('image_urls', '//*[@itemprop="image"][1]/@src',MapCompose(lambda i: urlparse.urljoin(response.url, i)))

        return l.load_item()

        # 设置管理字段

        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())