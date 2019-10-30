# -*- coding: utf-8 -*-
import scrapy
from chinasspp.items import ChinassppItem

class SsppMeishicanyinSpider(scrapy.Spider):
    name = 'sspp_meishicanyin'
    allowed_domains = ['chinasspp.com']
    start_urls = ['http://www.chinasspp.com/brand/%E7%BE%8E%E9%A3%9F%E9%A4%90%E9%A5%AE/']

    def parse(self, response):
        elements = response.xpath('//div[@class="l"]/div[@class="brand"]')
        for element in elements:
            item = ChinassppItem()

            item["BrandName"] = element.xpath('./p[@class="first"]/a/text()').extract()[0]
            item["BrandArea"] = element.xpath('./p[@class="last"]/text()').extract()[0]
            item["BrandType"] = element.xpath('.//span/text()').extract()[0]
            item["BrandFans"] = element.xpath('./p[@class="last"]/i/text()').extract()[0]
            item["BrandURL"] = element.xpath('./p[@class="first"]/a/@href').extract()[0]
            item["BrandIntro"] = element.xpath('./p[2]/text()').extract()[0]
            item["CompanyName"] = element.xpath('./p[@class="first"]/text()').extract()[-1].strip()

            yield item




"""
BrandName = scrapy.Field() # 品牌名
    BrandArea = scrapy.Field() # 品牌地区
    BrandType = scrapy.Field() # 行业类型
    BrandFans = scrapy.Field() # 人气
    BrandURL  = scrapy.Field() # 详情URL
    BrandIntro= scrapy.Field() # 品牌介绍
    CompanyName = scrapy.Field() # 公司名
"""



# 品牌名
# //div[@class="l"]/div[@class="brand"]/p[@class="first"]/a/text()
# 行业类型
# //div[@class="l"]/div[@class="brand"]//span/text()
# 公司名
# //div[@class="l"]/div[@class="brand"]/p[@class="first"]/text()
# 品牌简介
# //div[@class="l"]/div[@class="brand"]/p[2]/text()
# 品牌地区
# //div[@class="l"]/div[@class="brand"]/p[@class="last"]/text()
# 人气
# //div[@class="l"]/div[@class="brand"]/p[@class="last"]/i/text()
# 详情URL
# //div[@class="l"]/div[@class="brand"]/p[@class="first"]/a/@href
