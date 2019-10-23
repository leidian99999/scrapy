# coding=utf-8
import requests
from bs4 import BeautifulSoup


def imgurl(url):
    res = requests.get(url)  # url为a标签的helf链接，即为图片封面的图片
    soup = BeautifulSoup(res.text, 'html.parser')  # 使用BeautifulSoup来解析我们获取到的网页
    page = int(soup.select('.pagenavi span')[-2].text)  # 获取总页数，-2为去掉上下页
    # a = soup.select('.main-image a')[0]  # 获取当前图片链接
    # src = a.select('img')[0].get('src')
    src = soup.select('.main-image a img')[0].get('src')  # 获取图片链接
    meiziid = src[-9:-6]  # 切片将src的倒数的字符串做名字
    print('开始下载妹子:', format(meiziid))  # 输出窗口提示下载
    for i in range(1, page + 1):
        i = '%02d' % i
        img = src.replace('01.jpg', str(i) + '.jpg')  # replace()替换页数
        #  添加headers模拟浏览器工作 反反爬
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Referer': 'http://www.mzitu.com'
        }
        response = requests.get(img, headers=headers)

        f = open('D:\\666\\' + meiziid + '%s.jpg' % i, 'wb')  # 放在D:\666\目录下
        f.write(response.content)
        f.close()
        print('===> %s 完成 ' % (meiziid + i))
    print(' %s 已下载\n' % meiziid)


def imgpage(page=''):
    res = requests.get('http://www.mzitu.com/page/' + page)
    soup = BeautifulSoup(res.text, 'html.parser')  # 解析页面
    href = soup.select('#pins a')  # 筛选

    list = set([i.get('href') for i in href])  # 遍历获取筛选后的href链接并用set()去掉重复的链接
    [imgurl(i) for i in list]  # 遍历下载


result = input('下载哪一页：')
imgpage(result)
