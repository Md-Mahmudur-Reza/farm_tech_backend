from django.contrib import admin
from django.urls import path, include
from recommendation_app import views


urlpatterns = [
    path('api/recommendation', views.predictor),

]