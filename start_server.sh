#!/bin/sh

if [[ -z "${PORT}" ]]; then
  # some sensible default value
  PORT=80
fi

cd /app/src/

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear

if [ -n "$DEF_ADMIN" -a -n "$DEF_PASS" ]; then
  echo "Creating Default Admin"
  python manage.py ensure_adminuser --username=$DEF_ADMIN \
    --email=admin@example.com \
    --password=$DEF_PASS
fi

gunicorn -b 0.0.0.0:$PORT webproject.wsgi --log-file -
