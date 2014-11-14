from scrapy.spider import Spider
from scrapy.selector import Selector

#import DmozItem.py
from tutorial.DmozItem  import DmozItem
#from DmozItem.py import DmozItem
#import DmozItem


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        #"http://www.dmoz.org/"
    ]

    def parse(self, response):
#        filename = response.url.split("/")[-2]
#        open(filename, 'wb').write(response.body)
		sel = Selector(response)
		sites = sel.xpath('//ul[@class="directory-url"]/li')
		items = []
		for site in sites:
			#title = site.xpath('a/text()').extract()
			#link = site.xpath('a/@href').extract()
			#desc = site.xpath('text()').extract()
			#print title
			#print title,link,desc
			item = DmozItem();
			item['title'] = site.xpath('a/text()').extract()
			item['link'] = site.xpath('a/@href').extract()
			item['desc'] = site.xpath('text()').extract()
			items.append(item)

		#return  0 
		return  items




