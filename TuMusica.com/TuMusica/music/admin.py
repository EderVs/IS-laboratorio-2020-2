"""Models in Music admin."""
# Django
from django.contrib import admin
# Models
from .models import Song, Artist

admin.site.register(Song)
admin.site.register(Artist)
