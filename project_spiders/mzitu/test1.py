# coding=utf-8
import requests
from bs4 import BeautifulSoup

url = 'https://www.mzitu.com/page/3/'

request = requests.get(url)
soup = BeautifulSoup(request.text,'html.parser')

page = int(soup.select("div.nav-links a")[-2].text) # 总页数

title = []
for i in soup.select("div.postlist"):
    for x in i.select("li"):
        title.append('')