FROM python:3.6.10-alpine3.11 as building

RUN adduser -D runner
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

RUN chmod +x /app/start_server.sh
RUN chmod +x /app/start_server_dev.sh

FROM building as testing

RUN apk update apk add --no-cache bash \
        alsa-lib \
        at-spi2-atk \
        atk \
        cairo \
        cups-libs \
        dbus-libs \
        eudev-libs \
        expat \
        flac \
        gdk-pixbuf \
        glib \
        libgcc \
        libjpeg-turbo \
        libpng \
        libwebp \
        libx11 \
        libxcomposite \
        libxdamage \
        libxext \
        libxfixes \
        tzdata \
        libexif \
        udev \
        xvfb \
        zlib-dev \
        chromium \
        chromium-chromedriver

ENV PATH="/usr/bin/chromedriver:${PATH}" 

COPY requirements_testing.txt /app/requirements_testing.txt
# TODO do we need trusted sources here?
RUN pip install -r /app/requirements_testing.txt

CMD /app/start_server.sh

FROM building as deploy

# this will only take effect on Heroku that exposes
# this variable so that it can router our requests
EXPOSE $PORT

# Note that for this to work we assume that heroku
# may never give us a port below 1024
# This has to be repeated in the Dockerfile because
# we want to maintin root while installing dependencies
RUN chown -R runner /app/
USER runner

CMD /app/start_server.sh
