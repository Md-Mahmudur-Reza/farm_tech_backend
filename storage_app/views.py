from django.shortcuts import render
from .models import Storage
from .serializers import StorageSerializers
from rest_framework.response import Response
from rest_framework import generics


class StorageLists(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializers