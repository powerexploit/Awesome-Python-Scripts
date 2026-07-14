import scrapy
from ..items import ImdbItem

class ImdbspiderSpider(scrapy.Spider):
    name = 'top_rated_movies_spider'
    allowed_domains = ['www.imdb.com/chart/top/?ref_=nv_mv_250']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250/']

    def parse(self, response):
        item = ImdbItem()

        cards = response.css('.titleColumn')
        for card in cards:
            name = card.css('a::text').extract_first()
            year = card.css('.secondaryInfo::text').extract_first()
            year = year.replace("(","").replace(")","")
            year = int(year)
            category = "top rated movies"
            #rating = 
            item['movie_name'] = name
            item['movie_year'] = year
            item['category'] = category
            #items[movie_rating] = rating   

            yield item    
    
    