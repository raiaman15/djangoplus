FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip

RUN addgroup --system django \
    && adduser --system --ingroup django django

RUN mkdir /app
RUN chown -R django /app/
WORKDIR /app

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local/requirements.txt

COPY ./compose/local/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/local/django/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

USER django
COPY . /app/

ENTRYPOINT ["/entrypoint.sh"]