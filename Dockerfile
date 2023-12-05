FROM python:3.11.3
ENV PYTHONUNBUFFERED 1
WORKDIR /notificationapp
RUN pip install psycopg2
COPY requirments.txt /notificationapp/requirments.txt
RUN pip install -r requirments.txt
COPY . /notificationapp/