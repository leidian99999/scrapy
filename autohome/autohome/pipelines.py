# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from autohome import settings

class AutohomePipeline(object):
    def __init__(self):
        # self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images') # 构建路径，本目录的上级目录的"images"文件夹
        self.path = r"D:\xiazai1\scrapy\autohome\pics\mazda\ATENZA"
        if not os.path.exists(self.path):
            os.mkdir(self.path)


    def process_item(self, item, spider):
        category = item['category']
        img_urls = item["img_urls"]
        img_name = item["img_name"]

        category_path = os.path.join(self.path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in img_urls:
            img_name = url.split('_')[-1]
            request.urlretrieve(url,os.path.join(category_path,img_name))

        return item


class AutohomeImagesPipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 这个方法是在发送下载请求之前调用
        # 其实这个方法本身就是去发送下载请求的
        request_objs = super(AutohomeImagesPipline, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item

    def file_path(self, request, response=None, info=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        path = super(AutohomeImagesPipline, self).file_path(request,response,info)
        category = request.item.get("category")
        images_store = settings.IMAGES_STORE