import scrapy
import re
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls =[
            'http://www.dianping.com/shop/50464594',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        print(response.xpath('//span[@id="reviewCount"]/text()').re(r'1801(.*?)$'))




