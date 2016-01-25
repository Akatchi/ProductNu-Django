FROM python:2.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app

RUN apt-get install -y libmysqlclient-dev


# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

RUN chmod +x ./run_celery.sh