# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import requests
import json

class ProductnuScraperPipeline(object):
    def process_item(self, item, spider):
        url = 'http://198.199.125.55:3000/product/'
        payload = {
            'description': item['description'],
            'ean': item['ean'],
            'price': item['price'],
            'supply': item['supply'],
            'name': item['name'],
            'retailer_alias': item['retailer_alias'],
            'product_page': item['product_page'],
        }

        r = requests.post(url, json=payload)
        return r.text