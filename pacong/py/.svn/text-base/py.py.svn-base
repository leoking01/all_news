#!/usr/bin/env python
#coding: utf-8
 
import urllib
import time
 
list00 = []
i = j = 0
page = 1
 
while page < 8:
        str = "http://blog.sina.com.cn/s/articlelist_1191258123_0_%d.html" %(page)
        content = urllib.urlopen(str).read()
 
        title = content.find(r"<a title")
        href  = content.find(r"href=",title)
        html  = content.find(r".html",href)
        url = content[href + 6:html + 5]
        urlfilename = url[-26:]
        list00.append(url)
        print i,  url
 
        while title != -1 and href != -1 and html != -1 and i < 350:
                title = content.find(r"<a title",html)
                href  = content.find(r"href=",title)
                html  = content.find(r".html",href)
                url = content[href + 6:html + 5]
                urlfilename = url[-26:]
                list00.append(url)
                i = i + 1
                print i,  url
        else:
                print "Link address Finshed."
 
        print "This is %s page" %(page)
        page = page + 1
else:
        print "spage=",list00[50]
        print list00[:51]
        print list00.count("")
        print "All links address Finshed."
 
x = list00.count('')
a = 0
while a < x:
        y1 = list00.index('')
        list00.pop(y1)
        print a
        a = a + 1
 
print list00.count('')
listcount = len(list00)
 
 
while j < listcount:
        content = urllib.urlopen(list00[j]).read()
        open(r"/tmp/hanhan/"+list00[j][-26:],'a+').write(content)
        print "%2s is finshed." %(j)
        j = j + 1
        #time.sleep(1)
else:
        print "Write to file End."
