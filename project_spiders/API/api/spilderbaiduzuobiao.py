#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:zhoulong_GISER
# blog:https://blog.csdn.net/qq_33356563
from urllib.request import urlopen,quote
import json
import coordinateTransform

address="西安市"
ak='FA8atAaqd1wajikD56lPqtiaNCleCeyz'
url='http://api.map.baidu.com/geocoder/v2/?address='
output = 'json'
#ak = '你的ak'#需填入自己申请应用后生成的ak
add = quote(address)#本文城市变量为中文，为防止乱码，先用quote进行编码
url2 = url+add+'&output='+output+"&ak="+ak
req = urlopen(url2)
res  = req.read().decode()
temp = json.loads(res)
lng = temp['result']['location']['lng']  # 获取经度
lat = temp['result']['location']['lat']  # 获取纬度
list1=[lng,lat]
print('百度坐标为：',list1)
