FROM python:3.6.10-buster as building

RUN adduser runner
RUN mkdir /app

RUN apt-get update
# Pillow dependencies
RUN apt-get -y install python3-dev python3-setuptools libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev
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

#Source: https://github.com/SeleniumHQ/docker-selenium/blob/797cadb0320e43726846a61f79e5f8da1f51f585/NodeChrome/Dockerfile
ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

ARG CHROME_DRIVER_VERSION
RUN if [ -z "$CHROME_DRIVER_VERSION" ]; \
  then CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
    && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}"); \
  fi \
  && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

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
