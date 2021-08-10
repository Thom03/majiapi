 # pull official base image
 FROM python:3.7-alpine
 MAINTAINER George Thomas Muteti

# set work directory
WORKDIR /usr/src/app
#  set environment variables
 ENV PYTHONUNBUFFERED 1
 ENV PYTHONDONTWRITEBYTECODE 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
 COPY ./requirements.txt .
 RUN pip install -r requirements.txt


# copy the project
#RUN mkdir /app
#WORKDIR /app
 COPY ..


