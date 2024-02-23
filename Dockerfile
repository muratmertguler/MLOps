FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install sudo -y
RUN apt-get update && \
    apt-get install -y build-essential
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip

COPY src/ /bitcoin-forecast/src
COPY data/ /bitcoin-forecast/data
COPY models/ /bitcoin-forecast/models
COPY ./requirements.txt /bitcoin-forecast/requirements.txt
COPY ./ds_app.py /bitcoin-forecast/ds_app.py

WORKDIR /bitcoin-forecast

RUN pip3 install -r requirements.txt
RUN poetry config virtualenvs.create false
#RUN poetry install --no-dev
