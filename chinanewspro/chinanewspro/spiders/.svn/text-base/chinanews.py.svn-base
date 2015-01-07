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

from file_check_function  import file_check
import file_check_function
from chinanewspro.items import ChinanewsproItem
import urls

import time

sys.stdout=open('log.txt','w')

    
def list_2_dict(ls):
    """
    @function  : list_2_dict : 根据一个原始列表生成一个字典，用于统计并记录其各项出现的频数.
    @parameter : ls : 列表
    @返回值：一个字典
    """
    ##创建一个无重复的列表
    new_ls=[]
    for it in ls:
        if len(new_ls)==0:
            new_ls.append(it)
        else:
            for itt in new_ls:
                state=bianli(new_ls,it)
                if state==1:
                    pass
                else:
                    new_ls.append(it)
    ##创建默认字典
    length_frequency={}.fromkeys(new_ls,0)
    ##创建字典
    for it in ls:
        for itt in length_frequency:
            if itt==it:
                length_frequency[itt]+=1
    return length_frequency
    #return new_ls
    
    
def bianli(ls,item):
    """
    #@function:遍历一个list,返回特定项item是否存在
    #@parameter: ls: 列表
    #@parameter: item: 特定项
    #0: 存在
    #1：不存在
    """
    state=0
    for it in ls:
        if it==item:
            state=1
        else:
            pass
    return state


def dict_max(dict):
    """
    遍历字典，返回值最大的那一项的键
    """
    length_frequency={}
    value=0
    if len(dict)==0:
        return 0
    for dt in dict.keys():
        if dict[dt]>value:
            value=dict[dt]
    for dt in dict.keys():
        if value==dict[dt]:
            return dt


def dict_min(dict):
    """
    遍历字典，返回值最小的那一项的键
    """
    length_frequency={}
    value=0
    if len(dict)==0:
        return 0
    for dt in dict.keys():
        if dict[dt]<value:
            value=dict[dt]
    for dt in dict.keys():
        if value==dict[dt]:
            return dt

def dict_modif(dict):
    """
    修改一个给定的字典。
    返回一个新字典，其中频数最高的那个项的附近项被去掉.
    """
    length_frequency = dict.copy()

    if len(dict)!=0:
        max_key = dict_max(dict)
        del length_frequency[ max_key ]

    if len(length_frequency)!=0:
        max_key = dict_max(length_frequency)
        del length_frequency[ max_key ]

    if len(length_frequency)!=0:
        max_key = dict_max(length_frequency)
        del length_frequency[ max_key ]

    if len(length_frequency)!=0:
        max_key = dict_max(length_frequency)
        del length_frequency[ max_key ]

    return length_frequency



def evaluation(dict,lamda):
    """
    长度-频数 字典 评估处理函数.
    input: dict: 候选字典.
            lamda: 控制系数.控制系数越小，则越松弛。越大则越严格.
    返回一个字典，其中只有被评估之后的项.
    """
    if len(dict)==0:
        return {}
    max_key=dict_max(dict)
    #min_key=dict_min(dict)
    #print 'max_key,min_key :',max_key,min_key
    ddict = {}
    for dt in dict:
        #if dict[dt]> dict[min_key]+0.5*(dict[max_key]-dict[min_key]):
        if dict[dt]>= lamda*(dict[max_key]):
            ddict[dt]=dict[dt]
    return ddict
   

   
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

class ChinanewsSpider(scrapy.Spider):
    """
    ##所有新闻爬虫
    """
    """
    all_urls = (
        ##中国新闻网
        ###################################################
        ##############       中新网    ####################
        ###################################################
        ##'http://www.chinanews.com/',              ##中国新闻网                    OK
        'http://www.chinanews.com/china.shtml',##国内
        'http://www.chinanews.com/society.shtml',##社会
        ##分社网站
        ##http://www.chinanews.com/common/footer/zswz.shtml
        'http://www.ah.chinanews.com/portal.php?mod=list&catid=28',##安徽社会
        'http://www.bj.chinanews.com/focus/1.html',##北京聚焦
        'http://www.bj.chinanews.com/focus/6.html',##北京社会
        'http://www.fj.chinanews.com/new2014/shms/list.html',##福建社会
        'http://www.fj.chinanews.com/new2014/jryw/list.html',##福建-今日要闻
        'http://www.gs.chinanews.com/gsyw1/m1.html',##甘肃要闻
        'http://www.gd.chinanews.com/index/gddt.html',##广东动态
        'http://www.cq.chinanews.com/Include/newsmenu.asp?Id=119',##重庆新闻
        'http://www.hi.chinanews.com/gundong/hnnews.html',##海南新闻
        'http://www.gx.chinanews.com/GBK/1913/',##广西社会法治
        'http://www.ha.chinanews.com/GNnews/1/index.shtml',##河南新闻
        'http://www.heb.chinanews.com/hbzy/334.shtml',##河北要闻
        'http://www.hb.chinanews.com/hbxw.html',##湖北要闻
        'http://www.hn.chinanews.com/news/hnyw/index.shtml',##湖南  要闻
        'http://www.hn.chinanews.com/news/shsh/',##湖南 社会
        'http://www.js.chinanews.com/citynews/',##江苏社会
        'http://www.jx.chinanews.com/society/',##江西社会
        'http://www.jl.chinanews.com/jlyw.html',##吉林要闻
        'http://www.ln.chinanews.com/liaoningxinwen/',##辽宁要闻
        'http://www.sx.chinanews.com/4/2009/0107/1.html',##山西要闻
        'http://www.shx.chinanews.com/shfz.html',##陕西 社会法制 
        'http://www.shx.chinanews.com/sxxw.html',##陕西 市县新闻
        'http://www.sh.chinanews.com/society',##上海  社会民生
        'http://www.sc.chinanews.com/news/News_SiChuan/list.html',##四川新闻
        'http://www.hkcna.hk/m/wgyw.html',##香港  维港要闻
        'http://www.sh.chinanews.com/shnews',##上海  上海新闻
        'http://www.xj.chinanews.com/html/L_69.htm',##新疆 要闻
        'http://www.xj.chinanews.com/html/L_64.htm',##新疆 社会民生
        'http://www.bt.chinanews.com/News/yaowen/',##兵团 要闻
        'http://www.bt.chinanews.com/News/jiangnei/',##  兵团  疆内
        'http://www.yn.chinanews.com/ynxw/index.shtml',##云南 新闻
        'http://www.zj.chinanews.com/zhejiang/',##浙江新闻网
        'http://www.chinanews.com/best-news/news1.html',##贵州 精选新闻
        'http://www.hlj.chinanews.com/focus/xwdd.html',##黑龙江。这个网站难道不更新了？20150106看到最新的新闻是20141012。  
        'http://www.nmg.chinanews.com/nmgrd/',##内蒙古新闻   内蒙古的网速极慢啊   
        #'',##

        ##tencent
        ###################################################
        ##############       QQ    ########################
        ###################################################
        'http://news.qq.com/society_index.shtml', ##腾讯网 新闻中心 社会新闻        F
        'http://news.qq.com/china_index.shtml',   ##腾讯网 新闻中心 国内新闻    F
        'http://news.qq.com/top_index.shtml',     ##腾讯网 新闻中心 要闻            F
        #'地方站：'上海广东四川重庆陕西湖南湖北福建河南浙江辽宁江苏
        'http://sh.qq.com/news/',##  大申网
        'http://gd.qq.com/news/',##  粤
        'http://cd.qq.com/news/',##川
        'http://cq.qq.com/news/',##  渝
        'http://xian.qq.com/life/',##   陕西
        'http://hn.qq.com/l/news/sz/list2012022151359.htm',##  大湘  民生时事
        'http://hn.qq.com/l/news/ms/list2012022151800.htm',## 大湘  社会万象
        'http://hb.qq.com/news/',## 湖北
        'http://fj.qq.com/news/',## 福建
        'http://henan.qq.com/news/',## 河南
        'http://henan.qq.com/l/news/hlt/cspdhltlist.htm',##  河南 社会
        'http://henan.qq.com/l/news/hnxw/cspdhznlist.htm',## 河南  时事
        'http://henan.qq.com/l/news/blt/blt.htm',##河南民生
        'http://zj.qq.com/news/',## 浙江
        'http://ln.qq.com/news/',## 辽宁
        'http://ln.qq.com/l/news/news_ms/lnms.htm',## 民生焦点
        'http://ln.qq.com/l/news/news_shwx/shwx.htm',## 社会
        'http://ln.qq.com/l/news/loaclnews/localnews.htm',## 本地
        'http://js.qq.com/news/index.html',## 江苏
        #'',##
        'http://bj.jjj.qq.com/news/',##  河北
        #'',##
        #'',##
        #'',##
        #'',##
        #'',##

        ##新浪
        'http://news.sina.com.cn/society/',       ##新浪网新闻中心社会新闻
        'http://news.sina.com.cn/china/' ,        ##新浪网新闻中心国内新闻
        
        ##百度
        ##'http://news.baidu.com/',
        ##'http://guonei.news.baidu.com/',  ##   error   !!
        ##'http://shehui.news.baidu.com/',  ###  error   !!
        'http://shehui.news.baidu.com/n?cmd=4&class=socianews&pn=1',##百度 社会最新首页
        'http://news.baidu.com/n?cmd=4&class=shyf&pn=1',##百度社会与法
        'http://news.baidu.com/n?cmd=4&class=civilnews&pn=1&from=tab',##百度国内最新首页
        ##'',##
        ##'',##
        ##'',##

        #新华网
        ##'http://www.xinhuanet.com/',
        'http://www.news.cn/local/index.htm',
        'http://www.xinhuanet.com/local/#1',   
        'http://www.xinhuanet.com/local/',
        'http://www.news.cn/local/dfyw/index.htm',
        'http://www.news.cn/local/shwx.htm',

        ##'http://news.ifeng.com/',
        'http://news.ifeng.com/mainland/',      ###    F    待检查
        'http://news.ifeng.com/society/index.shtml',
        'http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml',

        ##'http://news.sohu.com/',
        'http://news.sohu.com/shehuixinwen.shtml',

        #网易新闻
        ##'http://news.163.com/',
        'http://news.163.com/domestic/',
        'http://news.163.com/shehui/', 

        ##'http://www.stnn.cc/',##星岛环球网
        'http://news.stnn.cc/china/',

        ##人民网
        ##'http://www.people.com.cn/',
        'http://society.people.com.cn/',     ####有乱七八糟的东西。 查一下这个网。
        'http://leaders.people.com.cn/GB/357524/index.html',
        'http://society.people.com.cn/GB/136657/index.html',##要闻

        'http://www.zaobao.com/',   ##联合早报
        ##中国政府网

        ##'http://www.huanqiu.com/',
        'http://china.huanqiu.com/',##环球网
        'http://society.huanqiu.com/',

        ##中华网
        ##'http://news.china.com/',
        'http://news.china.com/zh_cn/domestic/index.html',
        'http://news.china.com/zh_cn/social/index.html',

        ##'http://www.china.com.cn/',##中国网
        'http://news.china.com.cn/shehui/node_7185032.htm',
        'http://news.china.com.cn/',
        'http://news.china.com.cn/node_7115409.htm',

        ##'http://www.cyol.net/',##中国青年报
        'http://news.cyol.com/',
        'http://news.cyol.com/node_10005.htm',##国内
        'http://yuqing.cyol.com/',##舆情
        'http://news.cyol.com/node_10000.htm',##要闻

        ##羊城晚报
        ##'http://www.ycwb.com/',
        'http://news.ycwb.com/n_gn.htm',    ##  test  OK

        ##光明网
        'http://news.gmw.cn/newspaper/',##滚动     ##  OK  
        'http://politics.gmw.cn/node_9840.htm',##时政频道-国内
        'http://politics.gmw.cn/node_9844.htm',##时政频道-要闻
        'http://life.gmw.cn/node_9268.htm',##生活频道-要闻
        'http://life.gmw.cn/node_9267.htm',##生活资讯


        ###################################################
        ##############   安监网    ########################
        ###################################################
        'http://www.chinasafety.gov.cn/newpage/sgkb/sgkb.htm',###重特大事故信息
        'http://www.bjsafety.gov.cn/accidentinfor/sgkb/index.html?nav=20&sub=0'##北京事故快报
        'http://www.tjsafety.gov.cn/tj/shigukuaixun/index.html#page_1',##天津  事故快讯
        'http://www.hebsafety.gov.cn/index.do?templet=cs_ghkj_sg&cid=214',##河北  事故快报
        'http://www.sxaj.gov.cn/xx/zyhd/index.html',##山西  安全要闻
        'http://222.74.213.213:81/A/?L-9407210300.Html',##  内蒙
        'http://www.lnsafety.gov.cn/quick/gd1.asp',##  辽宁
        ##'http://www.lnsafety.gov.cn/quick/gd1.asp',##
        'http://www.jlsafety.gov.cn/sgxx/index.htm',## 吉林
        ##'http://www.hlsafety.gov.cn/zwgk/dtyw/sgkb/index.htm',## 黑龙江     !!!!error    暂时不知什么原因。严重错误。
        'http://www.shsafety.gov.cn/article/loadColumn.htm?columnId=1000137&pid=1000480',##  上海
        #'',##江苏的没有事故快报。
        'http://www.zjsafety.gov.cn/cn/sgkb/',##浙江
        'http://www.anhuisafety.gov.cn/views/zwgk/list/260100.htm',##安徽
        #'',##福建。没有事故快报模块
        'http://www.jxsafety.gov.cn/news/8.aspx',##江西 安全生产事故
        #'',##山东的没新闻内容。
        'http://www.hnsaqscw.gov.cn/viewCmsCac.do?cacId=40288177343d854301343dc2f85201d4',##  河南事故快报
        ##'http://www.hubeisafety.gov.cn/sample/article.asp?menuid=100&menu1=%B0%B2%C8%AB%CD%B3%BC%C6&menu2=%CA%C2%B9%CA%BF%EC%B1%A8',## 湖北  事故快报
        'http://www.hunansafety.gov.cn/shigukuaibao/',##混恩事故快报
        'http://www.gdsafety.gov.cn/sydllm/swsg/',## 广东 
        'http://www.gxajj.com/html_accident_report/default.html',##广西
        #'',##海南  无具体新闻列表。 只有每个月份新闻简报
        ##'http://www.cqsafety.gov.cn/infosListNew.jsp?item=AJ02&argId=PYmvSC9YF0bx00JNVRMCN6i35LqaAFCC6oGICvxu8pGnaashRY0u86VYYR5QorIt',##  重庆  事故快讯
        #'',##四川  没有新闻简报
        'http://www.gzaj.gov.cn/GZAJ/P/index.shtml',##贵州事故信息
        'http://www.tibetsafety.gov.cn/article.php?m=index&a=index&pid=111',## 西藏  事故快报
        'http://www.snsafety.gov.cn/admin/pub_newschannel.asp?chid=100102',##陕西 事故快报
        'http://www.ynsafety.gov.cn/channels/228.html',## 云南
        #'',##甘肃的  没有
        #'',##青海  没事故
        'http://www.nxsafety.gov.cn/sgtb/page00010007.html',##宁夏   事故通报
        'http://www.xjsafety.gov.cn/tabid/12',## 新疆  事故快报
        #'',##大连   没有事故快报
        'http://www.nbsafety.cn/zwgk/aqtb/sgkb/nbsgkb/index.htm',##  宁波  宁波事故
        'http://www.nbsafety.cn/zwgk/aqtb/sgkb/zjsgkb/index.htm',##宁波  浙江事故
        'http://media.chinasafety.gov.cn:8090/iSystem/shigumain.jsp',##  宁波  国家事故
        #'',##厦门  无信息
        ##'http://www.qdajj.gov.cn/mainone/Columns/sgkx.shtml',## 青岛
        'http://www.qdajj.gov.cn/mainone/Columns/yuqingxinxi.asp?typeid=1911&parentid=1908&videos=&jms=94',##青岛
        'http://www.szemo.gov.cn/yjjy/tfsj/zrzh/',## 深圳  自然灾害
        'http://www.szemo.gov.cn/yjjy/tfsj/sgzn/',##深圳  事故
        'http://www.szemo.gov.cn/yjjy/tfsj/ggwssj/',## 深圳  公共卫生
        'http://www.szemo.gov.cn/yjjy/tfsj/shaqsj/',##深圳  社会安全
        #'http://www.hunansafety.gov.cn/',##  湖南的   打不开.
        #'',##
        #'',##
    )


    test_urls = (
        )
    """
    name = "all_news"
    allowed_domains = []
    ##start_urls = all_urls 
    start_urls = urls.all_urls 
    ##start_urls = test_urls 

   
   
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
        #print 'length_frequency: ',length_frequency
        #leng_golden = dict_max(length_frequency)
        
        #leng_silver,leng_copper = 0,0
        #length_frequency_a = dict_modif(length_frequency)
        #print 'length_frequency_a: ',length_frequency_a
        #if len(length_frequency)!=0:
        #    leng_silver = dict_max(length_frequency_a)

        #length_frequency_a = dict_modif(length_frequency_a)
        #print 'length_frequency_a: ',length_frequency_a
        #if len(length_frequency)!=0:
        #    leng_copper = dict_max(length_frequency_a)

        #print 'leng_golden  leng_silver  leng_copper \n',leng_golden,leng_silver,leng_copper


        #创建候选字典
        #b,c = 0,0
        #a = length_frequency[leng_golden]
        #if leng_silver!=0:
        #    b = length_frequency[leng_silver]
        #if leng_copper!=0:
        #    c = length_frequency[leng_copper]
        #dict_candi = dict(( [leng_golden,a],[leng_silver,b],[leng_copper,c]   ))
        
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
                    ##url_m= (str(href))[3:-2]   ####这里需要小心.
                    ##url_m= ''.join(href)
                    ##url_new=urljoin(base_url,url_m )
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
        ##manu=manu.repalce('\%','_')
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
            item['hash']=[hash]

            ##开始写一个文本
            #path_check='/data/news_data/all_news'
            path_check='/data/news_data'
            ##crawl_body.file_check: 检查文件在既有文件夹下是否已经存在.如果已经存在,还要判断其是否异常。
            ##返回值 1:存在且正常.  2:不存在或者异常.
            pl = file_check_function.news_data_check(path_check,hash)
            ##pl = file_check(path_check,hash)
            if pl==0:
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
                for bod in bodys_b:
                    main_body=bod.xpath('text()').extract()
                    if ( len(main_body)!=0 and len( ''.join(main_body) )>=70 ) :
                        print ''.join(main_body[0]).encode('utf-8')
                        ##写入正文各段
                        fp.write( ''.join( main_body[0]).encode('utf-8')  )
                        fp.write('\n')
    
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
        ##print '\n\n\n\n'
    
    
    
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
    
    
def dir_creat(basic_path,dir_name): 
        """
        #建立文件路径,并返回
        old_path: 旧路径
        dir_name: 文件夹名
        """
        ##旧路径检查
        ##old_path='/data/news_data/all_news/'
        path_reconiz=os.path.exists(basic_path)
        if path_reconiz==1:
            pass
        else:
            os.mkdir(basic_path)
        ##文件夹名
        ##t=time.localtime()
        ##t=time.strftime('%Y_%m_%d',t)
        ##dir_name=t
        ##创建文件路径
        new_path=os.path.join(basic_path,dir_name)
        if not os.path.isdir(new_path):
            os.mkdir(new_path)##只有当路径不存在的情况下，才创建路径
        ##新路径检查
        ##path_check=os.path.exists()
        return new_path
    
    
##返回(评估)列表中最大长度的项    
def list_evaluation(ls):
    #lt = ls.copy()
    length_max=0
    if len(ls)==0:
        return []
    for it in ls:
        if len(''.join(it)) > length_max:
            length_max = len(''.join(it))
    for it in ls :
        if length_max == len(''.join(it)):
            return it
    
    
    
    
    
    
    
    
    
    
    
    
    
