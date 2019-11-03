#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:xxx time:2019/6/14

from scrapy import cmdline
cmdline.execute("scrapy crawl taobao -o info.csv -t csv".split())