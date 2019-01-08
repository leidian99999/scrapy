import scrapy

class mingyan(scrapy.Spider): # 需要继承scrapy.Spider类

    name = "itemspider" # 定义蜘蛛名

# 初始连接写法一
    # def start_requests(self): # 由此方法通过下面链接爬取页面
    #
    #     # 定义爬取链接
    #     urls = [
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse) # 爬取到的页面如何处理？提交给parse方法处理

    start_urls = [  # 另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn',
    ]

    #  如果是简写初始url，此方法名必须为：parse
    def parse(self, response):
        mingyan1 = response.css('div.quote')[0]

        text = mingyan1.css(".text::text").extract()[0]
        author = mingyan1.css(".author::text").extract()[0]
        tags = mingyan1.css('.tags .tag::text').extract()  # 提取标签
        tags = ','.join(tags)  # 数组转换为字符串

        # page = response.url.split("/")[-2] # 根据上面的连接提取分页，如：/page/1/,提取到的就是：1
        # filename = 'mingyan-%s.html' % page # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html

        filename = '%s-语录.txt' % author  # 爬取的内容存入文件，文件名为：作者-语录.txt
        with open(filename,'a+') as f: # 追加写入文件
            # f.write(response.body) # response.body代表刚才下载的页面
            f.write(text) # 写入名言内容
            f.write("\n") # 换行
            f.write("标签：" + tags) # 写入标签
            f.close() # 关闭文件操作
            # self.log("保存文件：%s" % filename) # 打印日志