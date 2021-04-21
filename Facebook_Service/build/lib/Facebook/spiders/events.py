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

    """Get informations about a user's events"""

    name = 'facebook_events'
    start_urls  = ['https://www.facebook.com/haithem.frad.54/']
    

    def parse(self, response):
        driver = Selenium()
        driver.login()        
        driver.navigate('https://www.facebook.com/haithem.frad.54/events')  
        #Scroll to end 
        driver.scroll_to_end()
        driver.sleep(3)
        #Get new response after scroll
        _driver = driver.get_driver()
        res = _driver.page_source.encode('utf-8')
        response = Selector(text = res)
        items = FacebookItem()
        data = []
        
        # list of events
        links = response.xpath(
            "//a[@class ='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 wkznzc2l oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l pioscnbf etr7akla']/@href").extract()
        for link in links:
            _driver = driver.navigate(str(link))  
            res = _driver.page_source.encode('utf-8')
            response = Selector(text = res)
            
            name = response.xpath("//span[@class ='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 pby63qed']/span/text()").extract_first()
            try:
                nb_people_participated = response.xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 ns63r2gh fe6kdd0r mau55g9w c8b282yb iv3no6db o3w64lxj b2s5l15y hnhda86s oo9gr5id oqcyycmt']/text()").extract()[0]
            except:
                nb_people_participated = ''
            try:
                nb_people_interested = response.xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 ns63r2gh fe6kdd0r mau55g9w c8b282yb iv3no6db o3w64lxj b2s5l15y hnhda86s oo9gr5id oqcyycmt']/text()").extract()[1]
            except:
                nb_people_interested = ''
            
            dic = {"name": name, "nb_people_interested": nb_people_interested, "nb_people_participated": nb_people_participated}
            data.append(dic)

        items['events'] = data
        yield items
        
            