"""
@Author:lichunhui
@Time:   
@Description: 百度百科爬虫程序入口
"""
from scrapy import cmdline

cmdline.execute("scrapy crawl baiduSpider".split())

