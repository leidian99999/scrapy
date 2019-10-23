import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import time


headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer': 'https://www.meituri.com/a/22633/'
}

# html = requests.get(url,headers=headers).content
# soup = BeautifulSoup(html,'lxml')

#解析单个网页
def parse_html(url):
    html = requests.get(url,headers=headers).content
    soup = BeautifulSoup(html,'lxml')
    return soup

#提取页面链接总数以及封面标题
def page_num(url):
    soup = parse_html(url)
    title = soup.head.title.text
    pages = soup.find('div', {'id': 'pages'}).findAll('a', {'class': ''})
    num =  pages[len(pages)-1].text #获取页面链接总数
    return title,num

#拼接页面的各个链接
'''
单个相册中，各页面链接直接通过页面下方的a标签获取。当相册页面多于12个时，部分页码被隐藏，链接不能完全获取。
解决方法：获取页面总数，再拼接完成各页面链接，存入列表，留待使用。
'''
def pages_url_connect(url,num):
    url_list = []
    for i in range(1,int(num)+1):
        if i == 1:
            url_list.append(url)
        else:
            url_complete = url+str(i)+'.html'
            url_list.append(url_complete)
    return url_list

#提取图片标签
def img_html(soup):
    img_list = soup.find('div',{'class':'content'}).findAll('img')
    return img_list

#提取单个图片链接
def img_mess(img_list):
    for img in img_list:
        message = {}
        message['name'] = img.attrs["alt"]
        message['url'] = img.attrs["src"]
        yield message

# 下载图片

# if not os.path.exists(path):
#     os.mkdir(path)

def save_img(message,path):
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        response = requests.get(message.get('url'),headers=headers)
        if response.status_code == 200:
            file_path = '{0}/{1}.jpg'.format(path,message.get('name').replace('/',''))
            if not os.path.exists(file_path):
                with open(file_path,'wb')as f:
                    f.write(response.content)
                    #time.sleep(1)
                    print('download... ',message.get('name'))
            else:
                print("already download:",file_path)
    except requests.ConnectionError:
        print("fail to download")



def main2(url, path,index):
    url = 'https://www.meituri.com/a/9340/'
    path = "D:\\Python\\dataset\\spiders\\pics\\meituri\\test\\"

    title,num = page_num(url)
    title= title.replace('/','')    #防止文件名中有‘/’导致路径错误
    print('第{}套，开始抓取: '.format(index), title)
    path = path+'/'+title
    print('保存地址: ',path)
    url_list = pages_url_connect(url,num) #获取各个页面完整链接，返回一个列表
    for page_url in url_list:
        # print(page_url)
        i_html = parse_html(page_url)
        imgs = img_html(i_html)
        message = img_mess(imgs)

        for mess in message:
            save_img(mess,path)

    print('第{}套'.format(index), title,' 抓取完成！\n')
    time.sleep(1)

if __name__=='__main__':
    main2()
