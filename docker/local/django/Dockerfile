FROM python:3.9.6-alpine

# copy project
COPY . /usr/src/app

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements /usr/src/app/requirements/
RUN pip install -r requirements/base.txt

