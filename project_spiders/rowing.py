# 导入库
from bs4 import BeautifulSoup as bs
import requests

# 解析网页

#模拟浏览器发送请求
request = requests.get('http://www.worldrowing.com/events/2018-world-rowing-under-23-championships/u23-mens-eight/')
#bs实例化（网页源代码str,解析网页方法str）
soup = bs(request.text,'html.parser')
athlete_list = soup.select('tr.resultsDetails li')
item_list = []

for athlete in athlete_list:
    item = {}
    item["name"] = athlete.select('h4 a')[0].text
    item["position"] = athlete.select('p.yPadding')[0].text.strip()
    item["img_url"] = "http://www.worldrowing.com" + athlete.select("a img")[0]['src']
    detail_url = "http://www.worldrowing.com" + athlete.select("h4 a")[0]['href']
    response = requests.get(detail_url)
    soup = bs(response.text,"html.parser")
    item['sex'] = soup.select('div.dd')[0].text
    item['birthday'] = soup.select('div.dd')[1].text
    item['country'] = soup.select('h1.athleteInfoTitle span')[0].text
    item['detail_url'] = detail_url
    item_list.append(item)
    print(item)
import pandas as pd
# df = pd.DataFrame(item_list,columns=item_list[0].keys())
# df.to_excel('athleteRecord.xlsx',index=False)

print("*"*100)
print(item_list[0].keys())
