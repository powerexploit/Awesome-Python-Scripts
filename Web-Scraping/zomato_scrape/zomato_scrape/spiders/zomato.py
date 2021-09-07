import scrapy
from ..items import ZomatoScrapeItem
from urllib.request import Request


class ZomatoSpider(scrapy.Spider):
    name = 'zomato'
    # allowed_domains = ['www.zomato.com/ahmedabad/gandhinagar-restaurants']
    start_urls = ['https://www.zomato.com/ahmedabad/gandhinagar-restaurants?page=1']
    page_no = 2
    def parse(self, response):
        item = ZomatoScrapeItem()

        cards = response.css('#orig-search-list .content')
        for card in cards:
            
            name_ = card.css('.fontsize0::text').extract_first()
            name = name_.split('\n')[0]
            
            address = card.css('b::text').extract_first()
            cost_per_two =  card.css('.res-cost .pl0::text').extract_first()
            
            timings_ = card.css('.res-timing .search-grid-right-text::text').extract_first()
            timings = timings_.split('\n')[1].lstrip()
            
            category = card.css('.fontsize6::text').extract_first()
            
            cusine_list =  card.css('.nowrap.pl0 a::text').extract()
            cusine = ",".join(cusine_list)
            
            detailed_address = card.css('.ln22::text').extract_first()
            featured_in = card.css('.res-collections .search-grid-right-text a::text').extract()
            featured_in = ",".join(featured_in)
            
            discount = card.css('.zgreen::text').extract_first()
            if discount is not None:
                discount = discount.split('\n')[1].lstrip()

            item['name'] = name
            item['address'] = address
            item['cost_per_two'] = cost_per_two
            item['timings'] = timings
            item['category'] = category
            item['cusine'] = cusine
            item['detailed_address'] = detailed_address
            item['featured_in'] = featured_in
            item['discount'] = discount
            
            yield item  
        
        # next_page = response.css('.paginator_item::attr(href)').get()
        # if next_page is not None:
            # yield response.follow(next_page,callback = self.parse)

        
    
        next_page = "https://www.zomato.com/ahmedabad/gandhinagar-restaurants?page="  + str(self.page_no)
        print("Page No currently going to crawl :",self.page_no)
        self.page_no += 1
        
        yield scrapy.Request(next_page, callback=self.parse)
        