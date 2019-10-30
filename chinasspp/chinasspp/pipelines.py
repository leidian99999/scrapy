# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class ChinassppPipeline(object):
    def __init__(self): # 第一次执行，之后不执行
        self.f = open("chinasspp_meishi_pg1.json","wb")


    def process_item(self, item, spider): # 每次item传来时执行
        content = json.dumps(dict(item),ensure_ascii=False)+ ",\n"
        self.f.write(content.encode("utf-8"))
        return item


    def close_spider(self,spider): # 最后一次执行，之前不执行
        self.f.close()