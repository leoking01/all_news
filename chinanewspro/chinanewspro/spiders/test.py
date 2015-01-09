#!/usr/bin/python

import file_check_function

##/data/news_data/all_news
hash1='2546b7f00120921d8813f717f276598b3ac11757'
hash = '129b9f93d492212b960cfaeb267e7de0baedfc13'
a1 = file_check_function.file_check('/data/news_data/all_news','123')

a2 = file_check_function.news_data_check('/data/news_data','123')

b1 = file_check_function.file_check('/data/news_data/all_news',hash )
b2 = file_check_function.news_data_check('/data/news_data',hash)

c=file_check_function.news_data_check('/data/news_data',hash1)
print 'a1,a2,b1,b2 :\n %s %s %s %s %s\n ' %(a1,a2,b1,b2,c)  
print 'b2',b2
