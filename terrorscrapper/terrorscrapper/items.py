# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TerrorscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TerrorItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    reward = scrapy.Field()
    associated_organization = scrapy.Field()
    associated_location = scrapy.Field()
    about = scrapy.Field()
    image_url = scrapy.Field()
    dob = scrapy.Field()
    
    