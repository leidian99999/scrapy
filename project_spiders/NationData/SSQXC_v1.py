import requests
from lxml import etree
import csv

# 主页源代码爬取
url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

# data = requests.get(url,headers = headers).text # 直接这样会出现乱码。。。
response = requests.get(url,headers = headers)
response.encoding = response.apparent_encoding # 网站现在使用的字符编码
data = response.text

# 省级名称、URL获取
selector = etree.HTML(data)


print()