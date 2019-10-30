# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencenthrItem(scrapy.Item):
    positionName = scrapy.Field()
    positionLink = scrapy.Field()
    positionType = scrapy.Field()
    peopleNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime  = scrapy.Field()
