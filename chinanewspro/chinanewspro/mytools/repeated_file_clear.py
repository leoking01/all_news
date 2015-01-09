#!/usr/bin/python
#! coding=utf-8 
import sys,os,time,datetime

from  somefunction  import get_filename,hashs_division,files_division,delete_repeated_files

######
dirs = '/data/news_data'
all_filenames = []
all_hashs = []
get_filename(dirs,all_filenames,all_hashs)
print 'len(all_filenames) : ',len(all_filenames)##25000
print 'len(all_hashs) : ',len(all_hashs)##同上 

hash_basic = []
hashs_division(all_hashs,hash_basic)
print 'len(hash_basic) :',len(hash_basic)##21000

hash_basic_logs = open('hash_basic_logs.txt','w')
for ha in hash_basic:
    hash_basic_logs.write( ''.join(ha)  )
    hash_basic_logs.write( '\n'  )
hash_basic_logs.close()##ok

file_basic = []
print 'len(all_filenames) : ',len(all_filenames)##25000
print 'len(hash_basic) :',len(hash_basic)##21000
files_division(all_filenames,hash_basic,file_basic)
print 'len(file_basic) : ',len(file_basic)

file_basic_logs=open( 'file_basic_logs.txt' ,'w' )
for fi in file_basic:
    file_basic_logs.write( ''.join(fi)  )
    file_basic_logs.write('\n')
file_basic_logs.close()

delete_repeated_files(all_filenames, file_basic)



