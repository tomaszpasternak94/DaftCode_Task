from rest_framework import generics
from rest_framework.response import Response
from .serializer import CrudSerializer
from .models import Crud

class CrudCreateApi(generics.CreateAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer

class CrudApiList(generics.ListAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer

class CrudUpdateApi(generics.RetrieveAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer

class CrudDeleteApi(generics.DestroyAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer