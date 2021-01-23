#!/bin/sh

echo "CHECKING PORT USAGE"
ss -lntu
echo "COLLECTING STATIC FILES"
python manage.py collectstatic --no-input
echo "CLEARING PYTHON COMPILED FILES"
find . -path "*.pyc"  -delete
echo "CLEARING MIGRATION FILES"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
exec "$@"