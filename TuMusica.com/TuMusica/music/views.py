"""Music Views."""
# Django
from django.shortcuts import render, get_object_or_404
from django.views import View

# Models
from .models import Song, Artist


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
class IndexView(View):
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


class TopSongsView(View):
    """Top songs.

    TODO: Show songs by its popularity.
    """

    template = "music/top_songs.html"

    def get(self, request):
        """GET method."""
        songs = Song.objects.all()
        to_play_id = request.GET.get("to_play", 1)
        songs_to_play = Song.objects.filter(id=to_play_id)
        if songs_to_play.count() == 0:
            to_play = Song.objects.first()
        else:
            to_play = songs_to_play.first()

        context = {"songs": songs, "to_play": to_play}
        return render(request, self.template, context)


class ArtistView(View):
    """Show Artist View."""

    template = "music/artist.html"

    def get(self, request, id):
        """Show artist template."""
        artist = get_object_or_404(Artist, id=id)
        context = {"artist": artist}
        return render(request, self.template, context)
