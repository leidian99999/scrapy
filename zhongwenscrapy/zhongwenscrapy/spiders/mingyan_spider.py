import scrapy

class mingyan(scrapy.Spider): # 需要继承scrapy.Spider类

    name = "argsSpider" # 定义蜘蛛名

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag', None)  # 获取tag值，也就是爬取时传过来的参数
        if tag is not None:  # 判断是否存在tag，若存在，重新构造url
            url = url + 'tag/' + tag  # 构造url若tag=爱情，url= "http://lab.scrapyd.cn/tag/爱情"
        yield scrapy.Request(url, self.parse)  # 发送请求爬取参数内容
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
        mingyan1 = response.css('div.quote') # 提取首页所有名言，保存至变量mingyan1中

        for v in mingyan1: # 循环获取每一条名言里面的内容，作者，标签
            text = v.css(".text::text").extract_first() # 提取名言
            author = v.css(".author::text").extract_first() # 提取作者
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串

        # page = response.url.split("/")[-2] # 根据上面的连接提取分页，如：/page/1/,提取到的就是：1
        # filename = 'mingyan-%s.html' % page # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html

            filename = '%s-语录.txt' % author  # 爬取的内容存入文件，文件名为：作者-语录.txt
            with open(filename,'a+') as f: # python文件操作:追加写入内容
                # f.write(response.body) # response.body代表刚才下载的页面
                # self.log("保存文件：%s" % filename) # 打印日志
                f.write(text) # 写入名言内容
                f.write('\n') # 换行
                f.write('标签：' + tags) # 写入标签
                f.write("\n---------\n")
                f.close() # 关闭文件

        next_page = response.css("li.next a::attr(href)").extract_first() # css选择器提取下一页
        if next_page is not None: # 判断是否存在下一页
            '''
            如果是相对路径，如/page/1
            urljoin能转换为绝对路径
            '''
            next_page =response.urljoin(next_page)

            yield scrapy.Request(next_page,callback=self.parse)
            '''
            scrapy.Request()
            参数1：继续爬去next_page
            参数2：把链接交回给parse函数，效果同在下面再写一个parse函数
            '''