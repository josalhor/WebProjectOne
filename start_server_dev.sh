#!/bin/sh

python /app/src/manage.py makemigrations
python /app/src/manage.py migrate
python manage.py collectstatic --no-input
/app/start_server.sh