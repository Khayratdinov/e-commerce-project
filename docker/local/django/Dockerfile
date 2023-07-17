FROM python:3.9.6-alpine

ENV APP_HOME=/app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip

RUN apk add gettext


COPY ./requirements/base.txt .

RUN pip install -r base.txt

COPY . .

EXPOSE 8000