# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item,Field

class Lianxi3Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 主要区域
    title = Field()
    price = Field()
    description =Field()
    address = Field()
    image_urls = Field()

    # 计算区域
    images = Field()
    location = Field()

    # 管理区域
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
