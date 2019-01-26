from bs4 import BeautifulSoup
import requests
import pandas as pd

marca = "eryfotona"
size_url = "https://www.isdin.com/producto/eryfotona"
request = requests.get(size_url)
request.encoding = 'utf-8'
soup = BeautifulSoup(request.content,'lxml')

product_list = soup.select("div.search-results")

for i in product_list:
	title1 = []
	title2 = []
	title3 = []
	img_url = []
	vende = []
	detail_url = []
	for x in i.select('div.title_1'):
		title1.append(x.text)
	for x in i.select('div.title_2'):
		title2.append(x.text)
	for x in i.select('div.title_3'):
		title3.append(x.text)
	for x in i.select('div.vende'):
		vende.append(x.text)
	for x in i.select('div.img'):
		img_url.append(x.img["src"])
	for x in i.select('div.item'):
		detail_url.append("https://www.isdin.com" + x.a["href"])
	# for a in detail_url:
	# 	soup = BeautifulSoup(request.content,'lxml')




dict_list = {
	"title1":title1,
	"title2":title2,
	"title3":title3,
	"vende" :vende,
	"img_url":img_url,
	"detail_url":detail_url
}		

data = pd.core.frame.DataFrame(dict_list)
data.to_excel(r"D:\GitHub\scrapy\scrapy\project_spiders\isdin.com\marca\\" + marca + ".xlsx",index=False)