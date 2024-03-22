from django.shortcuts import render
from rest_framework import generics
from .models import ExtendedUser, FarmerDetail, Land
from .serializers import ExtendedUserSerializers, FarmerDetailSerializers, LandSerializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


class ExtendedUserLists(generics.ListCreateAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializers
    # permission_classes = [permissions.IsAuthenticated]


class ExtendedUserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ExtendedUserSerializers
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ExtendedUser.objects.filter(user = user)
    
class FarmerLists(generics.ListCreateAPIView):
    queryset = FarmerDetail.objects.all()
    serializer_class = FarmerDetailSerializers
    # permission_classes = [permissions.IsAuthenticated]


class FarmerRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = FarmerDetailSerializers
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FarmerDetail.objects.filter(extendeduser__user = user)


class LandLists(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializers
    # permission_classes = [permissions.IsAuthenticated]



class LandRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandSerializers
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Land.objects.filter(extendeduser__user = user)