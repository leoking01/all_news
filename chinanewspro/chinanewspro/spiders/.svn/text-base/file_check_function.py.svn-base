# -*- coding: utf-8 -*-
## 函数1 parse_body ： 暂无用 。 类函数。
## 函数2 file_check :  检查文件是否在路径中存在。全局函数
import scrapy
from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.utils.response import get_base_url

from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlunparse
from posixpath import normpath
import datetime,time
import hashlib,os,sys

   
    ##正文抓取函数
def parse_body(self,response):
    #print 'parse_body: create dir-file,write in...'
    #print 'parse_body: response: ',response
   
    #建立文件路径
    old_path='/data/news_data/qq_news/'
    t=time.localtime()
    t=time.strftime('%Y_%m_%d',t)
    new_path=os.path.join(old_path,t)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    
    
    #建立文件名
    file=''
    if len(title)!=0:
        title_a=''.join(title[0])
        ##title_a=str( ( title[0] ) ).encode('utf-8')##
        sha1obj = hashlib.sha1()
        sha1obj.update(title_a)
        hash = sha1obj.hexdigest()
        file=new_path+'/'+hash##hash 值作为文件名

    ##读取当前路径下文件列表、并判断
    res=os.listdir(new_path)
    #print 'parse_body: type(res): ',type(res)
    #print 'parse_body: res: ',res
    ##print 'res:',str(res).encode('utf-8')
    pl=0
    for sh in res:
        if sh==hash:
            pl=1
    #print 'pl:',pl
    if pl==0:
        ##打开文件
        fp=open(file,'w')
        
        ##抓取、写入正文标题
        if len(title)!=0:
            ##获取标题、取hash值
            title=response.xpath('//*[@id=\'C-Main-Article-QQ\']/div[1]/h1/text()').extract()
            #print 'title: ',''.join(title[0]).encode('utf-8')
            ##写入标题
            fp.write( 'title:\n' )
            #fp.write( str( title[0].encode('utf-8') ) )
            fp.write( ''.join(title[0]).encode('utf-8') ) 
            fp.write( '\n' )
        
            ##获取新闻发布时间、写入发布时间
            time_release=response.xpath('//*[@id=\'C-Main-Article-QQ\']/div[1]/div[1]/div[1]/span[@class="article-time"]').extract()
            fp.write( 'time_release:\n' )
            fp.write( time_release )
            fp.write('\n')
        
            ##获取摘要、写入摘要 
            abstract=response.xpath('//*[@id=\'Cnt-Main-Article-QQ\']/p[1]').extract()
            fp.write( 'abstract:\n' )
            fp.write( abstract )
            fp.write('\n')
        
            ##抓取正文
            bodys_a=response.xpath('//div[@id=\'Cnt-Main-Article-QQ\']')
            bodys_b=bodys_a.xpath('.//p')
            ##写入正文
            fp.write('main_body: \n')
            fp.write('\n')
            for bod in bodys_b:
                main_body=bod.xpath('text()').extract()
                if len(main_body)!=0:
                    #print 'main_body: ',main_body[0].encode('utf-8')
                    ##写入正文各段
                    fp.write( str( main_body[0].encode('utf-8') ) )
                    fp.write('\n')
            #fp.write('finish.\n')
    
                    ##关闭文件
        fp.close()
    
    
    
##文件检查函数: 检查文件是否在某路径下存在.
##参数path: 路径
##    hash: 哈希值，即文件名
##返回值：0 -- 文件不存在
##        1 -- 文件已经存在
##dirs_base='/data/news_data/all_news'
##dir_0 = ./manu
##dir_b = ./datetime
def file_check(dirs_base,hash):
    dirs_main = os.listdir(dirs_base)
    state = 0

    for d in dirs_main:
        dir_0 = dirs_base+'/'+d
        if os.path.isdir(dir_0):
            for dir_a in os.listdir(dir_0):
                dir_b=dir_0+'/'+dir_a
                if os.path.isdir(dir_b):
                    for file in os.listdir(dir_b):
                        if hash==file:
                            state=1
                            v=os.path.getsize(dir_b+'/'+''.join(file) )
                            if v<200:
                                state=0
                                pass
                                #print '文件虽然存在但有异常(文件过小,可能是假新闻.)'
                            else:
                                #print '文件是正常的.'
                                pass
                        else:
                            pass
                else:
                    if hash==dir_a:
                        state=1
                        v=os.path.getsize(dir_b )
                        if v<100:
                            state=0
                            pass
                            #print '文件虽然存在但有异常(文件过小,可能是假新闻.)'
                        else:
                            #print '文件是正常的.'
                            pass
                    else:
                        pass
        else:
            pass 
    return state
    
   
def news_data_check(dirs_base,hash):
    dir_base = os.listdir(dirs_base)
    state = 0
    for dir in dir_base:
        path_t = dirs_base+'/'+dir
        state = file_check(path_t,hash)

    return state





