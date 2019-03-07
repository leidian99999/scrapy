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

    if 'lat' in temp['result']['location']['lat']:
    	lat=temp['result']['location']['lat']
	else:
	    pass
	
	if 'lng' in temp:
    	lng=temp['result']['location']['lng']
	else:
	    pass

    if 'precise' in temp:
    	precise = temp['precise']
	else:
	    pass

    if 'confidence' in temp:
    	confidence = temp['confidence']
	else:
	    pass

    if 'comprehension' in temp:
    	comprehension = temp['comprehension']
	else:
	    pass
	
    if 'level' in temp:
		level = temp['level']
	else:
	    pass

	
	
	return lat,lng,precise,confidence,comprehension,level


if __name__ == '__main__':

	df1 = pd.read_csv(r'F:/temp/190306/ZJ5000.csv')
	# print(df1.columns)
	# exit()
	# df1["address"] = df1["所属省"] + df1["地区"] + df1["收货地址"]
	# df1_dict = df1.to_dict('index') # CSV转为dict，index为index
	# df1_json = json.dumps(df1_dict) # dict转Json

	add = df1['导航地址']

	latlist = []
	lnglist = []
	preciselist = []
	confidencelist = []
	comprehensionlist = []
	levellist = []
	for i in add:
	    lat,lng,precise,confidence,comprehension,level=getlatlng_Baidu(i)
	    latlist.append(lat)
	    lnglist.append(lng)
	    preciselist.append(precise)
	    confidencelist.append(confidence)
	    comprehensionlist.append(comprehension)
	    levellist.append(level)

	df1["lat"] = latlist
	df1["lng"] = lnglist
	df1["precise"] = preciselist
	df1["confidence"] = confidencelist
	df1["comprehension"] = comprehensionlist
	df1["level"] = levellist

	df1.to_excel("F:/temp/190306/ZJ5000_BaiduAPI_test.xlsx",index=False)
