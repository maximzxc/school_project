FROM python:2.7
MAINTAINER maximzxc
 
ENV PYTHONUNBUFFERED 1
 
RUN apt-get update
RUN apt-get install -y python python-pip python-dev 
RUN apt-get install -y libxml2-dev libxslt-dev libffi-dev libssl-dev 
# RUN apt-get install -y libmysqlclient-dev


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD server/requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
 
# copy the current code
ADD . /usr/src/app/

CMD [ "python", "server/simplefeed/manage.py", "runserver"]
 
EXPOSE 8000
