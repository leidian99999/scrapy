# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import JsonItemExporter



'''
# class ChinassppPipeline(object):
        
#     def __init__(self): # 第一次执行，之后不执行
#         self.f = open("chinasspp_meishi_pgall.json","wb")
#
#
#     def process_item(self, item, spider): # 每次item传来时执行
#         content = json.dumps(dict(item),ensure_ascii=False)+ ",\n"
#         self.f.write(content.encode("utf-8"))
#         return item
#
#
#     def close_spider(self,spider): # 最后一次执行，之前不执行
#         self.f.close()
'''  # 原始存储方法


class ChinassppPipeline(object):
    '''
    返回列表，每个元素是一个dict,内含item元素
    '''
    def __init__(self): # 第一次执行，之后不执行
        self.f = open("chinasspp_meishi_pgall_list.json","wb")
        self.exporter = JsonItemExporter(self.f,ensure_ascii = False,encoding = 'utf-8')
        self.exporter.start_exporting() # 开始执行导入
    def open_spider(self,spider):
        print('爬虫开始了')


    def process_item(self, item, spider): # 每次item传来时执行
        self.exporter.export_item(item)
        return item


    def close_spider(self,spider): # 最后一次执行，之前不执行
        self.exporter.finish_exporting() # 结束导入
        self.f.close()
        print('爬虫结束了')