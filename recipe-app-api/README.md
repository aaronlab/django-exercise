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

## Create Django project

```commandline
docker-compose run <APP_NAME>
docker-compose run app sh -c "django-admin.py startproject app ."
```
