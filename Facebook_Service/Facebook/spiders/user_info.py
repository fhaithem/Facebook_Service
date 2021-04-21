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


class FacebbokSpider(scrapy.Spider): 
    """Extract user's information"""
    name = 'facebook_info'
    start_urls  = ['https://www.facebook.com/']
    

    def parse(self, response):
        driver = Selenium()
        driver.login()        
        _driver = driver.navigate('https://www.facebook.com/haithem.frad.54/')  
        res = _driver.page_source.encode('utf-8')
        response = Selector(text = res)
        
        #Check response
        """f = open("response.txt", "w")
        f.write(str(res))
        f.close()"""
        items = FacebookItem()

        try:
            name = response.xpath(
                    "//h1[@class='gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl bp9cbjyn j83agx80']/text()").extract_first()
                
        except :
            name = ''
        items['name'] = name

        """try:
            Intro = response.xpath(
                "//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr p8fzw8mz pcp91wgn iuny7tx3 ipjc6fyt']//text()").getall()
            Intro = Intro[:len(Intro)-3]
        except:
            Intro = ''
        items['user_description'] = Intro"""
        try:
            description = response.xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb mdeji52x a5q79mjw g1cxx5fr knj5qynh m9osqain oqcyycmt']/span//text()").getall()
            description = description[:len(description)-1]
        except:
            description = ''
        items['user_description'] = description

        try:
            profile_pic = response.xpath(
                "//div[@class='q9uorilb l9j0dhe7 pzggbiyp du4w35lb']/*").extract()[1]
            soup = BeautifulSoup(profile_pic, 'lxml')
            profile_pic_url = soup.find('image').get('xlink:href')
        except:
            profile_pic_url = ''
        items['profile_pic'] = profile_pic_url

        try:
            cover_pic_url = response.xpath(
                "//div[@class='gs1a9yip ow4ym5g4 auili1gw j83agx80 cbu4d94t buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 tgvbjcpo hpfvmrgz qt6c0cv9 rz4wbd8a a8nywdso jb3vyjys du4w35lb i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4']/img/@src").extract_first()
        except:
            cover_pic_url = ''
        items['cover_pic_url'] = cover_pic_url

        dic = {
            'name': name,
            'Intro': description,
            'profile_pic': profile_pic_url,
            'cover_pic': cover_pic_url
        }
        print(dic)

        yield items
        
    def parse_html_into_text(self, html, position):
        """Get text from html with specific position"""
        soup = BeautifulSoup(html, 'lxml')
        html = soup.find_all('h1')[position].get_text(strip=True)  # Good
        return html

    def parse_html_intro(self, html):
        """Get text from html"""
        txt = BeautifulSoup(html, 'lxml')
        # get text in html and split as list
        # print(txt)
        intro_list = (txt.getText(separator=':')).split(':')
        # intro_list = txt.get_text(strip=True)
        # print(intro_list)
        intro = self.arr

