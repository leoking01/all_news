#!/usr/bin/python
#! coding: utf-8
import os ,sys
sys.path.append('/home/luokun/work/scrapy_projects/allnewsproject/chinanewspro/chinanewspro/spiders')
import urls

from  somefunction  import get_filename,hashs_division,files_division,delete_repeated_files

##======================  空文件夹数 ====================
def get_number_from_errorfile(error_urls_file):
    error_urls_file='error_urls.txt'
    ##post_pro = open('error_urls.txt','r')
    post_pro = open(error_urls_file,'r')
    pro = post_pro.readlines()
    ##print 'pro = ',pro
    new_error_oper = open('new_error.txt','w+')
    no = 0
    for ur in pro:
        if ur.find('2015_01_07')!= -1:
            new_error_oper.write(ur)
            no+=1
    new_error_oper.close()

    post_pro.close()

    return no


########################################################################
##############   空文件夹搜索       ，统计、数据文件分布    ############
########################################################################
##def error_urls_gen():
if os.path.isfile('error_urls.txt'):
    os.remove('error_urls.txt')


##======================  文件清点 ====================
#print '='*105
print '*'*120
print '*'*52,' file   count ',52*'*'
print '*'*120

print "自12月30日开始，当日数据不再与之前数据有重复."##.encode('utf-8')

dirs_base='/data/news_data/'
dirs_main=os.listdir(dirs_base)
print 'director base: ',dirs_base
print 'directors list: '
for d in dirs_main:
    print d

for d in dirs_main:
    dir_0='/data/news_data/'+d
    print '\n'
    print 'directory: ',dir_0
    print '%-80s' %('='*120)
    print '%-80s %10s' %('director','number')
    all_total_number=0
    all_dir_number = 0
    date_number_dict={}
    for dir_a in os.listdir(dir_0):
        dir_b=dir_0+'/'+dir_a
        all_dir_number += 1
        print '\t%-70s %10s' %( dir_b,len( os.listdir(dir_b) )  )
        for dir_c in os.listdir(dir_b):
            dir_d = dir_b+'/'+dir_c
            if os.path.isdir(dir_d):
                number = len( os.listdir(dir_d) )
                if number==0:
                    print '\t\t%-70s %10s %10s' %( dir_d,number,'scrapy_failure'  )
                    error_url_messages = open('error_urls.txt','a')
                    error_url_messages.write('%-70s %10s %10s'%( dir_d,number,' scrapy_failure\n'  ) )
                    error_url_messages.close()
                elif number<10:
                    print '\t\t%-70s %10s %10s' %( dir_d,number,'too_small'  )
                    error_url_messages = open('error_urls.txt','a')
                    error_url_messages.write('%-70s %10s %10s'%( dir_d,number,' too_small\n'  ) )
                    error_url_messages.close()
                else:
                    print '\t\t%-70s %10s' %( dir_d,number  )
                all_total_number += number
                if date_number_dict.has_key(dir_c):
                    date_number_dict[dir_c]+=number
                else:
                    date_number_dict[dir_c]=number
    print '-'*33
    print '%-20s %10s' %('目录总数(manufacturers)：',all_dir_number)
    print '%-20s %10s' %('文件总数:',all_total_number)
    ##总all_urls 清点
    print 'urls总数 : ',len(urls.all_urls)
    ##错误或者异常urls数
    ##print 'urls错误或异常数：%s'%( error_urls() )
    ##print '',
    ##完全无效urls 数
    print 'urls完全无效数 ：%s '%(  len(urls.all_urls)-all_dir_number )
    ##print 'urls有效数：绝对数值，相对数值\n %s  %s\n',all_dir_number-error_urls(),(all_dir_number-error_urls())/len(urls.all_urls)
    print '日文件数(字典): \n',date_number_dict


print '\n\n'

##en=error_urls()
##print 

error_urls_file='error_urls.txt'
print 'urls错误或异常数：%s'%( get_number_from_errorfile( error_urls_file ) )


####
director = '/data/news_data'
all_filenames , all_hashs = [], []
get_filename(director,all_filenames,all_hashs)
print 'len(all_filenames) : ',len(all_filenames)
print 'len(all_hashs) : ',len(all_hashs)
