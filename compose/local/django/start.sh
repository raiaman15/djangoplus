#!/bin/sh

echo "FLUSHING DATABASE"
python manage.py flush --no-input
echo "MAKING MIGRATION FILES"
python manage.py makemigrations --noinput
echo "MIGRATING DATABASE"
python manage.py migrate --noinput
echo "SEEDING DATABASE | REFRESH"
# python manage.py some_seed
echo "RUNNING ALL TEST CASES"
python manage.py test
echo "CREATING TEST SUPERUSER"
echo "from django.contrib.auth import get_user_model; user = get_user_model().objects.create_user('admin@infroid.com', 'DevTeam@123'); user.is_superuser=True; user.is_staff=True; user.save()" | python manage.py shell
echo "STARTING DJANGO BUILT-IN SERVER"
python manage.py runserver 0.0.0.0:8000