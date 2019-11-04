from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from lxml import etree


browser = webdriver.Firefox()
wait=WebDriverWait(browser,10)

def get_html_one(keyword):
    browser.get("https://www.taobao.com/")
    time.sleep(0.5)
    #输入需要购买的物品
    browser.find_element_by_id('q').send_keys(keyword)
    #按下搜索按钮
    browser.find_element_by_class_name('btn-search').click()
    #扫码登录
    time.sleep(30)
    #找到页面元素：一共多少页
    # pages=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))).text
    pages = 1
    #返回一共页数
    return pages


def next_page(page_num):
    try:
        #找到输入页码的地方
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
        #先清除原来的，后输入
        input.clear()
        input.send_keys(page_num)
        #submit.click()
        time.sleep(1)
        #直接敲击回车
        ActionChains(browser).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        #确定是否找到对应的页码
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_num)))
    except Exception as ret:
        print(ret)
        #如有问题则再次调用该函数
        next_page(page_num)

def get_information_one():
    #获取网页源代码
    html = etree.HTML(browser.page_source)
    #
    #找到每一个宝贝并循环
    list = html.xpath("//div[@class='items']")

    for node in list:
        baobei = {}
        baobei["url"] = node.xpath("./div[@data-category='auctions']//a[@class='J_ClickStat']/@href")
        yield baobei
        #     {
        #     # 'price':item('.price.g_price strong').text(),
        #     # 'pay_people':item('.deal-cnt').text().split('人')[0],
        #     # 'title':item('.J_ClickStat').text(),
        #     # 'store_name':item('.shopname').text(),
        #     # 'location':item('.location').text(),
        #     'url':item("./div[@data-category='auctions']//a[@class='J_ClickStat']/@href")
        # }

def get2csv(csv,idot):
    csv=csv.append(idot,ignore_index=True)
    return csv

def main():
    keywords = "MartiDERM熬夜急救安瓶精华"
    pages=get_html_one(keywords)

    csv = DataFrame([],
                    columns=['url'])

    for item in get_information_one():
        csv=get2csv(csv,item)

    for i in range(2,pages+1):
        next_page(i)
        print(i)
        for item in get_information_one():
           csv=get2csv(csv,item)
    print(pages)
    csv.to_csv("D:/GitHub/scrapy/selenium_TB/" + keywords +".csv",
               header=True,index=False,encoding='utf-8-sig')

if __name__ == '__main__':
    main()