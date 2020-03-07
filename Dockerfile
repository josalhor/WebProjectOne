FROM python:3.6.10-alpine3.11

RUN mkdir /app

# TODO: why was it a good idea to copy first the requirements?
COPY requirements.txt /app/requirements.txt

# TODO do we need trusted sources here?
RUN pip install -r /app/requirements.txt

COPY . /app

# this will only take effect on Heroku that exposes
# this variable so that it can router our requests
EXPOSE $PORT

CMD /app/start_server.sh
