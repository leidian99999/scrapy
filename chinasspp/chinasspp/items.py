# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinassppItem(scrapy.Item):
    BrandName = scrapy.Field() # 品牌名
    BrandArea = scrapy.Field() # 品牌地区
    BrandType = scrapy.Field() # 行业类型
    BrandFans = scrapy.Field() # 人气
    BrandURL  = scrapy.Field() # 详情URL
    BrandIntro= scrapy.Field() # 品牌介绍
    CompanyName = scrapy.Field() # 公司名