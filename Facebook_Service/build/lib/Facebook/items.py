# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FacebookItem(scrapy.Item):
    name = scrapy.Field()
    user_description = scrapy.Field()
    friends = scrapy.Field()
    profile_pic = scrapy.Field()
    cover_pic_url = scrapy.Field()
    photos = scrapy.Field()
    followers = scrapy.Field()
    events = scrapy.Field()
    likes = scrapy.Field()
   
