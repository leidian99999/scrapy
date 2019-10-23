from bs4 import BeautifulSoup
import requests
import pandas as pd


# 获取列表页所有品牌连接
def get_marca_list(url):	
    request = requests.get(url)
    request.encoding="utf-8"
    soup = BeautifulSoup(request.content,"lxml")
    marca_url = []
    Marca_name = []
    for i in soup.select("ul.son-menu-marca"):
        for x in i.select("li"):
            Marca_name.append(x.text)
            marca_url.append("https://www.isdin.com" + x.a["href"])
    return marca_url,Marca_name

# 获取列表页所有商品信息
def get_product_list(url):
    request = requests.get(url)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.content,'lxml')
    detail_url = []
    title1 = []
    title2 = []
    title3 = []
    img_url = []
    vende = []
    for i in soup.select("div.search-results"):
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
            detail_url.append("https://www.isdin.com" + x.a["href"].strip())
    return title1,title2,title3,vende,img_url,detail_url

def get_product_detail(detail_url):
    request = requests.get(detail_url)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.content, 'lxml')

    # zone1
    Indicaciones = soup.select("div.field_indicaciones h6")[0].text
    Indicaciones_detail = soup.select("div.field_indicaciones p")[0].text

    # zone2
    Beneficios = soup.select("div.field_accion h6")[0].text
    Beneficios_detail = []
    for i in soup.select("div.field_accion div.zoneContainer p"):
        Beneficios_detail.append(i.text)

    # zone3
    ModoDeEmpleo = soup.select("div.field_posologia h6")[0].text
    ModoDeEmpleo_detail = []
    for i in soup.select("div.field_posologia div.zoneContainer p"):
        ModoDeEmpleo_detail.append(i.text)

    # zone4
    Composicion = soup.select("div.field_composicion h6")[0].text
    Composicion_detail = soup.select("div.field_composicion p")[0].text

    return Indicaciones_detail,Beneficios_detail,ModoDeEmpleo_detail,Composicion_detail

# 输出
def output(dict_name,outpath,filename):
    data = pd.core.frame.DataFrame(dict_name) # dict转DF
    data.to_excel(outpath + filename + ".xlsx",index=False)

# 获取每个品牌列表页名称
def get_marca_title(url):
    request = requests.get(url)
    request.encoding="utf-8"
    soup = BeautifulSoup(request.content,"lxml")
    marca_title = soup.select("ul#crumbs li")[2].text
    return marca_title

if __name__ == "__main__":
    # 输出路径
    writer = r"D:\GitHub\scrapy\scrapy\project_spiders\isdin.com\test\\" # outpath
    # 起始URL
    url = "https://www.isdin.com/producto/"
    # 获取各品牌URL,和品牌名称
    (marca_url,Marca_name) = get_marca_list(url)
# print("共有{}个品牌".format(len(Marca_name)))

    for x in marca_url:
        print("正要开始盘" + str(x))
        # 解析得到各品牌列表页商品信息
        (title1,title2,title3,vende,img_url,detail_url) = get_product_list(x)
        (Indicaciones_detail,Beneficios_detail,ModoDeEmpleo_detail,Composicion_detail) = get_product_detail(detail_url)
        print("已经抓取完毕，准备输出！！")
        print("全体转换格式！")
        # 把list做成dict
        dict_list = { # dict_name
            "title1":title1,
            "title2":title2,
            "title3":title3,
            "vende" :vende,
            "img_url":img_url,
            "detail_url":detail_url,
            "Indicaciones_detail":Indicaciones_detail,
            "Beneficios_detail":Beneficios_detail,
            "ModoDeEmpleo_detail":ModoDeEmpleo_detail,
            "Composicion_detail":Composicion_detail
        }
        # 获取品牌名称,做filename
        marca_title  = get_marca_title(x) # filename
        print("输出start,文件名是{}".format(marca_title))
        output(dict_list,writer,marca_title)
        print("*"*50)
