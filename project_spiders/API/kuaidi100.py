import pandas as pd
import json
from urllib.request import urlopen, quote
import requests

# ak = 'z3KEtliyTGvj0bFudEkz4GO0GN8eQQa5'


def getlatlng_Kuaidi100(TrackingNum):
	"""根据传入地名参数获取经纬度"""
	url = 'http://www.kuaidi100.com/query'
	carrier = 'jd'#输出数据的格式	
	trickingNum = quote(TrackingNum) #由于本文地址变量为中文，为防止乱码，先用quote进行编码
	uri = url + '?' + 'type=' + carrier  + '&postid=' + trickingNum 
	req = urlopen(uri)
	res = req.read().decode() 
	temp = json.loads(res)
	
	time=temp['data']['time']
	# context=temp['data']['context']

	return time,context


if __name__ == '__main__':

	df1 = pd.read_csv('F:/temp/190225/jdtest.csv')

	timelist = []
	contextlist = []


	trickingNum = df1["物流单号"]

	for i in trickingNum:
	    time,context=getlatlng_Kuaidi100(i)
	    timelist.append(time)
	    contextlist.append(context)
	    



	df1["time"] = latlist
	df1["context"] = lnglist

	df1.to_excel("F:/temp/190225/output190211chenmo_kuaidi100.xlsx",index=False)
