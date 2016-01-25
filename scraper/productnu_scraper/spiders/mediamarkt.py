# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MediamarktSpider(CrawlSpider):
    name = "mediamarkt"
    allowed_domains = ["mediamarkt.nl"]
    start_urls = (
        'http://www.mediamarkt.nl/',
        'http://www.mediamarkt.nl/mcs/productlist/_Laptops,10259,512030.html?langId=-11&searchParams=&sort=&view=&page=1',
    )

    rules = (Rule(LinkExtractor(allow=()), callback='test_me', follow=True))

    def test_me(self, response):
        self.logger.debug(response)
        return

    def parse(self, response):
        pass
