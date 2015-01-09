#!/usr/bin/python
# -*- coding: utf-8 -*-
## 函数1 delete_repeat() ： 去重
import datetime,time
import hashlib,os,sys
    
##文件检查函数: 检查文件是否在某路径下存在.
##参数path: 路径
##    hash: 哈希值，即文件名
##返回值：0 -- 文件不存在
##        1 -- 文件已经存在
##dirs_base='/data/news_data/all_news'
##dir_0 = ./manu
##dir_b = ./datetime
def check_delete_one_file(dirs_base,hash):
    dirs_main = os.listdir(dirs_base)
    state = 0
    print 'check_delete_one_file,dirs_base: ',dirs_base
    noter = open('delete_file2.txt','a')
    
    for d in dirs_main:
        dir_0 = dirs_base+'/'+d
        ##print 'check_delete_one_file: dir_0: ',dir_0
        if os.path.isdir(dir_0):
            for dir_a in os.listdir(dir_0):
                dir_b=dir_0+'/'+dir_a
                ##如果dir_b 是文件夹
                if os.path.isdir(dir_b):
                    for file in os.listdir(dir_b):
                        if hash==file:
                            state = 1
                            print 'will remove (dir_b+\'/\'+\'\'.join(file)): ',dir_b+'/'+''.join(file)
                            ##os.remove(  dir_b+'/'+''.join(file)  )
                            return state
                        else:
                            pass
                ##如果dir_b是文件
                elif os.path.isfile(dir_b):
                    if hash==dir_a:
                        state = 1
                        print 'will remove dir_b : ',dir_b
                        ##os.remove(  dir_b  )
                        return state
                    else:
                        pass
        elif os.path.isfile(dir_0):
            if hash==d:
                state = 1
                print 'will remove file: dir_0:' , dir_0
                os.remove(dir_0)
                noter.write( str( datetime.datetime.now() )  )
                noter.write(dir_0)
                noter.write('\n')
                noter.close()
                ##v=os.path.getsize(dir_0 )
                return state
            else:
                pass
    return state
   
   
##def news_data_check(dirs_base,hash):
##    dir_base = os.listdir(dirs_base)
##    state = 0
##    for dir in dir_base:
##        path_t = dirs_base+'/'+dir
##        state = file_check(path_t,hash)
##        if state!=0:
##            return state
##    return state


##dirs=/data/news_data/all_news
##dirs_target=[contains('2015_01_07','08')]
##dirs_refer=[contains('2015_01_06') ]
def get_dirs_target(dirs,dirs_target, dirs_refer, ref_date):
    dirs_total = []

    for dir in os.listdir(dirs):##munu
        dir_a = dirs+'/'+dir
        for dir_b in os.listdir(dir_a):##2015_01_06
            dir_c = dir_a+'/'+dir_b
            dirs_total.append(dir_c)

    for dir in dirs_total:
        if ''.join(dir).find( ref_date  ) == -1:
            dirs_target.append(dir)
        elif ''.join(dir).find( ref_date ) != -1:
            dirs_refer.append(dir)
        else:
            print 'something wrong.'
    print 'something right.'
    print 'length dirs_refer: ',len(dirs_refer)
    print 'length dirs_target: ',len(dirs_target)
    print 'length dirs_total: ',len(dirs_total)


def delete_files(dirs_target,dirs_refer):
    hashs=[]
    for dir_r in dirs_refer:
        hash = os.listdir(dir_r)
        for ha in hash:
            hashs.append(ha)

    for hash in hashs:
        for dir_tar in dirs_target:
            check_delete_one_file(dir_tar,hash)


dirs_target=[]
dirs_refer=[]
dirs='/data/news_data/all_news'
ref_date='2015_01_06'
ref_date='2015_01_07'


get_dirs_target(dirs,dirs_target,dirs_refer, ref_date)
print 'length dirs_target : ',len(dirs_target)
print 'length dirs_refer : ',len(dirs_refer)
delete_files(dirs_target,dirs_refer)



