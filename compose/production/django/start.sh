#!/bin/sh

echo "MIGRATING DATABASE"
python manage.py migrate --noinput
echo "SEEDING DATABASE | REFRESH"
# python manage.py some_seed
echo "RUNNING ALL TEST CASES"
python manage.py test
echo "CREATING TEST USERS"
echo "from django.contrib.auth import get_user_model; user = get_user_model().objects.create_user('admin@infroid.com', 'DevTeam@123'); user.is_superuser=True; user.is_staff=True; user.save()" | python manage.py shell
echo "STARTING WSGI GUNICORN SERVER WITH 2 WORKERS 4 THREADS (GTHREAD)"
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers=2 --threads=4 --worker-class=gthread