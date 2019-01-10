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
# 不完整的html


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml') # 初始化：将html传给BeautifulSoup,并使用lxml解析器，
print(soup.prettify()) # 把要解析的字符串以标准的缩进格式输出
print("*"*20)
print(soup.title.string) # 输出html中Title节点的文本内容