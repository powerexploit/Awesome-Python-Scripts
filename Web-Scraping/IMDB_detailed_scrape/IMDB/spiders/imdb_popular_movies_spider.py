import scrapy
from ..items import ImdbItem

class ImdbspiderSpider(scrapy.Spider):
    name = 'popular_movies_spider'
    allowed_domains = ['www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=TE15VSHN7TY6H3MAV4B0&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_2']
    start_urls = ['https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=TE15VSHN7TY6H3MAV4B0&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_2']

    def parse(self, response):
        item = ImdbItem()

        cards = response.css('.titleColumn')
        for card in cards:
            name = card.css('a::text').extract_first()
            year = card.css('.secondaryInfo::text').extract_first()
            year = year.replace("(","").replace(")","")
            year = int(year)
            category = 'most popular movies'
            #rating = 
            item['movie_name'] = name
            item['movie_year'] = year
            item['category'] = category
            #items[movie_rating] = rating   

            yield item  