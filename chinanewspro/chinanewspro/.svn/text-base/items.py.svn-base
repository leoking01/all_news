# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinanewsproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    pass
    title=scrapy.Field()##新闻标题
    link=scrapy.Field()##新闻链接
    response_news=scrapy.Field()##新闻回应，抓取值.


    time_release=scrapy.Field()##新闻发布时间
    #type_news=scrapy.Field()##新闻类型，抓取值。网站所给的分类。
    #from_news=scrapy.Field()##新闻出处。通常为新闻频道。
    abstract=scrapy.Field()##摘要
    keywords=scrapy.Field()##关键词
    mainbody=scrapy.Field()##正文
    
    ##标记
    hash=scrapy.Field()##标题的hash值，处理值
    manufacturer=scrapy.Field()##文件在本系统中的出处(哪个spider.)，处理标记



