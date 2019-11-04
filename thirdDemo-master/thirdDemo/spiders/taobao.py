# -*- coding: utf-8 -*-
import time

import scrapy

from scrapy.http import Request
import re
from thirdDemo.items import ThirddemoItem

from thirdDemo.settings import detail_headers


class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        key = '德国阳光玻尿酸'
        for i in range(0,101):
            url = 'https://s.taobao.com/search?q=' + str(key) + '&s=' + str(44*i)
            print(url)
            yield Request(url=url, callback=self.page)

    def page(self, response):
        body = response.body.decode('utf-8','ignore')
        pattam_id = '"nid":"(.*?)"'
        all_id = re.compile(pattam_id).findall(body)
        for i in range(0, len(all_id)):
            this_id = all_id[i]
            url = 'https://item.taobao.com/item.htm?id=' + str(this_id)


            yield Request(url=url, callback=self.next)


    def next(self, response):
        item = ThirddemoItem()
        url = response.url
        # 获取商品是属于天猫的、天猫超市的、还是淘宝的。
        pattam_url = 'https://(.*?).com'
        subdomain = re.compile(pattam_url).findall(url)

        # 获取商品的标题
        if subdomain[0] != 'item.taobao': # 如果不属于淘宝子域名，执行if语句里面的代码
            title = response.xpath("//div[@class='tb-detail-hd']/h1/text()").extract()
        else:
            title = response.xpath("//h3[@class='tb-main-title']/@data-title").extract()

        item['title'] = title

        # 获取商品的链接网址
        item['link'] = url

        # 获取商品的正常的价格
        if subdomain[0] != 'item.taobao': # 如果不属于淘宝子域名，执行if语句里面的代码
            pattam_price = '"defaultItemPrice":"(.*?)"'
            price = re.compile(pattam_price).findall(response.body.decode('utf-8', 'ignore')) # 天猫

        else:
            price = response.xpath("//em[@class = 'tb-rmb-num']/text()").extract() # 淘宝

        # print(price)
        item['price'] = price

        pattam_id = 'id=(\d+)'
        this_id = re.compile(pattam_id).findall(url)[0]
        # 构造具有评论数量信息的包的网址
        comment_url = 'https://dsr-rate.tmall.com/list_dsr_info.htm?itemId=' + str(this_id)

        import requests
        comment_data = requests.get(url = comment_url, headers=detail_headers).text
        pattam_comment = '\"rateTotal\":(\d+)'
        comment = re.search(pattam_comment,comment_data)
        comment1 = comment.groups(1)
        item['comment'] = comment1[0]

        yield item
