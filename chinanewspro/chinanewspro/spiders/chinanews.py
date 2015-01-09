# -*- coding: utf-8 -*-
"""
采用多条件判断的方式提取新闻标题和正文。
标题和链接：
1，链接长度频度最高。或者比较高。(链接长度统计----链接--标题搜集)

正文：
2. 正文字数不低于100字。(正文字数统计----正文-标题爬取)

其他：
3. 链接的层次只能是一层。(链接层数控制: 1)
4. 
"""
import sys,os,hashlib
import time

from twisted.enterprise import adbapi
import MySQLdb.cursors
import MySQLdb
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy import log

import scrapy
from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.utils.response import get_base_url

from urlparse import urljoin,urlparse,urlunparse
from posixpath import normpath

from chinanewspro.items import ChinanewsproItem

from file_check_function  import file_check
import file_check_function
import urls

from chinanews_functions import  list_2_dict,bianli,dict_max,dict_min,dict_modif,evaluation,dir_creat,list_evaluation

sys.stdout=open('log.txt','w')
   

class ChinanewsSpider(scrapy.Spider):
    name = "all_news"
    allowed_domains = []
    start_urls = urls.all_urls 
   
    def parse(self,response):
        print '=====parse_surface_item:=====response:',response

        base_url = get_base_url(response)


        ##################  链接长度统计 #############################
        hrefs=response.xpath('//a/@href').extract()
        ##找出出现最多的那个长度值，以及长度的最长值
        lengths=[]
        for href in hrefs:
            href = urljoin(base_url,href )
            length = len( ''.join(href) )
            lengths.append(length)##链接长度列表
            ##print len(''.join(href) ),'->',href

        print 'lengths: ',lengths


        ##可用链接长度值分为三个阶段：均值分别为：leng_golden，leng_silver，leng_copper
        ##根据 链接长度列表 得到 长度--频度 字典{长度：频率}
        length_frequency = list_2_dict(lengths)  ####  原始字典
        #lamda: 控制系数.控制系数越小，则越松弛。越大则越严格.
        lamda = 0.8
        evalu_length_freq = evaluation(length_frequency , lamda )##评估字典
        print 'evalu_length_freq : ',evalu_length_freq

        list_evalu = evalu_length_freq.keys()##可用键
        print 'list_evalu : ',list_evalu
        print 'oh, here.'


        #######################  标题-链接搜集   ###############################
        print 'crawl start.'
        sites = response.xpath('//a')
        for site in sites :
            ##item: ...
            href = site.xpath('./@href').extract()
            href = urljoin(base_url,''.join(href)  )
            length = len( ''.join(href) )
            manufacturer = ''.join(base_url)[0:30]
            if length in list_evalu :
                title = site.xpath('./text() ' ).extract()
                if len(title)!=0 and len( ''.join(title) )>4 :
                    response_news=['']##不考虑

                    item=ChinanewsproItem(title=title,link=href,response_news=response_news,\
                        manufacturer = manufacturer)
                    yield scrapy.Request(href, callback=self.parse_body,meta={'item':item})
   
   
    ##正文抓取函数
    def parse_body(self,response):
        print '进入正文抓取部分'
        print 'parse_body: create dir-file,write in...'
        print 'parse_body: response: ',response
        item=response.meta['item']
   
        #建立文件保存路径
        ##一级路径: 域名
        basic_path = '/data/news_data/all_news/'
        manu = ''.join(item['manufacturer'])[7:].replace("/",'_')
        manu = manu.replace('?','_')
        path_order_one = dir_creat(basic_path,manu  )

        ##二级路径：日期
        t = time.localtime()
        date_name = time.strftime('%Y_%m_%d',t)
        path_order_two = dir_creat(path_order_one,date_name )
        new_path = path_order_two 
  
        ##正文统计分析
        ##bodys = response.xpath().extract

        ##正文-标题搜集

        #建立文件名
        file=''
        hash=0
        bodys = response.xpath('//body')

        title = bodys.xpath('.//h1/text()  |  ../*[contains(@*,\'titl\')]').extract()
        time_release = bodys.xpath(' .//*[ contains(@*,\'time\') ]/text() ' ).extract()
        time_release = list_evaluation(time_release)
        ##print 'parse_body: title: ',''.join(title).encode('utf-8')
        if len(title)!=0:
            title_a=''.join(title[0]).encode('utf-8')
            sha1obj = hashlib.sha1()
            sha1obj.update(title_a)
            hash = sha1obj.hexdigest()
            print 'hash: ',hash
            file=new_path+'/'+hash##hash 值作为文件名
            item['path']=file
            item['hash']=[hash]

            ##开始写一个文本
            #path_check='/data/news_data/all_news'
            path_check = '/data/news_data'
            ##crawl_body.file_check: 检查文件在既有文件夹下是否已经存在.如果已经存在,还要判断其是否异常。
            ##返回值 1: 存在且正常. 
            ##       0: 不存在  
            ##       2: 异常.
            pl = file_check_function.news_data_check(path_check,hash)
            ##pl = file_check(path_check,hash)
            if pl!=1:
                ##打开文件
                print '文件写入开始。hash: ',hash
                fp=open(file,'w')
        
                ##抓取、写入正文标题
                ##获取标题、取hash值
                print 'title: ',''.join(title[0]).encode('utf-8')
                fp.write( 'title:\n' )
                fp.write( ''.join(title[0]).encode('utf-8') ) 
                fp.write( '\n' )
        
                ##获取新闻发布时间、写入发布时间
                item['time_release']= [  ''.join(time_release).encode('utf-8') ]
                if len(time_release)==0:
                    item['time_release']=['']
                time_release= ''.join(time_release).encode('utf-8')
                print 'parse_body: time_release: ',time_release
                fp.write( 'time_release:\n' )
                fp.write( time_release )
                fp.write('\n')

                ##新闻链接
                fp.write( 'response:\n' )
                print 'response :\n',response
                fp.write( str(response)[5:].rstrip(">")   )
                fp.write('\n')

        
                ##获取摘要、写入摘要 
                ##abstract=response.xpath('//*[@id=\'Cnt-Main-Article-QQ\']/p[1]/text()').extract()
                ##print 'parse_body: abstract: ',''.join(abstract).encode('utf-8')##abstract 是有可能为空的,故不能给定索引.
                ##item['abstract']=abstract
                #fp.write( 'abstract:\n' )
                ##fp.write( ''.join(abstract ).encode('utf-8') )
                #fp.write('\n')
        
                ##抓取正文
                bodys_b=bodys.xpath('.//p')
                ##写入正文
                fp.write('main_body: \n')
                print 'main_body: '
                fp.write('\n')
                main_bodys = []
                for bod in bodys_b:
                    main_body=bod.xpath('text()').extract()
                    if ( len(main_body)!=0 and len( ''.join(main_body) )>=70 ) :
                        print ''.join(main_body[0]).encode('utf-8')
                        ##写入正文各段
                        fp.write( ''.join( main_body[0]).encode('utf-8')  )
                        main_bodys.append(main_body)
                        fp.write('\n')
                item['mainbody'] = main_bodys
    
                ##关闭文件
                fp.close()
                print 'finish.'
                print '\n\n\n\n'
                return item
    
            else:
                print 'pl: ',pl
                print '由于文件已经存在.无操作。'
    
        else:
            item['time_release']=['']
            item['hash']=['']
            print '标题为空。不操作。'
    
    
