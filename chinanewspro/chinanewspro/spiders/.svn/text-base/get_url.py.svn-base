# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

import sys,os,hashlib

from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlunparse
from posixpath import normpath
from scrapy.utils.response import get_base_url

import file_check_function
from chinanewspro.items import ChinanewsproItem

import time

sys.stdout=open('log.txt','w')

   
   
class ChinanewsSpider(scrapy.Spider):
    zhuyaomeiti="""
    #新浪新闻
    #凤凰资讯
    #腾讯新闻
    #新华网
    #CCTV新闻
    #搜狐新闻
    #环球网
    #参考消息
    #网易新闻
    #人民网
    #联合早报
    #中国新闻网
    #南方网
    #中国广播网
    #百度新闻搜索
    #中国政府网
    #中国军网
    #中华网
    #央广网
    #国际在线
    #大公网
    #msn中文网
    #星岛环球网
    #中国青年网
    #宣讲家
    """
   
    name = "gu"
    allowed_domains = []
    start_urls = (
        ##新浪网
        ##搜狐
        ##腾讯网
        'http://www.qq.com/',
        #网易
        ##凤凰网
        #新华
        #人民
        ##中国新闻网
        'http://www.chinanews.com/',
        #央视新闻
        #环球网
        #百度新闻
        #参考消息
        #中华网
        #联合早报
        #南方周末
        #新闻大全

    )

   
   
    def parse(self,response):
        print '=====parse_surface_item:=====response:',response
        sel_a=response.xpath('//div[contains(@id,"newsContent")]')
        sel_b=sel_a.xpath('.//ul')
        sel_c=sel_b.xpath('.//li')
        id=0        
        base_url = get_base_url(response)
        for site in sel_c:
            id+=1
            
            ##item: ...
            title=site.xpath('a/text()' ).extract()
            if len(title)!=0:
                link=site.xpath('a/@href' ).extract()
                response_news=['']

                item=ChinanewsproItem(title=title,link=link,response_news=response_news,\
                    manufacturer='surface')

                url_m= (str(link))[3:-2]
                #url_m= ''.join(link)
                url_new=urljoin(base_url,url_m )
                yield scrapy.Request(url_new, callback=self.parse_body,meta={'item':item})
   
   
   
   
    ##正文抓取函数
    def parse_body(self,response):
        print 'done'
        print 'parse_body: create dir-file,write in...'
        print 'parse_body: response: ',response
        item=response.meta['item']
   
        #建立文件路径
        old_path='/data/news_data/get_urls/'
        path_reco=os.path.exists(old_path)
        if path_reco==1:
            pass
        else:
            os.mkdir(old_path)
        t=time.localtime()
        t=time.strftime('%Y_%m_%d',t)
        new_path=os.path.join(old_path,t)
        if not os.path.isdir(new_path):
            os.mkdir(new_path)
    
    
        #建立文件名
        file=''
        hash=0
        title=response.xpath('//*[@id=\'C-Main-Article-QQ\']/div[1]/h1/text()').extract()
        print 'parse_body: title: ',''.join(title).encode('utf-8')
        if len(title)!=0:
            title_a=''.join(title[0]).encode('utf-8')
            sha1obj = hashlib.sha1()
            sha1obj.update(title_a)
            hash = sha1obj.hexdigest()
            print 'hash: ',hash
            file=new_path+'/'+hash##hash 值作为文件名
            item['hash']=[hash]

            ##开始写一个文本
            path='/data/news_data/'
            ##file_check_function.file_check: 检查文件在既有文件夹下是否已经存在.如果已经存在,还要判断其是否异常。
            ##返回值 1:存在且正常.  2:不存在或者异常.
            pl=file_check_function.file_check(path,hash)
            if pl==0:
                ##打开文件
                print '文件写入开始。hash: ',hash
                fp=open(file,'w')
        
                ##抓取、写入正文标题
                ##获取标题、取hash值
                title=response.xpath('//*[@id=\'C-Main-Article-QQ\']/div[1]/h1/text()').extract()
                print 'title: ',''.join(title[0]).encode('utf-8')
                ##写入标题
                fp.write( 'title:\n' )
                #fp.write( str( title[0].encode('utf-8') ) )
                fp.write( ''.join(title[0]).encode('utf-8') ) 
                fp.write( '\n' )
        
                ##获取新闻发布时间、写入发布时间
                time_release_t=response.xpath('//*[@id=\'C-Main-Article-QQ\']/div[1]/div[1]/div[1]/span[@class="article-time"]/text()  |  //*[@id="time_source"]/span/text()').extract()
                item['time_release']= [  ''.join(time_release_t).encode('utf-8') ]
                if len(time_release_t)==0:
                    item['time_release']=['']
                time_release= ''.join(time_release_t).encode('utf-8')
                print 'parse_body: time_release: ',time_release
                fp.write( 'time_release:\n' )
                fp.write( time_release )
                fp.write('\n')
        
                ##获取摘要、写入摘要 
                abstract=response.xpath('//*[@id=\'Cnt-Main-Article-QQ\']/p[1]/text()').extract()
                print 'parse_body: abstract: ',''.join(abstract).encode('utf-8')##abstract 是有可能为空的,故不能给定索引.
                item['abstract']=abstract
                fp.write( 'abstract:\n' )
                fp.write( ''.join(abstract ).encode('utf-8') )
                fp.write('\n')
        
                ##抓取正文
                bodys_a=response.xpath('//div[@id=\'Cnt-Main-Article-QQ\']')
                bodys_b=bodys_a.xpath('.//p')
                ##写入正文
                fp.write('main_body: \n')
                print 'main_body: '
                fp.write('\n')
                for bod in bodys_b:
                    main_body=bod.xpath('text()').extract()
                    if len(main_body)!=0:
                        print ''.join(main_body[0]).encode('utf-8')
                        ##写入正文各段
                        fp.write( ''.join( main_body[0]).encode('utf-8')  )
                        fp.write('\n')
    
                ##关闭文件
                fp.close()
                print 'finish.'
                return item
    
            else:
                print 'pl: ',pl
                print '由于文件已经存在.无操作。'
    
        else:
            item['time_release']=['']
            item['hash']=['']
            print '标题为空。不操作。'
        print '\n\n'
    
    
