from django.shortcuts import render
from . models import Movie
from . serializers import MovieListSerializer, MovieSerializer
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import spotipy
from musics.models import Music
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

class MoviePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 100
    
def save_ost(request):
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
    return Response({'검색된 영화 개수':movie_count,
                     '저장된 음악 개수':music_count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_movie_ost(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_movie(request, keyword):
    movie_search_result = Movie.objects.filter(Q(original_title__icontains=keyword)|Q(title__icontains=keyword))
    paginator = MoviePagination()
    result_page = paginator.paginate_queryset(movie_search_result, request)
    serializer = MovieListSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

