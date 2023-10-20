#!/bin/bash

set -e

if [[ "${MIGRATION_ENABLED}" == "true" ]]; then
  echo "Running migrations"
  flask db upgrade
fi


if [[ "${DEBUG}" == "true" ]]; then
  flask run --host=${SERVER_BIND_ADDRESS:-0.0.0.0} --port=${SERVER_PORT:-5000} --debug
else
  gunicorn \
    --bind "${SERVER_BIND_ADDRESS:-0.0.0.0}:${SERVER_PORT:-5000}" \
    --workers ${SERVER_WORKER_AMOUNT:-1} \
    --worker-class ${SERVER_WORKER_CLASS:-gevent} \
    --timeout ${GUNICORN_TIMEOUT:-200} \
    --preload \
    app:app
fi

