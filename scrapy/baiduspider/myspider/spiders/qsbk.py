# -*- coding: utf-8 -*-
import scrapy
import json

class QsbkSpider(scrapy.Spider):
    name = 'zhihu'
    #allowed_domains = ['quotes.toscrape.com']
    #start_urls = ['http://quotes.toscrape.com/page/1/']
    #start_urls = ['https://movie.douban.com/chart']
    start_urls = ['https://www.baidu.com/s?wd=xpath&rsv_spt=1&rsv_iqid=0x8543f70f0010ec41&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=7&rsv_sug1=12&rsv_sug7=100&rsv_sug2=0&inputT=37999&rsv_sug4=37999']

    def parse(self, response):
        #open('wangyiyun','wb').write(response.body)
        music = response.xpath('//div[@class = "c-row c-gap-top"]//div[contains(@class, "opr-recommends-merge-item")]/div[contains(@class, "c-gap-top-small")]/a/text()').extract()
        #print(response.body)
        #print(music)
        for item in music:
            print(item)
        #for quote in response.css('div.hd'):
            #print(quote.css('span.title::text').extract_first())
            #yield {'title':quote.css('span.title').extract_first()}
            #open('text', 'wb').write(quote.css('span.text::text').extract_first())
            #yield {'text':quote.css('span.text::text').extract_first('utf-8'),
             #      'author':quote.css('small.author::text').extract_first('utf-8'),}
