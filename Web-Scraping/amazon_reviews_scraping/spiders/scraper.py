import scrapy
 
class AmazonReviewsSpider(scrapy.Spider):
 
    name = 'amazon_reviews'
 
    allowed_domains = ['amazon.in']
 
    myBaseUrl = "https://www.amazon.com/OnePlus-Interstellar-Unlocked-Android-Smartphone/product-reviews/B0872473BF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    start_urls=[]
 
    for i in range(1,121):
        start_urls.append(myBaseUrl+str(i))
 
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
 
            star_rating = data.css('.review-rating')
 
            comments = data.css('.review-text-content')
            count = 0
 
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1
