"""Music URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from music import views

urlpatterns = [
    path('', views.index, name='home'),
    path('top-songs', views.top_songs, name='top-songs'),
]
