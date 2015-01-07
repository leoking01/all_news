#!/usr/bin/env python
#coding:utf-8
#Author：Allentuns
#Email：zhengyansheng@hytyi.com
 
 
import urllib
import os
import sys
import time
 
ahref = '<a href="'
ahrefs = '<a href="h'
ahtml = ".htm"
atitle = "<img style"
ajpg = ".jpg"
btitle = '<img src="'
 
page = 0
while page < 4300:    #这个地方可以修改;最大值为4300，我测试的时候写的是3.
        mmurl = "http://mm.taobao.com/json/request_top_list.htm?type=0&page=%d" %(page)
        content = urllib.urlopen(mmurl).read()
 
        href = content.find(ahref)
        html = content.find(ahtml)
        url = content[href + len(ahref) : html + len(ahtml)]
        print url
        imgtitle = content.find(btitle,html)
        imgjpg = content.find(ajpg,imgtitle)
        littleimgurl = content[imgtitle + len(btitle): imgjpg + len(ajpg)]
        print littleimgurl
 
        urllib.urlretrieve(littleimgurl,"/www/src/temp/image/taobaomm/allentuns.jpg")
 
        s = 0
        while s < 18:
                href = content.find(ahrefs,html)
                html = content.find(ahtml,href)
                url = content[href + len(ahref): html + len(ajpg)]
                print s,url
 
                imgtitle = content.find(btitle,html)
                imgjpg = content.find(ajpg,imgtitle)
                littleimgurl = content[imgtitle : imgjpg + len(ajpg)]
                littlesrc = littleimgurl.find("src")
                tureimgurl = littleimgurl[littlesrc + 5:]
                print s,tureimgurl
 
 
                if url.find("photo") == -1:
                        content01 = urllib.urlopen(url).read()
                        imgtitle = content01.find(atitle)
                        imgjpg = content01.find(ajpg,imgtitle)
                        littleimgurl = content01[imgtitle : imgjpg + len(ajpg)]
                        littlesrc = littleimgurl.find("src")
                        tureimgurl = littleimgurl[littlesrc + 5:]
                        print tureimgurl
 
                        imgcount = content01.count(atitle)
                        i = 20
                        try:
                                while i < imgcount:
                                        content01 = urllib.urlopen(url).read()
                                        imgtitle = content01.find(atitle,imgjpg)
                                        imgjpg = content01.find(ajpg,imgtitle)
                                        littleimgurl = content01[imgtitle : imgjpg + len(ajpg)]
                                        littlesrc = littleimgurl.find("src")
                                        tureimgurl = littleimgurl[littlesrc + 5:]
                                        print i,tureimgurl
                                        time.sleep(1)
                                        if tureimgurl.count("<") == 0:
                                                imgname = tureimgurl[tureimgurl.index("T"):]
                                                urllib.urlretrieve(tureimgurl,"/www/src/temp/image/taobaomm/%s-%s" %(page,imgname))
                                        else:
                                                pass
                                        i += 1
                        except IOError:
                                print '/nWhy did you do an EOF on me?'
                                break
                        except:
                                print '/nSome error/exception occurred.'
 
                s += 1
        else:
                print "---------------{< 20;1 page hava 10 htm and pic  }-------------------------}"
        page = page + 1
        print "****************%s page*******************************" %(page)
else:
        print "Download Finshed."
