#!/bin/sh

python /app/src/manage.py makemigrations
python /app/src/manage.py migrate
python /app/src/manage.py collectstatic --no-input
