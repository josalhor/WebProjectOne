#!/bin/bash

echo "Trying to start web server..."

rm -f /app/db.sqlite3

chmod +x /app/start_server.sh
chmod +x /app/start_server_dev.sh

secrets_web_file="/app/web.env.secrets.sh"

if [[ -z "${NYT_API_KEY}" ]]; then
  if [ -f "${secrets_web_file}" ]; then
    . ${secrets_web_file}
  fi
  if [[ -z "${NYT_API_KEY}" ]]; then
    echo "NYT_API_KEY env variable not set"
    exit -1
  fi
fi

if [[ -z "${PORT}" ]]; then
  # some sensible default value
  PORT=8080
fi

cd /app/

# Note, when the app is finished this will be considered
# Admin actions that will be need to be taken a side

# Useful when the models are changing but not useful anymore:
# python manage.py reset_db --noinput
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

if [[ -z "${TESTING}" ]];
then
  gunicorn -b 0.0.0.0:$PORT webproject.wsgi --log-file -
else
  echo "Starting Behave testing"
  python manage.py behave
fi

