#-*-coding:utf-8-*-
# getlonlat.py
# from: mamq
# run: python3 getlonlat.py
from urllib.request import urlopen, quote
from pymongo import MongoClient
import json
import codecs
import sys
import os

path = sys.path[0] + os.sep

def getlnglat(address):
    """根据传入地名参数获取经纬度"""
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '申请好的密钥' # 浏览器端密钥
    address = quote(address) 
    uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak 
    req = urlopen(uri)
    res = req.read().decode() 
    temp = json.loads(res)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lat, lng

def jsondump(outfilename, dic):
    """传入保存路径和字典参数，保存数据到对应的文件中"""
    with codecs.open(path + outfilename + '.json', 'a', 'utf-8') as outfile:
        json.dump(dic, outfile, ensure_ascii=False)
        outfile.write('\n')

def convertfile(filename):
    file = codecs.open(path + filename, 'r', encoding='utf-8')
    outfilename = 'loc' + filename
    for line in file:
        dic = json.loads(line.strip())
        address = dic['地址']
        dic['lat'], dic['lng'] = getlnglat(address)
        jsondump(outfilename, dic)

def convertmongodb(host, dbname, collname):
    '''连接mongodb, 并根据其位置字段得到其坐标信息，进而更新数据库'''
    client = MongoClient(host, 27017)   
    db = client[dbname]
    collection = db[collname]
    for dic in collection.find():
        dic['lat'], dic['lng'] = getlnglat(dic['地址'])
        collection.save(dic) # 更新数据，并覆盖相同_id的记录
    print (dic)

if __name__ == '__main__':
    filename = '/home/mamq/test.json'
    # convertfile(filename)
    host = '192.168.1.101' # 需要连接的数据库所在ip
    dbname = 'landPlan'
    collname = 'xian'
    convertmongodb(host, dbname, collname)
    