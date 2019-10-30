# -*- coding: utf-8 -*-
import scrapy
from Amazon.items import AmazonItem
from scrapy import Request


class MobileListSpider(scrapy.Spider):
    name = 'mobile_list'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=tea&rh=p_89%3ATAZO%2Cp_72%3A2661618011&dc&qid=1572418166&rnid=2661617011&ref=sr_nr_p_72_1']

    def parse(self, response):
        print(response.url)
        h2 = response.xpath('//div[contains(@class,"a-spacing-medium")]')
        for node in h2:
            item = AmazonItem()

            title = node.xpath('.//span[contains(@class,"a-size-base-plus")]/text()').extract()
            comment = node.xpath('.//span[@class="a-size-base"]/text()').extract()
            price = node.xpath('.//span[@class="a-offscreen"]/text()').extract()
            url = node.xpath('.//h2/a/@href').extract_first()
            # print(title)

            item["title"] = title
            item["comment"] = comment
            item["price"] = price
            item["url"] = "https://www.amazon.com" + str(url)

            yield item

            next = response.xpath('//div[contains(@class,"a-text-center")]/ul/li[contains(@class,"a-last")]/a/@href').extract_first()
            if next != None:
                next_url = "https://www.amazon.com" + next
                yield Request(next_url)
