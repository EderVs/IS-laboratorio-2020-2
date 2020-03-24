"""Music URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from music import views

app_name = "music"
urlpatterns = [
    # Function-based views
    #     path('', views.index, name='home'),
    #     path('top-songs', views.top_songs, name='top-songs'),
    # Class-based views
    path("", views.IndexView.as_view(), name="home"),
    path("top-songs", views.TopSongsView.as_view(), name="top-songs"),
    path("artist/<int:id>", views.ArtistView.as_view(), name="artist"),
]
