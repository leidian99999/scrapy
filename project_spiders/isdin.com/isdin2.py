from bs4 import BeautifulSoup
import requests

size_url = "https://www.isdin.com/producto"
request = requests.get(size_url)
request.encoding = 'utf-8'
soup = BeautifulSoup(request.content,'lxml')

brand_list = soup.select('ul.son-menu-marca')
item_list = []
for brand in brand_list:
    # 获取品牌名
    name = brand.select("li a")[0].text
    # 获取品牌链接
    brand_url_list = "https://www.isdin.com" + brand.select("li a")[0]["href"]
    request_brand_list = requests.get(brand_url_list)
    request_brand_list.encoding = 'utf-8'
    soup_brand_list = BeautifulSoup(request_brand_list.text, 'lxml')
    product_list = soup.select('div.search-results')[0]

    print(product_list)


    # for li in brand.find_all(name='li'):
    #     # name = li.string
    #     brand_url = li.select("a")["href"]
    #     print(brand_url)
    # brand_url = brand.find_all("a")
    # print(brand_url)

# print(brand_list)
# print(len(brand_list))