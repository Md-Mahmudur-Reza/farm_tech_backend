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


class ExtendedUserLists(generics.ListAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializers
    
class FarmerLists(generics.ListAPIView):
    queryset = FarmerDetail.objects.all()
    serializer_class = FarmerDetailSerializers

class LandLists(generics.ListAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializers
