from scrapy import signals

from itemadapter import is_item, ItemAdapter


class AmazonReviewsScrapingSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        
        return None

    def process_spider_output(self, response, result, spider):
        
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        
        pass

    def process_start_requests(self, start_requests, spider):
        
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AmazonReviewsScrapingDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        
        return None

    def process_response(self, request, response, spider):
        
        return response

    def process_exception(self, request, exception, spider):
        
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
