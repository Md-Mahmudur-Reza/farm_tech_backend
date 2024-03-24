from django.urls import path, include
from  storage_app import views

urlpatterns = [
    path('api/storage', views.StorageLists.as_view()),
]