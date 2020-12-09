from django.urls import path
from .api import CrudCreateApi

urlpatterns = [
    path('api/create', CrudCreateApi.as_view()),

]