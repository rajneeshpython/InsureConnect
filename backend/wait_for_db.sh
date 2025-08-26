#!/bin/sh
set -e

echo "Waiting for Postgres at $POSTGRES_HOST:$POSTGRES_PORT..."

until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

>&2 echo "Postgres is up - executing command"

case "$1" in
  web)
    python manage.py migrate
    exec gunicorn insureconnect.wsgi:application --bind 0.0.0.0:8000
    ;;
  worker)
    exec celery -A insureconnect worker --loglevel=info
    ;;
  beat)
    exec celery -A insureconnect beat --loglevel=info
    ;;
  *)
    echo "Unknown argument: $1"
    exit 1
    ;;
esac
