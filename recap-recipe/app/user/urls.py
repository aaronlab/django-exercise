from django.urls import path

from . import views

# for reverse to look up, like the names in urls
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
