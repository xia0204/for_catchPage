# -*- coding: utf-8 -*-
import scrapy
from maitian.items import MaitianItem

class ExampleSpider(scrapy.Spider):
    name = 'guoqi'
    #allowed_domains = ['http://guoqi.work']
    start_urls = ['http://47.105.207.35/']#其实url
    def parse(self, response):#负责解析Downloader通过引擎传回的response
        for item in response.xpath('//header[@class="entry-header"]'):
            result = {
            "name" : item.xpath('h3[@class="entry-title"]/a/text()').extract_first().strip(),
            "url": item.xpath('h3[@class="entry-title"]/a/@href').extract_first().strip(),
            "time":item.xpath('//time[@class="updated"]/text()').extract_first().strip(),
            }
            print(result)
            yield result
        next_page_url = response.xpath('//a[@class="next page-numbers"]/@href').extract()[0]
        print(next_page_url)
        if next_page_url is not None:
            yield scrapy.Request(next_page_url)