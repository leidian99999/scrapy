# -*- coding: utf-8 -*-
import scrapy
import json
from zhihu_Ajax.items import ZhihuAjaxItem

class ZhihuspideraSpider(scrapy.Spider):
    name = 'ajax_zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/columns/zimei/articles?limit=20&offset=0']

    def parse(self, response):
        # print(response.body)
        jsonBody = json.loads(response.body.decode('gbk').encode('utf-8'))
        articles = jsonBody['data']
        for art in articles:
            item = ZhihuAjaxItem()
            item['title'] = art['title']
            item['name'] = art['author']['name']
            item['headline'] = art['author']['headline']
            item['url'] = art['url']
            yield item

        if articles:
            yield scrapy.Request(jsonBody['paging']['next'], callback=self.parse)
        else:
            print("获取完毕！")
