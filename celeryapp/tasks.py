from celery import task
import subprocess
import os

@task
def start_scraper(*args, **kwargs):
    # print("start")
    os.chdir("scraper/productnu_scraper/spiders/")
    os.getcwd()
    os.system('scrapy runspider laptopshop.py')

    # subprocess.call("./foo.sh", shell=True)
    # print("end")
    # os.system('cd scraper/productnu_scraper/spiders/')
    # os.system('ls')
    # os.system('scrapy runspider laptopshop.py')