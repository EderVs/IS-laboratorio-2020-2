"""Music Views."""
# Django
from django.shortcuts import render


def index(request):
    """Music index.

    Showing some artists, songs, albums and playlists.
    TODO: Show artists.
    TODO: Show songs.
    TODO: Show albums.
    TODO: Show playlists.
    """
    template = "music/index.html"
    return render(request, template)


def top_songs(request):
    """Top songs.

    TODO: Show songs by its popularity.
    """
    template = "music/top_songs.html"
    return render(request, template)
