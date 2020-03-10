"""Music Models"""
from django.db import models


class Artist(models.Model):
    """Artist Model."""

    name = models.CharField(max_length=200)

    def __str__(self):
        """Get str representation."""
        return self.name

    def __repr__(self):
        """Get str representation."""
        return self.__str__()


def song_directory_path(instance, filename):
    """Get song directory path to save."""
    return f"music/songs/{instance.id}_{instance.name}_{filename}"


class Song(models.Model):
    """Song Model."""

    name = models.CharField(max_length=200)
    song_file = models.FileField(null=True, upload_to=song_directory_path)

    # Relations
    artists = models.ManyToManyField("music.Artist", related_name="songs")

    def __str__(self):
        """Get str representation."""
        artists_str = ""
        artists = list(self.artists.all())
        if len(artists) == 0:
            return f"{self.name}"
        artists_str = f"{artists[0].name}"
        for artist in artists[1:]:
            artists_str += f", {artist.name}"
        return f"{self.name} by {artists_str}"

    def __repr__(self):
        """Get str representation."""
        return self.__str__()
