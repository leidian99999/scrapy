from bs4 import BeautifulSoup
import requests
import pandas as pd



size_url = "https://www.isdin.com/producto/fotoprotector-isdin"
request = requests.get(size_url)
request.encoding = 'utf-8'
soup = BeautifulSoup(request.content,'lxml')

product_list = soup.select("div.search-results")

item_list = []

item_title1 = soup.select('div.title_1')
item_title2 = soup.select('div.title_2')
item_title3 = soup.select('div.title_3')
item_vende = soup.select('div.vende')
item_img = soup.select('div.img')



print("*"*100)

print("*"*100)