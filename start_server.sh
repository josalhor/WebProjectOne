#!/bin/sh

if [[ -z "${PORT}" ]]; then
  # some sensible default value
  PORT=80
fi

python /app/src/manage.py collectstatic --no-input
gunicorn -b 0.0.0.0:$PORT --chdir /app/src/ webproject.wsgi --log-file -
