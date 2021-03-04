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
docker-compose run app sh -c "python manage.py <TEST_FILE_NAME>"
```

## Create Core App

```commandline
docker-compose run app sh -c "python manage.py startapp core"
```

no needs to have test.py + views.py in core app
