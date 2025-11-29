#!/bin/bash

set -e

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput --clear

echo "=== Running migrations ==="
python manage.py migrate --noinput

echo "=== Populating database ==="
python manage.py populate_db

echo "=== Build completed successfully ==="
