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

    """Get the name and url of a user's followers"""

    name = 'facebook_followers'
    start_urls  = ["https://www.facebook.com/haithem.frad.54/"]
    

    def parse(self, response):
        driver = Selenium()
        driver.login()        
        driver.navigate("https://www.facebook.com/haithem.frad.54/followers") 
        #Scroll to end 
        driver.scroll_to_end()
        #Get new response after scroll
        _driver = driver.get_driver()
        res = _driver.page_source.encode('utf-8')
        response = Selector(text = res)
        items = FacebookItem()
        followers = []
        texts = response.xpath("//div[@class='j83agx80 l9j0dhe7 k4urcfbm']/descendant-or-self::*/a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']//text()").extract()
        links = response.xpath("//div[@class='j83agx80 l9j0dhe7 k4urcfbm']/descendant-or-self::*/a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']/@href").extract()
        for i,j in zip (texts, links):
            text = i
            link = j
            follower = {'name': i, 'link': j}
            followers.append(follower)
        items['followers'] = followers
        print(followers)
        yield items