import requests
import re
'''
https://s.taobao.com/search?initiative_id=tbindexz_20170315&ie=utf8&spm=a21bo.50862.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E4%B9%A6%E5%8C%85&suggest=0_1&_input_charset=utf-8&wq=shubao&suggest_query=shubao&source=suggest
https://s.taobao.com/search?initiative_id=tbindexz_20170315&ie=utf8&spm=a21bo.50862.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E4%B9%A6%E5%8C%85&suggest=0_1&_input_charset=utf-8&wq=shubao&suggest_query=shubao&source=suggest&bcoffset=0&ntoffset=0&p4ppushleft=1%2C48&s=44
https://s.taobao.com/search?initiative_id=tbindexz_20170315&ie=utf8&spm=a21bo.50862.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E4%B9%A6%E5%8C%85&suggest=0_1&_input_charset=utf-8&wq=shubao&suggest_query=shubao&source=suggest&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=88
'''
#获取text
def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding= r.apparent_encoding
		return r.text
	except:
		return ""
 
 
def paserPage(list,html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d.]*\"',html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			list.append([price,title])
	except:
		print("出丑") 
 
 
def printGoodsList(list):
	tplt ="{:4}\t{:8}\t{:16}"
	print(tplt.format("序号", "价格", "商品"))
	count = 0
	for g in list:
		count=count+1
		print(tplt.format(count,g[0],g[1]))
      
 
def main():
	goods = '玻尿酸'
	depth = 3 #爬取页数
	start_url = 'https://s.taobao.com/search?q=' + goods
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44*i)
			html = getHTMLText(url)
			#print(html)
			paserPage(infoList,html)
		except:
			continue
	#print(infoList)
	printGoodsList(infoList)
 
main()
 
 
