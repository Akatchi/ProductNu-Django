FROM django:onbuild

RUN apt-get install -y libmysqlclient-dev
