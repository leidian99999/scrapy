html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.title) #打印title
# print(type(soup.title)) # 打印title类型
# print(soup.title.string) # 打印title文本
# print(soup.head) # 打印head
# print(soup.p) # 打印P标签(第一个，后面的没有找到)
#
# print(soup.title.name) # 获取节点名称

# 获取属性
# print(soup.p.attrs) # 获取所有属性
# print(soup.p.attrs['name']) # 获取name属性值

# 简写
# print(soup.p['name'])
# # print(soup.p['class'])

# 获取内容
print(soup.p.string)