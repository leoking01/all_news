# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.utils.response import get_base_url

from urlparse import urljoin,urlparse,urlunparse

from posixpath import normpath
import os,hashlib,sys
import datetime,time

from chinanewspro.items import ChinanewsproItem

sys.stdout=open('log.txt','w')

class QqSpider(CrawlSpider):
    name = "qq_test"
    allowed_domains = ['news.qq.com']
    start_urls = (
        'http://news.qq.com/',
    )

    rules=(
        ##一：新闻中心_要闻##   http://news.qq.com/
        Rule(LinkExtractor(allow=('.', ) ) ,callback='parse_base_item', follow='true'),
        ##二：新闻中心_国内新闻##   http://news.qq.com/china_index.shtml
        Rule(LinkExtractor(allow=('china_index.shtml',) ) ,callback='parse_china_item'),
        ##三：新闻中心_社会新闻##   http://news.qq.com/society_index.shtml
        Rule(LinkExtractor(allow=('society_index.shtml',) ) ,callback='parse_society_item'),
    )
   
    
#########################################      一：新闻中心_要闻      ##################################################
    ######## 一：新闻中心_要闻 #######  http://news.qq.com/
    def parse_base_item(self,response):
        ###  (1)新闻中心_要闻
        print '=====parse_base_item:=====response:',response
        base_url = get_base_url(response)
        sel_a=response.xpath('//*[@id="mainTabPanel"] | //*[@id=\'moreNews\']')
        sel_b=sel_a.xpath('.//div[@class="Q-tpWrap"]')
        id=0       
        ##爬取主页新闻标题列表
        for site in response.xpath('//em[@class]'):
            id+=1
##.//*[@id='mainTabPanel']/div[18]/div/em/span/span/a
##.//*[@id='mainTabPanel']/div[23]/div/em/span/span/a
##.//*[@id='moreNews']    /div[6] /div/em/span/span/a
            title=site.xpath('span/span/a/text() ' ).extract()
            link=site.xpath('span/span/a/@href' ).extract()
            response_news=site.xpath('../p[@class]/text() ').extract()

            
            ##show contents
            item=ChinanewsproItem(title=title,link=link,\
                    response_news=response_news,\
                    manufacturer='qq_center_yaowen')

            ##正文抓取
            print 'main body loop:'
            print 'response = ',response
            link=site.xpath('span/span/a/@href' ).extract()
            url_n= ''.join(link)
            url_new=urljoin(base_url,url_n )
            yield scrapy.Request(url_new, callback=self.parse_body_center_yaowen,meta={'item':item})

    ##新闻中心  要闻  正文
    def parse_body_center_yaowen(self,response):
        print 'parse_body_center_yaowen : done '
        print 'response: ',response
        print '####################### '
        item=response.meta('item')
        #文件路径
        old_path='/data/news_data/qq_news/'
        t=time.localtime()
        t=time.strftime('%Y-%m-%d',t)
        new_path=os.path.join(old_path,t)
        if not os.path.isdir(new_path):
            os.mkdir(new_path)
        
        #新文件名
        t=time.localtime()
        tt=time.strftime('%Y_%m_%d_%X',t).replace(':','_')
        file=new_path+'/'+tt
        fp=open(file,'w')
        str='test word. \n'####test##ok.
        fp.write(str)
        fp.close()
        
            ##item: hash
            #title_a=''.join(title)
            #sha1obj = hashlib.sha1()
            #sha1obj.update(title_a)
            #hash = sha1obj.hexdigest()
            #print 'spider: hash: ',hash
        return item 


#########################################      1.5 新闻中心_国内      ##################################################
            #http://news.qq.com/top_index.shtml
            #.//*[@id='listZone']/div[5]/div/em/a
            #.//*[@id='listZone']/div[11]/div/em/a
            #.//*[@id='listZone']/div[3]/div/em/a

#########################################      二：新闻中心_国内      ##################################################
    ########二：新闻中心_国内#######
    def parse_china_item(self,response):
        print '=====parse_china_item:=====response:',response
        sel_a=response.xpath('.//div[@id="news"]')
        sel_b=sel_a.xpath('.//div[@class="Q-tpWrap"]')
        id=0        
        for site in sel_b:
            id+=1
            title=site.xpath('em[@class]/a/text() ' ).extract()
            link=site.xpath('em[@class]/a/@href' ).extract()
            #link="http://news.qq.com/"+str(link)
            time_release=site.xpath('em[@class]/a/@href ').extract()
            response_news=site.xpath('p[@class]/text() ').extract()
            type_news=site.xpath('em[@class]/a/text() ' ).extract()

            ##item: hash
            title_a=''.join(title)
            sha1obj = hashlib.sha1()
            sha1obj.update(title_a)
            hash = sha1obj.hexdigest()
            print 'spider: hash: ',hash

            item=ChinanewsproItem(title=title,link=link,\
                    time_release=time_release,\
                    response_news=response_news,\
                    type_news=type_news,hash=hash,manufacturer='qq_center_china')


            print 'id : ',id
            print 'response :  ',response

            if not len(item['response_news'])==0:
                print 'response_news:',item['response_news'][0].encode('utf-8')
            else:
                print 'response_news:','response_news'

            if not len(item['title'])==0:
                print 'title:',item['title'][0].encode('utf-8')
            else:
                print 'title:','null'
            yield item


#########################################      三：新闻中心_社会      ##################################################
    ########三：新闻中心_社会#######
    def parse_society_item(self,response):
        print '=====parse_society_item:=====response:',response
        sel_a=response.xpath('.//div[@id="news"]')
        sel_b=sel_a.xpath('.//div[@class="Q-tpWrap"]')
        id=0        
        for site in sel_b:
            id+=1
            title=site.xpath('em[@class]/a/text()' ).extract()
            link=site.xpath('em[@class]/a/@href' ).extract()
            time_release=site.xpath('em[@class]/a/@href ').extract()
            response_news=site.xpath('p[@class]/text() ').extract()
            type_news=site.xpath('em[@class]/a/text()' ).extract()

            ##item: hash
            title_a=''.join(title)
            sha1obj = hashlib.sha1()
            sha1obj.update(title_a)
            hash = sha1obj.hexdigest()
            print 'spider: hash: ',hash

            item=ChinanewsproItem(title=title,link=link,time_release=time_release,response_news=response_news,type_news=type_news,hash=hash,manufacturer='qq_center_china')


            print 'id : ',id
            print 'response :  ',response

            if not len(item['response_news'])==0:
                print 'response_news:',item['response_news'][0].encode('utf-8')
            else:
                print 'response_news:','response_news'

            if not len(item['title'])==0:
                print 'title:',item['title'][0].encode('utf-8')
            else:
                print 'title:','null'

            yield item


#############################################################################

        ########四：滚动新闻：另做。以下不工作。#######
    def parse_roll_item(self,response):
        print '=====parse_roll_item:=====response:',response
        sel_a=response.xpath('//div[@class="main"]/div[@class="mainCon"]/div[@class="list c"]')
        sel_b=sel_a.xpath('.//ul')
        sel_b=sel_a.xpath('.//li')
        id=0        
        for site in sel_b:
            id+=1
            title=site.xpath('a/text()' ).extract()
            link=site.xpath('a/@href' ).extract()
            time_release=site.xpath('a/@href ').extract()
            type_news=site.xpath('span[@class="t-tit"]/text()' ).extract()
            #response_news=site.xpath('p[@class]/text() ').extract()

            item=ChinanewsproItem(title=title,link=link,time_release=time_release,type_news=type_news)
            print 'id : ',id
            print 'response :  ',response
            print 'response_news:',item['response_news'][0].encode('utf-8')
            if not len(item['title'])==0:
                print 'title:',item['title'][0].encode('utf-8')
            else:
                print 'title:','null'
            yield ChinanewsproItem(title=title,link=link,time_release=time_release,type_news=type_news)


