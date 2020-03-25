"""Users models."""
# Django
from django.db import models
from django.contrib.auth.models import User

# Models
from music.models import Song


class ExtendedUser(models.Model):
    """Extended user to save fav songs and playlists."""

    user = models.OneToOneField(
        User, related_name="extended_user", on_delete=models.CASCADE
    )
    fav_songs = models.ManyToManyField(
        "music.Song", related_name="users_fav", blank=True
    )

    def __str__(self):
        """Get string representation."""
        return f"User({self.user.id} {self.user.first_name})"

    def __repr__(self):
        """Get representation."""
        return self.__str__()
