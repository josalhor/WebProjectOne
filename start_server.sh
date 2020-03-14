#!/bin/sh

if [[ -z "${PORT}" ]]; then
  # some sensible default value
  PORT=80
fi

cd /app/src/

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

gunicorn -b 0.0.0.0:$PORT webproject.wsgi --log-file -
