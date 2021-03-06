# Django

Django

## Create project

```commandline
django-admin startproject <PROJECT_NAME>
```

## Crate app

```commandline
python manage.py startapp <APP_NAME>
```

## settings.py

- `ALLOWED_HOSTS`: When the server is not debug mode

- `INSTALLED_APPS`: Included apps

- `TIME_ZONE = 'Asia/Seoul'`

- `USE_TZ = False`

## Migrate basic table

```commandline
python manage.py migrate
```

## Run server

```commandline
python manage.py runserver --noreload
```

## Create Super User

```commandline
python manage.py createsuperuser
```

## Make models & Migrate

- [Model file](ch3_recap/polls/models.py)

- Register in [admin.py](ch3_recap/polls/admin.py)

- makemigrations

```commandline
python manage.py makemigrations
python manage.py migrate
```

## URLconf

- Add urls
    
    - [main](ch3_recap/mysite/urls.py)
    - [app](ch3_recap/polls/urls.py)
  
## Make templates + Views
