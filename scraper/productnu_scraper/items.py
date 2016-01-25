# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ProductnuScraperItem(scrapy.Item):
    # define the fields for your item here like:
    manufacturer_code = scrapy.Field()
    ean = scrapy.Field()
    description = scrapy.Field()
    product_page = scrapy.Field()
    name = scrapy.Field()
    supply = scrapy.Field()
    price = scrapy.Field()
    retailer_alias = scrapy.Field()
    # name = scrapy.Field()
    # desc = scrapy.Field()