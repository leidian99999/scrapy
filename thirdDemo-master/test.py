#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:xxx time:2019/6/14
import requests
from bs4 import BeautifulSoup

url = "https://s.taobao.com/search?q=小吃&s=44"

headers = {

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 't=a806a2d08c6783afd6c34ee8e33b3edd; thw=cn; cna=IXgqFYG/EGICAQ7Eapx4e76i; tracknick=%5Cu6211%5Cu7684%5Cu5973%5Cu795E%5Cu6709%5Cu70B9%5Cu6C61; _cc_=UtASsssmfA%3D%3D; tg=0; enc=r8hBVtnKxhtig2EPmjzsbqzxXKH8f4xEcHO3q%2FPT8rJPx7zN2zW54gr1CCZ5Sf5%2FAhteOFkT3OglvPSfDsdaqQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; miid=748249091544495874; cookie2=1c2ff52f09449be9bee87f5ca6d0a4dc; v=0; _tb_token_=e3b3baa3ee8ba; JSESSIONID=02FBAFED3B262824B107B3E8A81FBCC9; l=bBEy4xenv3xbvGVyBOCNZuI-iKQ9SIRA_uPRw2Jpi_5p46LsvobOkj0i6Fp6Vj5RsELB4VHBZd99-etki; isg=BKCgHrVf6eDu-FRf0DkKwm_Dca6yAdxBY6hswRqxaLtJFUA_wroeA5knrf0wojxL',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',

}

def get_page():
    req = requests.get(url=url, headers=headers)

    with open('taobaoindex.html', 'w', encoding='utf8')as fw:
        fw.write(req.text)

    print('ok')

# class="J_Ajax num icon-tag"


def parser_next_page():
    with open('taobaoindex.html', 'r', encoding='utf8')as fw:
        html = fw.read()

    print(html)

    soup = BeautifulSoup(html,'lxml')
    next = soup.find("pager")
    print(next)



# //s.taobao.com/search?q\u003d%E5%B0%8F%E5%90%83\u0026s\u003d44\u0026bcoffset\u003d0\u0026ntoffset\u003d0

parser_next_page()