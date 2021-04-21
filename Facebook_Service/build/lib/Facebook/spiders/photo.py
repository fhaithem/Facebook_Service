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

    """Extract user's photos"""
    
    name = 'facebook_photos'
    start_urls  = ['https://www.facebook.com/haithem.frad.54/']
    

    def parse(self, response):
        driver = Selenium()
        driver.login()        
        _driver = driver.navigate('https://www.facebook.com/haithem.frad.54/photos_all')  
        driver.scroll_to_end()
        res = _driver.page_source.encode('utf-8')
        response = Selector(text = res)
        items = FacebookItem()
        url_list = []
        try:
            i = 1
            content = response.xpath("//div[@class='j83agx80 btwxx1t3 lhclo0ds']/div[@class='rq0escxv rj1gh0hx buofh1pr ni8dbmo4 stjgntxs l9j0dhe7']/div/div/a/img/@src").extract()
            for e in content:
                url_list.append({'image': i, 'url': e})
                i += 1
            print(url_list)
            items['photos'] = url_list
        except:
            url_list = []
        yield items