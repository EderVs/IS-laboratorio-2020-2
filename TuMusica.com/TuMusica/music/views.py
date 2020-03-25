"""Music Views."""
# Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

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
    TODO: Show albums.
    TODO: Show playlists.
    """

    template = "music/index.html"

    def get(self, request):
        """GET method."""
        artists = Artist.objects.all()
        songs = Song.objects.all()
        context = {"artists": artists, "songs": songs}
        return render(request, self.template, context)


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
        context = {"artist": artist, "songs": artist.songs.all()}
        return render(request, self.template, context)


class ToggleLikeSongAPIView(LoginRequiredMixin, View):
    """Like song api."""

    def post(self, request, id):
        """Toggle Like of a song."""
        song = get_object_or_404(Song, id=id)
        response_text = ""
        if song in request.user.extended_user.fav_songs.all():
            request.user.extended_user.fav_songs.remove(song)
            response_text = "Like"
        else:
            request.user.extended_user.fav_songs.add(song)
            response_text = "Dislike"
        return HttpResponse(response_text, status=200)
