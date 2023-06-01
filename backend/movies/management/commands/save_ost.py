from django.core.management.base import BaseCommand
from django.conf import settings
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

from musics.models import Music
from movies.models import Movie


class Command(BaseCommand):
    help = 'Save OST from Spotify'

    def handle(self, *args, **options):
        sp_client_id = settings.SPOTIFY_ID
        sp_secret = settings.SPOTIFY_SECRET
        client_credentials_manager = SpotifyClientCredentials(client_id=sp_client_id, client_secret=sp_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        movies = Movie.objects.all()

        movie_count = 0
        music_count = 0

        for movie in movies:
            album = sp.search(q=movie.original_title, type='album', limit=1)['albums']
            poster = ''
            if album['items']:
                poster = album['items'][0]['images'][0]['url']
            album = album['items']
            if not album:
                continue
            movie_count += 1
            for track in sp.album_tracks(album[0]['id'])['items']:
                music = Music(title=track['name'], artist=track['artists'][0]['name'], uri=track['uri'], album_cover=poster)
                music.save()
                movie.ost.add(music)
                music_count += 1
            print(music_count, movie_count)
