html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading')) # class=panel下的 class=panel-heading
# print(soup.select('ul li')) # 选择所有ul下的所有li节点,方法一
# print(soup.select('#list-2 .element')) # 选择所有id=list-2下的class=element节点
# print(type(soup.select('ul')[0]))


# 遍历所有ul节点中的li节点,方法二:推荐这种方法获取元素
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.select('ul'): # 选择所有ul节点
#     print(ul.select('li'))

# 获取每个ul节点的id属性
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.select('ul'):
#     print(ul['id'])
#     # print(ul.attrs['id'])

# 获取文本,二者方法完全一样
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)