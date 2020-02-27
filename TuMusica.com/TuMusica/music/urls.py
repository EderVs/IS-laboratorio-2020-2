"""Music URL configuration."""
from django.contrib import admin
from django.urls import include, path
# Views
from music import views

urlpatterns = [
    path('', views.index, name='home')
]
