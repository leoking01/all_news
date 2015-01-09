#!/usr/bin/python
#! coding=utf-8 
import sys,os,time,datetime


def get_filename( dirs,all_filenames,all_hashs ):
    ##all_filenames = []
    for dir in os.listdir(dirs):
        dir_0 = dirs+'/'+dir
        if os.path.isdir(dir_0):
            get_filename(dir_0, all_filenames,all_hashs)
        elif os.path.isfile(dir_0):
            all_filenames.append(dir_0)
            all_hashs.append(dir)
        else:
            pass

    return all_filenames


def hashs_division(hashs_all,hashs_basic):
    if len(hashs_all)==0:
        return 0
    for hash in hashs_all:
        if len(hashs_basic)==0:
            hashs_basic.append(hash)
        else:
            pass
        
        indi = 0
        for ha in hashs_basic:
            if ha == hash:
                indi += 1
                print '发现相同项.hash:',hash
                break
            else:
                pass
                ##continue
        if indi == 0:
            print 'indi = ',indi,'将附加hash:',hash
            hashs_basic.append(hash)


######  !!!! 
def files_division(file_all,hash_basic, file_basic):
    if len(file_all)==0 or len(hash_basic)==0:
        return 0
    for ha  in hash_basic:
        indi = 0 
        for file in file_all:
            if file.find(ha)!= -1:
                indi = 1
                file_basic.append(file)
                file_basic_store=open('file_basic_store.txt','a')
                file_basic_store.write( str(file) )
                file_basic_store.write( '\n' )
                file_basic_store.close()
                break ##return file_basic 
    return file_basic
        





def delete_repeated_files(file_all,file_basic):
    for file in file_all:
        if not file in file_basic:
            ##print ' delete_repeated_files: will delete file  ',file
            delete_pro=open('deleted_files20150109.txt','a')
            delete_pro.write( str(file) )
            delete_pro.write( '\n' )
            delete_pro.close()##希望这个文件永远为空.
            os.remove(file)####终于不用再注释这一行了

    pass

