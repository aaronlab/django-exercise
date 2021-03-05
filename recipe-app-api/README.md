# Recipe App Api

Recipe App Api

## Docker

Make [`DockerFile`](Dockerfile)

```commandline
docker build .
```

Make [`docker-compose.yml`](docker-compose.yml)

```commandline
docker-compose build
```

Docker + Pycharm 자동완성 해결([링크](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html))

## Create Django project

```commandline
docker-compose run <APP_NAME> sh -c "django-admin.py startproject app ."
```

## Test

```python
from django.test import TestCase
```

- Inherit TestCase

```commandline
docker-compose run app sh -c "python manage.py test"
```

## Create Core App

```commandline
docker-compose run app sh -c "python manage.py startapp core"
```

no needs to have test.py + views.py in core app

add 'core' app in `INSTALLED_APPS` of the setting file

## User Model

**extra_fields: any args

## Postgres

> in `docker-compose.yml`

- in the same scope level with app

    ```text
    db:
        image: postgres:10-alpine
        environment:
          - POSTGRES_DB=app
          - POSTGRES_USER=postgres
          - POSTGRES_PASSWORD=supersecretpassword
    ```

- in the app

    ```text
    environment:
          - DB_HOST=db
          - DB_NAME=app
          - DB_USER=postgres
          - DB_PASS=supersecretpassword
        depends_on:
          - db
    ```

> in `requirements.txt`
  
  ```text
  psycopg2>2.7.5,<2.8.0
  ```

> in `Dockerfile`
 
- before `pip install`

  ```dockerfile
  RUN apk add --update --no-cache postgresql-client
  RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
  ```
  
- after `pip install`

  ```dockerfile
  RUN apk del .tmp-build-deps
  ```
  
```commandline
docker-compose build
```

