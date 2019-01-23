import urllib.request
import time
from bs4 import BeautifulSoup
import requests


url = 'http://www.shicimingju.com/book/sanguoyanyi.html'

request = requests.get(url)
request.encoding = 'utf-8'
soup = BeautifulSoup(request.content, 'lxml')



# 得到所有的章节链接
oa_list = soup.select('.book-mulu > ul > li > a')

for oa in oa_list:
    title = oa.text
    print(title)