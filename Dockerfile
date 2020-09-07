FROM python:3

ENV PYTHONUNBUFFERED 1
MAINTAINER Edwin C

RUN mkdir /code
WORKDIR /code

RUN easy_install pip

ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt --proxy=http://user:pass@addr:port