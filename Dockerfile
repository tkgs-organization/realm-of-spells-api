FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /api/requirements.txt

ADD . /api/