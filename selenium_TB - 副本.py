from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from numpy import random as nr
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

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
    time.sleep(20)
    #找到页面元素：一共多少页
    # pages=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))).text
    pages = "1"
    #返回一共页数
    return int(re.search('\d+',pages).group())


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
    doc=pq(browser.page_source)
    #找到每一个宝贝并循环
    lis=doc('.item.J_MouserOnverReq').items()
    for item in lis:
        # if item('.J_ClickStat').attr('href').startswith('https'):
        #     get_child_information = get_child(item('.J_ClickStat').attr('href'))
        # else:
        #     get_child_information = get_child(r'https:'+item('.J_ClickStat').attr('href'))
        yield {
            'price':item('.price.g_price strong').text(),
            'pay_people':item('.deal-cnt').text().split('人')[0],
            'title':item('.J_ClickStat').text(),
            'store_name':item('.shopname').text(),
            'location':item('.location').text(),
            
            # 'True_price':get_child_information[0],
            # 'comment_num':get_child_information[1],
            # 'people_call':get_child_information[2],
            # 'append_comment':get_child_information[3]
        }
#
# def get_child(url):
#     w_c = webdriver.Firefox()
#     w_c.get(url)
#     time.sleep(0.2)
#     w_c.find_element_by_id('sufei-dialog-close').click()
#     time.sleep(10)
#     doc = pq(w_c.page_source)
#     a = [doc('.tm-price').text(), doc('#J_ItemRates .tm-indcon .tm-count').text(), doc('#J_CollectCount').text()]
#     w_c.find_element_by_css_selector('#J_ItemRates .tm-indcon .tm-count').click()
#     time.sleep(1)
#     try:
#         try:
#             all=w_c.find_elements_by_css_selector('.tm-rate-append .tm-rate-content div')
#             mystr=''
#             for i in all:
#                 mystr=mystr+i.text+'\n'
#             a.append(mystr)
#             time.sleep(5)
#         except Exception:
#             a.append('fail')
#         w_c.close()
#         return a
#     except Exception:
#         w_c.close()
#         return[0,0,0,0]
def get2csv(csv,idot):
    csv=csv.append(idot,ignore_index=True)
    return csv

def main():
    pages=get_html_one("Martiderm玻尿酸补水保湿面膜")
    # pages = 1
    csv = DataFrame([], columns=['price', 'pay_people', 'title', 'store_name', 'location'])
    for item in get_information_one():
        csv=get2csv(csv,item)
    for i in range(2,pages+1):
        next_page(i)
        print(i)
        for item in get_information_one():
           csv=get2csv(csv,item)

    csv.to_csv(r"D:\GitHub\scrapy\selenium_TB\Martiderm玻尿酸补水保湿面膜.csv",header=True,index=False,encoding='utf-8-sig')

if __name__ == '__main__':
    main()