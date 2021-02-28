# Profiles Rest API

## Vagrant

- Init

```commandline
vagrant init ubuntu/bionic64
```

- Up

```commandline
vagrant up
```

- Down

```commandline
vagrant halt
```

- SSH

```commandline
vagrant ssh
cd /vagrant
```

## Python env

- Setup Env

```commandline
python -m venv ~/env
```

- Activate Env

```commandline
source ~/env/bin/activate
```

- Deactivate Env

```commandline
deactivate
```

- Add dependency file

```text
requirements.txt

django==2.2
djangorestframework==3.9.2
```

- Install Dependency

```commandline
pip install -r requirements.txt
```

## Django

- Init project

```commandline
django-admin.py startproject <Project Name> <Location>
```

- Sub Application

```commandline
python manage.py startapp <API NAME>
```

## Setting Files

> settings.py

- Rest Framework: `INSTALLED_APPS`
    - 'rest_framework'
    - 'rest_framework.authtoken'
    - also sub applications too

## Start Server

> should be same with the port in Vagrant

```commandline
python manage.py runserver <IP:PORT>

# ex: python manage.py runserver 0.0.0.0:8000
# localhost:8000
```

## Stop Server

```commandline
ctrl c
```
