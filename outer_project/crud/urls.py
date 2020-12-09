from django.urls import path
from .api import CrudApiList
from .api import CrudCreateApi
from .api import CrudUpdateApi

urlpatterns = [
    path('api/', CrudApiList.as_view()),
    path('api/create', CrudCreateApi.as_view()),
    path('api/<int:pk>', CrudUpdateApi.as_view()),
]