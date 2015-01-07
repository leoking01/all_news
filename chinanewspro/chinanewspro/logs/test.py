#! /usr/bin/env python
#coding=utf-8
#实现哈希表（线性地址再散列）

def ChangeKey(key,m,di):
    key01=(key+di) % m
    return key01

a=raw_input("Please entry the numbers:\n").split()
m=len(a)
dict01={}

for i in a:
    key=int(i)%m
    if "%s"%key in dict01:
        NewKey=ChangeKey(key,m,1)
        while "%s"%NewKey in dict01:         #因为下面的dict01的key值是以字符串来保存，因此这里作判断时也要用字符串格式
            NewKey=ChangeKey(NewKey,m,1)
        dict01["%s"%NewKey]=int(i)
    else:
        dict01["%s"%key]=int(i)
print dict01


