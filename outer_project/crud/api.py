from rest_framework import generics
from rest_framework.response import Response
from .serializer import CrudSerializer
from .models import Crud

class CrudCreateApi(generics.CreateAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer