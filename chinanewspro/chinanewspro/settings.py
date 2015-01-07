# -*- coding: utf-8 -*-

# Scrapy settings for chinanewspro project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'chinanewspro'

SPIDER_MODULES = ['chinanewspro.spiders']
NEWSPIDER_MODULE = 'chinanewspro.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'chinanewspro (+http://www.yourdomain.com)'

ITEM_PIPELINES=['chinanewspro.pipelines.ChinanewsproPipeline']
