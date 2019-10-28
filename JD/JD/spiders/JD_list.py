# -*- coding: utf-8 -*-
import scrapy
import json

class JdListSpider(scrapy.Spider):
    name = 'JD_list'
    allowed_domains = ['3.cn']
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):
        jd_json = json.loads(str(response.body,encoding="gbk"),encoding="gbk")

        for data in jd_json["data"]:
            for data2 in data['s']:
                url1 = data2["n"].split('|')[0]
                title1 = data2["n"].split('|')[1]
                print(title1,url1)
                for data3 in data2["s"]:
                    url2 = data3["n"].split('|')[0]
                    title2 = data3["n"].split('|')[1]
                    print("=>",title2,url2)
                    for data4 in data3["s"]:
                        title3 = data4["n"].split('|')[1]
                        url3 = data4["n"].split('|')[0]
                        print("->",title3,url3)
        pass
