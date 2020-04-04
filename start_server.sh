#!/bin/sh

if [[ -z "${PORT}" ]]; then
  # some sensible default value
  PORT=8080
fi

pip freeze > /app/frozen_requirements.txt

cd /app/

# Note, when the app is finished this will be considered
# Admin actions that will be need to be taken a side
python manage.py reset_db --noinput
python manage.py makemigrations
python manage.py makemigrations book_visualizer
python manage.py migrate
python manage.py collectstatic --no-input --clear


if [ -n "$DEF_ADMIN" -a -n "$DEF_PASS" ]; then
  echo "Creating Default Admin"
  python manage.py ensure_adminuser --username=$DEF_ADMIN \
    --email=admin@example.com \
    --password=$DEF_PASS
fi

python manage.py request_categories

gunicorn -b 0.0.0.0:$PORT webproject.wsgi --log-file -
