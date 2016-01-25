#!/bin/sh

./manage.py celery worker

#cd main
# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
#su -m myuser -c "celery worker -A celery -Q default -n default@%h"