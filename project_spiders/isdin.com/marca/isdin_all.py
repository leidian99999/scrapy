from bs4 import BeautifulSoup
import requests
import pandas as pd



def get_marca_list(url):	
    request = requests.get(url)
    request.encoding="utf-8"
    soup = BeautifulSoup(request.content,"lxml")
    for i in soup.select("ul.son-menu-marca"):
        marca_url = []
        Marca_name = []
        for x in i.select("li"):
            Marca_name.append(x.text)
            marca_url.append("https://www.isdin.com" + x.a["href"])
    return marca_url,Marca_name

def get_product_list(url):
    request = requests.get(url)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.content,'lxml')
    for i in soup.select("div.search-results"):
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
    return title1,title2,title3,vende,img_url,detail_url


def output(dict_name,outpath,filename):
    data = pd.core.frame.DataFrame(dict_name)
    data.to_excel(outpath + filename + ".xlsx",index=False)

def get_marca_title(url):
    request = requests.get(url)
    request.encoding="utf-8"
    soup = BeautifulSoup(request.content,"lxml")
    marca_title = soup.select("ul#crumbs li")[2].text
    return marca_title

if __name__ == "__main__":
	writer = r"D:\GitHub\scrapy\scrapy\project_spiders\isdin.com\test\\"
	url = "https://www.isdin.com/producto/"
	(marca_url,Marca_name) = get_marca_list(url)
# print("共有{}个品牌".format(len(Marca_name)))

	for x in marca_url:
	    print("正要开始盘" + str(x))
	    (title1,title2,title3,vende,img_url,detail_url) = get_product_list(x)
	    print("已经抓取完毕，准备输出！！")
	    print("全体转换格式！")
	    dict_list = {
	        "title1":title1,
	        "title2":title2,
	        "title3":title3,
	        "vende" :vende,
	        "img_url":img_url,
	        "detail_url":detail_url
	    }

	    marca_title  = get_marca_title(x)
	    print("输出start,文件名是{}".format(marca_title))
	    output(dict_list,writer,marca_title)
	    print("*"*50)
