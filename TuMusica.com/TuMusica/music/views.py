"""Music Views."""
# Django
from django.shortcuts import render
from django.views import View


# Function-based views.
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


# Class-based views.
class Index(View):
    """Music index.

    Showing some artists, songs, albums and playlists.
    TODO: Show artists.
    TODO: Show songs.
    TODO: Show albums.
    TODO: Show playlists.
    """

    template = "music/index.html"

    def get(self, request):
        """GET method."""
        return render(request, self.template)


class TopSongs(View):
    """Top songs.

    TODO: Show songs by its popularity.
    """

    template = "music/top_songs.html"

    def get(self, request):
        """GET method."""
        return render(request, self.template)
