from bs4 import BeautifulSoup
import requests
import pandas as pd



size_url = "https://www.isdin.com/producto/fotoprotector-isdin"
request = requests.get(size_url)
request.encoding = 'utf-8'
soup = BeautifulSoup(request.content,'lxml')

product_list = soup.select("div.search-results")

item_list = []

for product in product_list:
    for title in product.find_all(attrs={'class': 'title_2'}):
        title2 = list(title.get_text())
        houseDetails2 = {}
        houseDetails2['houseName2'] = title2
        item_list.append(houseDetails2)
    for title in product.find_all(attrs={'class': 'title_1'}):
        title1 = title.get_text()
        houseDetails1 = {}
        houseDetails1['houseName1'] = title1
        item_list.append(houseDetails1)


# df = pd.DataFrame(item_list, columns=item_list[0].keys())
# writer = pd.ExcelWriter(r"F:\test4.xlsx")
# df_ZT.to_excel(writer,sheet_name="中通",index=False)
# df_JD.to_excel(writer,sheet_name="京东",index=False)

# df.to_excel('estest.xlsx',index=False)