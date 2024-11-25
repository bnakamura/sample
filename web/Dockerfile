FROM python:3.11

RUN mkdir -p /var/www/html/
COPY requirements.txt /var/www/html/
COPY uwsgi.ini /var/www/html/

COPY app.py /var/www/html/
WORKDIR /var/www/html/

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt