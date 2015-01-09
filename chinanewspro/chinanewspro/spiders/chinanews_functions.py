# -*- coding: utf-8 -*-
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
    #print 'max_key,min_key :',max_key,min_key
    ddict = {}
    for dt in dict:
        #if dict[dt]> dict[min_key]+0.5*(dict[max_key]-dict[min_key]):
        if dict[dt]>= lamda*(dict[max_key]):
            ddict[dt]=dict[dt]
    return ddict
   

##标题检查函数
def title_check():


    pass
   
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
    
    
    
    
    
    
    
    
    
    
    
    
    
