from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.isdin.com/producto/fotoprotector-isdin/sunbrush-mineral-spf-30"
request = requests.get(url)
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


print(Composicion_detail)