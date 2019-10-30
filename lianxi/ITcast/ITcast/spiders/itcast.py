#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
from ITcast.items import  ItcastItem




class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")
        # 用来保存所有的item字段
        items = []
        for node in node_list:
            # 创建item字段对象，用来储存信息
            item = ItcastItem()
            # .extract()将xpath对象转换为Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]
            # 返回提取到的每个item数据，给管道文件处理，同时还会回来继续执行后面的代码(for循环）
            yield item


            # items.append(item)
        # return items