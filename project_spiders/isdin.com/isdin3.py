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
    # 第一列
    # product_dict0 = {}
    # for title in product.select("div.item-0 div.title_1"):
    #     title1 = title.get_text()
    #     product_dict0["product0_title1"] = title1
    #     item_list.append(product_dict0)
    product0_title2 =product.select("div.item-0 div.title_2")[0].text
    # product0_title3 = product.select("div.item-0 div.title_3")[0].text
    # product0_vende = product.select("div.item-0 div.vende")[0].text
    # product0_btn = product.select("div.item-0 div.btn")[0].text
    # product0_img = product.select("div.item-0 div.img img")[0]["src"]
    # product0_url = "https://www.isdin.com" + product.select("div.item-0 a")[0]["href"]
    # product_dict0["product0_title2"] = product0_title2
    # product_dict0["product0_title3"] = product0_title3
    # product_dict0["product0_btn"]   = product0_btn
    # product_dict0["product0_img"]   = product0_img
    # product_dict0["product0_url"]   = product0_url
    # product_dict0["product0_vende"] = product0_vende
    # item_list.append(product_dict0)




    # # 第二列
    # product1_title1 = product.select("div.item-1 div.title_1")[0].text
    # product1_title2 = product.select("div.item-1 div.title_2")[0].text
    # product1_title3 = product.select("div.item-1 div.title_3")[0].text
    # product1_vende = product.select("div.item-1 div.vende")[0].text
    # product1_btn = product.select("div.item-1 div.btn")[0].text
    # product1_img = product.select("div.item-1 div.img img")[0]["src"]
    # product1_url = "https://www.isdin.com" + product.select("div.item-1 a")[0]["href"]
    # # 第三列
    # product2_title1 = product.select("div.item-2 div.title_1")[0].text
    # product2_title2 = product.select("div.item-2 div.title_2")[0].text
    # product2_title3 = product.select("div.item-2 div.title_3")[0].text
    # product2_vende = product.select("div.item-2 div.vende")[0].text
    # product2_btn = product.select("div.item-2 div.btn")[0].text
    # product2_img = product.select("div.item-2 div.img img")[0]["src"]
    # product2_url = "https://www.isdin.com" + product.select("div.item-2 a")[0]["href"]
    # 将所有信息放入字典
    # product_dict1 = {}
    # product_dict1["product1_title"] = product1_title1,product1_title2,product1_title3
    # product_dict1["product1_vende"] = product1_vende
    # product_dict1["product1_img"]   = product1_img
    # product_dict1["product1_url"]   = product1_url
    #
    # product_dict2 = {}
    # product_dict2["product2_title"] = product2_title1,product2_title2,product2_title3
    # product_dict2["product2_vende"] = product2_vende
    # product_dict2["product2_img"]   = product2_img
    # product_dict2["product2_url"]   = product2_url



    # item_list.append(product_dict1)
    # item_list.append(product_dict2)

# df = pd.DataFrame(item_list, columns=item_list[0].keys())
# df.to_excel('estest.xlsx',index=False)

    # print(product1_url)
    # print(product2_title2)
    # print(product2_title3)
    # print(product2_vende)
    # print(product2_btn)