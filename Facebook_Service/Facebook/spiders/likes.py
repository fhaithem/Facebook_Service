import scrapy
from scrapy.http import Request, FormRequest 
from .Selenium import Selenium
from scrapy.selector.unified import Selector
from Facebook.items import FacebookItem
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch


es = Elasticsearch()
settings = {
    "settings": {
        "index.max_result_window": 100000
    }
}
es.indices.create(index='facebook_service', ignore=400, body=settings)


class FacebookSpider(scrapy.Spider): 

    """Get informations (name+url) about a user's pages"""

    name = 'facebook_likes'
    start_urls  = ['https://www.facebook.com/haithem.frad.54/']
    

    def parse(self, response):
        driver = Selenium()
        driver.login()        
        _driver = driver.navigate('https://www.facebook.com/haithem.frad.54/likes')  
        res = _driver.page_source.encode('utf-8')
        response = Selector(text = res)
        items = FacebookItem()
        li = []
        #Scroll to end 
        driver.scroll_to_end()
        driver.sleep(3)
        #Get new response after scroll
        _driver = driver.get_driver()
        res = _driver.page_source.encode('utf-8')
        response = Selector(text = res)
        links = response.xpath("//a[@class ='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']/@href").extract()
        texts = response.xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p oo9gr5id hzawbc8m']/text()").extract()
        for link,text in zip(links, texts):
            dic = {"name": text, "link": link}
            li.append(dic)
        items['likes'] = li
        yield items
        