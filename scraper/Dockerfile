FROM ubuntu:wily

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7 && \
    echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | tee /etc/apt/sources.list.d/scrapy.list && \
    apt-get update && apt-get install -y scrapy python-pip

# Upgrade PIP this way to latest version. Apt version is for getting all the depts.
RUN easy_install pip

RUN pip install requests==2.8.1
RUN pip install celery[redis]==3.1.19

COPY . /usr/src/app
WORKDIR /usr/src/app/scraper