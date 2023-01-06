# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

# install dependencies
RUN pip install --upgrade pip
COPY ./taskmanager/requirements.txt .
RUN pip install -r requirements.txt

# copy project откуда - куда
COPY ./taskmanager .
