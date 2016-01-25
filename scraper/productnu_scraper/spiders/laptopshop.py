# -*- coding: utf-8 -*-
import scrapy

from productnu_scraper.items import ProductnuScraperItem #FUK U

class LaptopshopSpider(scrapy.Spider):
    name = "laptopshop"
    allowed_domains = ["www.laptopshop.nl"]
    start_urls = ('http://www.laptopshop.nl', 'http://www.laptopshop.nl/category/45702/laptops.html')

    def parse(self, response):
        for productBox in response.xpath('//div[@class="shop-content"]/div[contains(@class, "layout-content")]/div[@id="layout_content"]/div[@id="facet_productlist"]/div[@id="specification_results"]/div[contains(@class, "product-list")]/ul/li[contains(@class, "product-list-item")]'):
            """ get the url for the product page and enter it."""
            for productUrl in productBox.xpath('//h2/a/@href').extract():
                url = response.urljoin(productUrl)
                yield scrapy.Request(url, callback=self._parse_product_page)

        """ see if there is pagination """
        next_page = response.xpath('//div[@class="productlist_footer_container"]/div[@class="paging-footer"]/div[@class="paging-old"]/div[contains(@class, "paging-navigation")]/a[contains(@class, "next")]/@href').extract()

        """ if there is pagination """
        if next_page:
            """ enter next page """
            next_page_url = response.urljoin(next_page[0])
            self.logger.info(next_page_url)
            """ make request again """
            yield scrapy.Request(next_page_url, callback=self.parse)

    def _parse_product_page(self, response):

        #general product specs
        product_specs = response.xpath('//div[@class="product-specs"]/div[contains(@class, "is-collapsable")]/div[@class="collapse-content"]')

        #grab the product title
        product_title = response.xpath('//span[contains(@class, "js-product-name")]/text()').extract()[0].strip()

        # see if the product is in stock
        product_stock = response.xpath('//div[contains(@class, "product-order")]/div[contains(@class, "product-order--offer")]//div[contains(@class, "availability-state")]/span[contains(@class, "availability-state--on-stock")]').extract()

        #grab the item description
        product_description = ''.join(response.xpath('//div[contains(@class, "product-description--content")]//text()').extract()).strip()

        #grab the price
        product_price = response.xpath('//div[contains(@class, "product-order")]/div[contains(@class, "product-order--information")]//div[@class="sales-price"]/strong[@class="sales-price--current"]/text()').extract()[0].strip()[:-1]

        #start building the product item
        #wauw
        product = ProductnuScraperItem()
        product['name'] = product_title
        product['retailer_alias'] = 'coolblue'
        product['supply'] = True if product_stock else False
        product['description'] = product_description
        product['product_page'] = response.url
        product['price'] = product_price
        product['ean'] = '' # no ean

        #return the product
        yield product
