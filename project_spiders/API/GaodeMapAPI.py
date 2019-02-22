import pandas as pd
import json
from urllib.request import urlopen, quote
import requests


#申请的key
ak='f30c9d52b003c2b3ac089e2672e18baf'

#传入地址，返回对应地址的经纬度信息
def getlatlng_Gaode(address):
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
    contest=contest['geocodes'][0]['location']
    return contest





if __name__ == '__main__':


	df1 = pd.read_csv('F:/temp/190222/sample2.csv')
	df1["address"] = df1["所属省"] + df1["地区"] + df1["收货地址"]
	add = df1['address']

	locallist = []
	for i in add:
	    location=getlatlng_Gaode(i)
	    locallist.append(location)

	df1["location"] = locallist
	split = pd.DataFrame((x.split(',') for x in df1['location']), index=df1.index, columns=['lng','lat'])
	df1 = pd.merge(df1,split,left_index=True,right_index=True)
	df1 = df1.drop(columns = ['location'])
	df1.to_excel("F:/temp/190222/output1_Gaode.xlsx",index=False)
    # print(getlatlng_Gaode("兰州西站"))