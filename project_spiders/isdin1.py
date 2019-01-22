def getHousesDetails(url):
  from bs4 import BeautifulSoup
  import requests
  request = requests.get(url)
  request.encoding = 'utf-8'
  soup = BeautifulSoup(request.text,'lxml')
  houses = soup.select('.lpList')
  housesDetails = []
  for house in houses:
    #获取楼盘名字
    houseName = house.select('.title h2 a')[0].text
    #获取楼盘地址
    address = house.select('.lpTxt div')[1].select('p')[1].text.strip('楼盘地址： 查看地图')
    if(len(address) >= 16):
        houseDetailHref = house.select('.title h2 a')[0]['href']
        request = requests.get(houseDetailHref)
        request.encoding = 'utf-8'
        soup = BeautifulSoup(request.text,'lxml')
        address = soup.select('.toplpMsg ul li div i')[0].text.strip('楼盘地址：')
    #获取楼盘开盘时间
    openTime = house.select('.lpTxt div')[1].select('p')[3].text.strip('开盘时间：')
    #获取楼盘价格
    price = house.select('.price p b')[0].text
    #获取楼盘销售状态
    def numberToString(number):
      switcher = {
          1: "在售",
          3: "尾盘",
          5: "未售",
          15: "售罄"
      }
      return switcher.get(number,'未知')
    saleStatusImg = house.select('.title p img')[0]['src']
    saleStatusId = int(saleStatusImg.lstrip('/public/images/state_').rstrip('.jpg'))
    saleStatus = numberToString(saleStatusId)
    #将所有楼盘信息做成楼盘信息字典
    houseDetails = {}
    houseDetails['houseName'] = houseName
    houseDetails['address'] = address
    houseDetails['openTime'] = openTime
    houseDetails['price'] = price
    houseDetails['saleStatus'] = saleStatus
    housesDetails.append(houseDetails)
  return housesDetails

def getAllHousesDetails():
  maxPageNumber = 54
  urlBefore = 'http://house.lanfw.com/xm/search-y{}'
  allHousesDetails = []
  for i in range(1,maxPageNumber+1):
    url = urlBefore.format(i)
    allHousesDetails.extend(getHousesDetails(url))
  import pandas
  dataframe = pandas.DataFrame(allHousesDetails)
  return dataframe

if __name__ == '__main__':
  allHousesDetails = getAllHousesDetails()
  allHousesDetails.to_excel('houseDetails2.xlsx')