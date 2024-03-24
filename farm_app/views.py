from django.shortcuts import render
from rest_framework import generics
from .models import ExtendedUser, FarmerDetail, Land, LandApplication
from .serializers import ExtendedUserSerializers, FarmerDetailSerializers, LandSerializers, LandApplicationSerializers, UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth import authenticate, login

class UserRegistrationView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                login(request, user)
                return Response({"message": "User logged in successfully."})
            return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    

class LandApplicationLists(generics.ListCreateAPIView):
    queryset = LandApplication.objects.all()
    serializer_class = LandApplicationSerializers

class LandApplicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandApplicationSerializers

    def get_queryset(self):
        user = self.request.user
        return Land.objects.filter(extendeduser__user = user)