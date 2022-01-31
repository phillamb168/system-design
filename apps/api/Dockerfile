# Stuck with 3.7 due to psycopg2
FROM python:3.7-alpine AS builder
WORKDIR /opt/api
COPY ./ .
RUN apk update && apk add mysql-client && rm -f /var/cache/apk/*
RUN apk add --virtual .build-deps gcc musl-dev g++
RUN pip install -r requirements-dev.txt

FROM python:3.7-alpine
WORKDIR /opt/api
RUN apk update && apk add mysql-client && rm -f /var/cache/apk/*
RUN apk add --virtual .build-deps gcc musl-dev g++
COPY ./quipper/ ./quipper/
COPY ./setup.py .
RUN pip install .

EXPOSE 80

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "80", "--app-dir", "/opt/api/quipper", "--reload", "main:app"]
