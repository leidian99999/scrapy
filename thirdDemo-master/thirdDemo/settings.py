# -*- coding: utf-8 -*-

# Scrapy settings for thirdDemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'thirdDemo'

SPIDER_MODULES = ['thirdDemo.spiders']
NEWSPIDER_MODULE = 'thirdDemo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {

   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
   'accept-encoding': 'gzip, deflate, br',
   'accept-language': 'zh-CN,zh;q=0.9',
   'cache-control': 'max-age=0',
   'cookie': 't=a806a2d08c6783afd6c34ee8e33b3edd; thw=cn; cna=IXgqFYG/EGICAQ7Eapx4e76i; tracknick=%5Cu6211%5Cu7684%5Cu5973%5Cu795E%5Cu6709%5Cu70B9%5Cu6C61; _cc_=UtASsssmfA%3D%3D; tg=0; enc=r8hBVtnKxhtig2EPmjzsbqzxXKH8f4xEcHO3q%2FPT8rJPx7zN2zW54gr1CCZ5Sf5%2FAhteOFkT3OglvPSfDsdaqQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; miid=748249091544495874; cookie2=1c2ff52f09449be9bee87f5ca6d0a4dc; v=0; _tb_token_=e3b3baa3ee8ba; JSESSIONID=02FBAFED3B262824B107B3E8A81FBCC9; l=bBEy4xenv3xbvGVyBOCNZuI-iKQ9SIRA_uPRw2Jpi_5p46LsvobOkj0i6Fp6Vj5RsELB4VHBZd99-etki; isg=BKCgHrVf6eDu-FRf0DkKwm_Dca6yAdxBY6hswRqxaLtJFUA_wroeA5knrf0wojxL',
   'upgrade-insecure-requests': '1',
   'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',

}

detail_headers = {

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 't=a806a2d08c6783afd6c34ee8e33b3edd; thw=cn; cna=IXgqFYG/EGICAQ7Eapx4e76i; tracknick=%5Cu6211%5Cu7684%5Cu5973%5Cu795E%5Cu6709%5Cu70B9%5Cu6C61; _cc_=UtASsssmfA%3D%3D; tg=0; enc=r8hBVtnKxhtig2EPmjzsbqzxXKH8f4xEcHO3q%2FPT8rJPx7zN2zW54gr1CCZ5Sf5%2FAhteOFkT3OglvPSfDsdaqQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; miid=748249091544495874; cookie2=1c2ff52f09449be9bee87f5ca6d0a4dc; v=0; _tb_token_=e3b3baa3ee8ba; JSESSIONID=02FBAFED3B262824B107B3E8A81FBCC9; l=bBEy4xenv3xbvGVyBOCNZuI-iKQ9SIRA_uPRw2Jpi_5p46LsvobOkj0i6Fp6Vj5RsELB4VHBZd99-etki; isg=BKCgHrVf6eDu-FRf0DkKwm_Dca6yAdxBY6hswRqxaLtJFUA_wroeA5knrf0wojxL',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',

}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'thirdDemo.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'thirdDemo.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'thirdDemo.pipelines.ThirddemoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
