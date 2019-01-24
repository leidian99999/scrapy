from urllib.parse import quote
from lxml import etree

import json
import requests

# 全国有必胜客的城市，将城市放到文件中，一共380个城市
cities = []


# 第一步：从文件中读取城市信息
def get_citis():
    '''从文件中获取城市'''
    file_name = 'cities.txt'
    with open(file_name,'r',encoding='UTF-8-sig') as file:
        for line in file:
            city = line.replace('\n','')
            cities.append(city)

count = 1
results = {}

# 第二步：依次遍历cities列表，将每个城市作为参数，构建Cookies的iplocation字段。
# 依次遍历所有城市的餐厅
for city in cities:
    restaurants = get_stores(city,count)
    results[city] = restaurants


# 第三步：再以POST方式携带COOKIE去请求必胜客服务器，最后在对返回页面数据惊醒提取
def get_stores(city,count):
    '''根据城市获取餐厅信息'''
    session = requests.Session()
    # 对【城市|0|0】进行 Url 编码
    city_urlencode = quote(city + '|0|0')
    # 用来存储首页的cookies
    cookies = requests.cookies.RequestsCookieJar()