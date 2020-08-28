# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_year = scrapy.Field()
    category = scrapy.Field()
    #movie_rating = scrapy.Field()

class actorItem(scrapy.Item):
    actor_name = scrapy.Field()
    
