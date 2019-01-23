import pandas as pd

from bs4 import BeautifulSoup
import requests
request = requests.get('http://house.lanfw.com/xm/search-y5')
request.encoding = 'utf-8'
soup = BeautifulSoup(request.text,'lxml')
houses = soup.select('.lpList')
housesDetails = []
for house in houses:
  #获取楼盘名字
  houseName = house.select('.title h2 a')[0].text
  #将所有楼盘信息做成楼盘信息字典
  houseDetails = {}
  houseDetails['houseName'] = houseName
  housesDetails.append(houseDetails)
  print(houseDetails)