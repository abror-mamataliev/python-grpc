FROM python:3.12-alpine

WORKDIR /srv/app

COPY requirements.txt /srv/app
RUN python -m pip install -U pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . /srv/app

EXPOSE 5000
