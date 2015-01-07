#!/usr/bin/python
#!coding: utf-8 
def makedict(ls):
    """
    @function  : makedict : 根据一个列表生成一个字典
    @parameter : ls : 列表
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
    #ddict={}.fromkeys(new_ls,0)
    ##创建字典
    #for it in ls:
    #    for itt in ddict:
    #        if itt==it:
    #            ddict[itt]+=1
    #return ddict
    return new_ls

#@function:遍历一个list,返回是否存在
#@parameter: ls: 列表
#@parameter: item: 特定项
#0: 存在
#1：不存在
def bianli(ls,item):
    state=0
    for it in ls:
        if it==item:
            state=1
        else:
            pass
    return state


ls=[1,2,3,3,2,2] 
print makedict(ls)
   
