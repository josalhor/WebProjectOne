#!/bin/sh

if [[ -z "${PORT}" ]]; then
  # some sensible default value
  PORT=80
fi

gunicorn -b 0.0.0.0:$PORT --chdir /app/src/ webproject.wsgi --log-file -