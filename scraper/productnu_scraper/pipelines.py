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
        payload = json.dumps(dict(item))
        r = requests.post(url, json=payload)
        return r.text