# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from os import path
import datetime
import hashlib

from twisted.enterprise import adbapi
import MySQLdb.cursors
import MySQLdb

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy import log

class ChinanewsproPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='db_luokun',
            user='root', passwd='', cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8', use_unicode=True)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item


    def _conditional_insert(self, tx, item):
        re=0
        now=datetime.datetime.now()

        ##确定文件名
        title_a=['']
        if len(item['title'])!=0:
            title_a=''.join(  item['title'][0]  ).encode('utf-8')##!!必须采用严格的格式要求，保持一致
            re = tx.execute("select * from chinanews where title = %s", (item['title'][0], ))
            if re:
                log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
            else:
                if 1==1:
                    t = datetime.datetime.now()
                    ##t=str(t).split('.')
                    ##t=t[0]
                    #link,time_release,response_news='','',''
                    ##link
                    #if  len(item['link'])==0:
                    #    item['link']=['']
                    ##response_news
                    #if  len(item['response_news'])==0:
                    #    item['response_news']=['']
                    ##time_release
                    ########################print 'pipline: item:',item
                    #if  len( item['time_release'] ) == 0:
                    #    item['time_release']=['']
                    ##hash
                    #if  len( item['hash'] ) == 0:
                    #    item['hash']=['']
                    #print "pipline: item[\'time_release\']:",''.join( item['time_release'] ).encode('utf-8')
                        
                    tx.execute( "insert into chinanews(title,link,response_news,time_release,time_add,hash,manufacturer,path)"
                            " values(%s,%s,%s,%s,%s,%s,%s,%s)" ,(title_a,item['link'],item['response_news'],item['time_release'] ,t,item['hash'],item['manufacturer'],item['path'] )   )
                    print 'db_store: title: ',''.join(item['title'][0]).encode('utf-8')
                    print '\n\n\n\n'
                    log.msg("Item stored in db: %s" % item, level=log.DEBUG)

                     
    def handle_error(self, e):
        log.err(e)


    ##自定义哈希函数
    def hash_my(tx):
        pass
                                              
                                              
                                              
