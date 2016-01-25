from subprocess import call
from celery import app

@app.task
def start_scraper(*args, **kwargs):
    call("scraper/scrapy runspider spiders/laptopshop.py")