FROM python:3.6.10-alpine3.11

RUN mkdir /app

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Pillow dependencies
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

# TODO do we need trusted sources here?
RUN pip install -r /app/requirements.txt

COPY . /app

# this will only take effect on Heroku that exposes
# this variable so that it can router our requests
EXPOSE $PORT

RUN chmod +x /app/start_server.sh
RUN chmod +x /app/start_server_dev.sh

CMD /app/start_server.sh
