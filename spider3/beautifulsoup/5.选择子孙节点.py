html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.p.contents) # contents只得到结果的直接子节点的列表，无孙节点


# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.children)
# for i, child in enumerate(soup.p.children): # 遍历得到子节点
#     print(i, child)


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.p.descendants) # 返回生成器类型，遂用for
for i, child in enumerate(soup.p.descendants): # 遍历得到全部子孙节点
    print(i, child)