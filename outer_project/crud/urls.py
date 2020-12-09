from django.urls import path
from .api import CrudApiList
from .api import CrudCreateApi

urlpatterns = [
    path('api/', CrudApiList.as_view()),
    path('api/create', CrudCreateApi.as_view()),

]