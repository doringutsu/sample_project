FROM python:3.7.5-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade --no-cache-dir pip
RUN apk add --no-cache postgresql-dev build-base libffi-dev libxml2-dev libxslt-dev git
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app
RUN pip install -e .
