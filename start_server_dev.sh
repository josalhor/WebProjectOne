#!/bin/sh

python /app/src/manage.py makemigrations
python /app/src/manage.py migrate
/app/start_server.sh