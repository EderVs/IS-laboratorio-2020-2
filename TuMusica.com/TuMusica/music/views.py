"""Music Views."""
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Music index.

    Showing some artists, songs, albums and playlists.
    TODO: Show artists.
    TODO: Show songs.
    TODO: Show albums.
    TODO: Show playlists.
    """
    return HttpResponse("<h1>This is the music index!<!h1>")
