# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9.12

WORKDIR /code

ADD . /code

COPY ./requirement.txt /app/requirement.txt
 
RUN pip install -r requirement.txt

COPY . /code/

