#!/bin/sh

if [[ -z "${PORT}" ]]; then
  # some sensible default value
  PORT=80
fi

cd /app/src/

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear

gunicorn -b 0.0.0.0:$PORT webproject.wsgi --log-file -
