 # -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from bmw.items import BmwItem

class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']
    rules = (
        Rule(LinkExtractor(allow="https://car.autohome.com.cn/pic/series/65.+"),callback="parse_page",follow=True),
    )

    def parse_page(self,response):
        category = response.xpath("//div[@class='uibox']/div[1]/text()").extract_first()
        srcs = response.xpath("//div[contains(@class,'uibox-con')]//li/a/img/@src").getall()
        srcs = list(map(lambda x:x.replace("240x180_0_q95_c42_",""),srcs))
        srcs = list(map(lambda x:response.urljoin(x),srcs))
        yield BmwItem(category=category,urls=srcs)

    # def parse(self, response):
    #     uiboxs = response.xpath("//div[@class='uibox']")[1:]
    #     for uibox in uiboxs:
    #         category = uibox.xpath(".//div[@class='uibox-title']/a[1]/text()").get()
    #         urls = uibox.xpath(".//ul/li/a/img/@src").getall()
    #         urls = list(map(lambda x:response.urljoin(x),urls))
    #         item = BmwItem(category=category,urls=urls)
    #         yield item

