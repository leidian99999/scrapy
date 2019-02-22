import pandas as pd
import json
from urllib.request import urlopen, quote
import requests

ak = 'z3KEtliyTGvj0bFudEkz4GO0GN8eQQa5'


def getlatlng_Baidu(address):
	"""根据传入地名参数获取经纬度"""
	url = 'http://api.map.baidu.com/geocoder/v2/'
	output = 'json'#输出数据的格式	
	add = quote(address) #由于本文地址变量为中文，为防止乱码，先用quote进行编码
	uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak 
	req = urlopen(uri)
	res = req.read().decode() 
	temp = json.loads(res)
	lat=temp['result']['location']['lat']
	lng=temp['result']['location']['lng']
	return lat,lng


if __name__ == '__main__':

	df1 = pd.read_csv('F:/temp/190222/sample2.csv')
	df1["address"] = df1["所属省"] + df1["地区"] + df1["收货地址"]
	# df1_dict = df1.to_dict('index') # CSV转为dict，index为index
	# df1_json = json.dumps(df1_dict) # dict转Json

	add = df1['address']

	latlist = []
	lnglist = []
	for i in add:
	    lat,lng=getlatlng_Baidu(i)
	    latlist.append(lat)
	    lnglist.append(lng)

	df1["lat"] = latlist
	df1["lng"] = lnglist


	df1.to_excel("F:/temp/190222/output1_Baidu.xlsx",index=False)
