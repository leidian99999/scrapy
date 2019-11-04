from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from lxml import etree

# 调用Chrome浏览器
browser = webdriver.Chrome()

# 1.
# html = etree.HTML(browser.page_source)
# html.xpath("")


# 2.

# 2.1 文本框输入 input type='text/password/email/number'
# try:
#     browser.get('https://www.baidu.com') # 打开网页
#     input_data_id = browser.find_element_by_id("kw")  # 定位元素，id是唯一的
#     # 输入查询关键词
#     input_data_id.send_keys('id定位')
#     # 点击回车
#     input_data_id.send_keys(Keys.ENTER)
#     # 等待加载
#     wait = WebDriverWait(browser,10)
#     # 等待5秒
#     time.sleep(5)
#     # 清空输入框
#     input_data_id.clear()
#     time.sleep(5)
#
#     # 关闭浏览器
#     browser.close()
# except:
#     pass

'''
a = browser.find_element_by_id('su') # id定位
# a = browser.find_element(By.ID,'su')
b = browser.find_element_by_class_name('su') # class属性名定位
# b = browser.find_element(By.CLASS_NAME,'su')
c = browser.find_element_by_name('email') # name属性名定位
# c = browser.find_element(By.NAME,'email')
d = browser.find_element_by_tag_name('div') # 标签名定位
# d = browser.find_element(By.TAG_NAME,'div')
e = browser.find_element_by_xpath('//div') # xpath定位
# e = browser.find_element(By.XPATH,'//div')
f = browser.find_element_by_css_selector('//div') # css定位
# f = browser.find_element(By.CSS_SELECTOR,'//div')

## 以上都是只获取第一个元素的，获取所有的是find_elements
'''

# 2.2 按钮 input type = 'submit'

# 2.3 checkbox(记住用户名密码) input type = 'checkbox'
try:
    browser.get('https://www.douban.com') # 打开网页
    remember = browser.find_element(By.NAME,"remember")  # 定位元素，id是唯一的
    remember.click()
    # 等待5秒
    # time.sleep(5)
    # # 清空输入框
    # remember.clear()
    # time.sleep(5)
    #
    # # 关闭浏览器
    # browser.close()
except:
    pass



# 2.4 select 下拉列表





# 1。如果只是想要解析网页中的数据，那么推荐将网页源代码扔给lxml来解析。因为lxml底层是用C语言，所以解析效率会更高。
# 2. 如果是想要对元素进行一些操作，比如给一个文本框输入值，或者是点击某个按钮，就必须是用selenium的找元素的方法。