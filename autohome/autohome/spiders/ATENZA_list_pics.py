# -*- coding: utf-8 -*-
import scrapy
from autohome.items import AutohomeItem

class AtenzaListPicsSpider(scrapy.Spider):
    name = 'ATENZA_list_pics'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/2809.html#pvareaid=2042214']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")
        for element in uiboxs:
            category = element.xpath("./div[@class = 'uibox-title']/a/text()").extract_first()
            img_name = element.xpath(".//ul/li/a/img/@title").extract()
            img_urls = element.xpath(".//ul/li/a/img/@src").getall()
            # for url in img_urls:
            #     url = "https:" + url
            #     print(url)
            img_urls = list(map(lambda url:response.urljoin(url),img_urls))
            item = AutohomeItem(category=category,image_urls=img_urls)
            yield item