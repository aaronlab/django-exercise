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

## Model

- Model: AbstractBaseUser, PermissionsMixin

- Manager: BaseUserManager

- settings.py: `MODEL_NAME = '<DIR>.<MODEL_CLASS_NAME>'`

## Create migrations and sync DB

```commandline
vagrant ssh
cd /vagrant
source ~/env/bin/activate
python manage.py makemigrations <APP NAME>
python manage.py migrate
```

## Create super user

```commandline
python manage.py createsupseruser
```

## Enable Django Admin

in the file `admin.py`

```python
from < PACKAGE >
import < MODELS >

admin.site.register( < MODEL_CLASS >)
```

## Test Django Admin

```commandline
python manage.py runserver 0.0.0.0:8000
```

- [http://localhost:8000/admin](http://localhost:8000/admin)

## Create API View

in the file `views.py`

```python
from rest_framework.views import APIView
from rest_framework.response import Response


# then create a class and get method
# e.g.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_api_view = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'api_view': an_api_view})
```

## Configure view URL

in the file `urls.py`

```python
from django.urls import path, include

urlpatterns = [
    path('<PATH>/', include('<PACKAGE_NAME>.urls'))
]
```

in the file `urls.py` in the `package`

```python
from django.urls import path

from profiles_api import views

urlpatterns = [
    path('<PATH>/', views. < API_CLASS(APIView) >.as_view())
]

```

## Infinite reload error

```commandline
python manage.py dbshell
python manage.py runserver 0.0.0.0:8000 --noreload
```

## Serialize

> You can easily understand like this is a kinda form  for data.

```python
from rest_framework import serializers
```

- Inherit `serializers.Serializer` for a  `class`

- And then add `parameters` that you should take from the `post` request.

- Import serializer and declare one in the `class`

- Now, can use it in a method like below
  
```python
# Serializer

from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

# Api    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def post(self, request):
    """Create a hello message with our name"""
    serializers = self.serializer_class(data=request.data)

    if serializers.is_valid():
        name = serializers.validated_data.get('name')
        message = f'Hello, {name}.'
        return Response({'message': message})

    else:
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
```

## Put / Patch / Delete

> `pk` for the argument of the method means the primary key

- You will use `patch` to handle a `partial update` of an object.

- Or you will use `put` to handle a `whole object`. This means that the original object will be replaced.

- You will use `delete` to delete an object.

- To test `patch`, you should use `raw data`, because you need to update particular fields.

## Viewset

> Framework that takes care of a lot of typical logic

- Fastest way to make a database interface

- Simple CRUD interface to the database / Quick & Simple API

## Create simple viewset Example

```python
from rest_framework.response import Response
from rest_framework import viewsets


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
```

## Add URL Router

- in `urls.py` of the package

```python
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from <PACKAGE_NAME> import views

router = DefaultRouter()
router.register('<NAME_OF_URL>', views.<CLASS(viewsets.ViewSet)>, base_name='<RETRIEVE_URL>')

urlpatterns = [
    path('', include(router.urls))
]
```

## How to use viewset

> in `views.py` import `viewsets` and inherit

- Methods

  - list: `GET` all items list
  - create: `POST` create
  - retrieve: `GET` by its primary key(`pk`)
  - update: `UPDATE` by its primary key(`pk`)
  - partial_update: `PATCH` by its primary key(`pk`)
  - destroy: `DELETE` by its primary key(`pk`)
