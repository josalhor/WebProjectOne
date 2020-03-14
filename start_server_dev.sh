#!/bin/sh

echo "Creating Default Admin"

python /app/src/manage.py ensure_adminuser --username=DEV_ADMIN \
    --email=admin@example.com \
    --password=DEV_PASS

/app/start_server.sh