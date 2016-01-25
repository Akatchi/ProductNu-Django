from celery import task
import os

@task
def start_scraper(*args, **kwargs):
    os.chdir("scraper/productnu_scraper/spiders/")
    os.getcwd()
    os.system('scrapy runspider laptopshop.py')