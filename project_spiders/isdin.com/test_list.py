from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.isdin.com/producto/"

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
        # for x in i.select('div.title_1'):
        #     title1.append(x.text)
        # for x in i.select('div.title_2'):
        #     title2.append(x.text)
        # for x in i.select('div.title_3'):
        #     title3.append(x.text)
        # for x in i.select('div.vende'):
        #     vende.append(x.text)
        # for x in i.select('div.img'):
        #     img_url.append(x.img["src"])
        for x in i.select('div.item'):
            aa = detail_url.append(r"https://www.isdin.com" + x.a["href"])
            print(aa)
    return detail_url


def get_product_detail(detail_url):
    request = requests.get(detail_url)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.content, 'lxml')

    # zone1
    Indicaciones = soup.select("div.field_indicaciones h6")[0].text
    Indicaciones_detail = soup.select("div.field_indicaciones p")[0].text
    #
    # # zone2
    # Beneficios = soup.select("div.field_accion h6")[0].text
    # Beneficios_detail = []
    # for i in soup.select("div.field_accion div.zoneContainer p"):
    #     Beneficios_detail.append(i.text)
    #
    # # zone3
    # ModoDeEmpleo = soup.select("div.field_posologia h6")[0].text
    # ModoDeEmpleo_detail = []
    # for i in soup.select("div.field_posologia div.zoneContainer p"):
    #     ModoDeEmpleo_detail.append(i.text)
    #
    # # zone4
    # Composicion = soup.select("div.field_composicion h6")[0].text
    # Composicion_detail = soup.select("div.field_composicion p")[0].text

    return Indicaciones_detail


detail_URL = get_product_list(url)
