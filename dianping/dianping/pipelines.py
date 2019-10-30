# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
import  json


class DianpingPipeline(object):
    def __init__(self):
        # self.wb = Workbook()
        # self.ws = self.wb.active
        # self.ws.append(['店铺名称', '地点', '评论人数', '平均消费', '口味', '环境评分', '口味评分', '服务评分', ])  # 设置表头

        self.f = open("dianpingTEST.json", "wb")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content.encode("utf-8"))
        return item
        # line = [item['name'], item['location'], item['people'], item['money'], item['taste'], item['envir'],
    #         #         item['taste_score'], item['service']]  # 把数据中每一项整理出来
    #         # self.ws.append(line)  # 将数据以行的形式添加到xlsx中
    #         # self.wb.save('dazhong.xlsx')  # 保存xlsx文件
    #         # return item


    def spider_closed(self, spider):
        self.file.close()