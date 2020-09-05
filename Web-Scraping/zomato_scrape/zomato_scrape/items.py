# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZomatoScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    address = scrapy.Field()
    cost_per_two = scrapy.Field()
    timings = scrapy.Field()
    category = scrapy.Field()
    cusine =  scrapy.Field()
    detailed_address = scrapy.Field()
    featured_in = scrapy.Field()
    discount = scrapy.Field()
    
