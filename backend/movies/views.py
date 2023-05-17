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


class MoviePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 100
    
def save_ost(request):
    client_id = '150e34294220415f8bc1337af12adb58'
    client_secret = '257cf688a26f4c8181c2b3b5447ac4e1'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    movies = Movie.objects.all()
    for movie in movies:
        album = sp.search(q=movie.original_title, type='album', limit=1)['albums']['items']
        if not album:
            continue
        for track in sp.album_tracks(album[0]['id'])['items']:
            music = Music(title=track['name'], artist=track['artists'][0]['name'], uri=track['uri'])
            music.save()
            movie.ost.add(music)
            print(movie, music)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    if movie not in user.like_movie.all():
        user.like_movie.add(movie)
        response_data = {"like_count": movie.users_like_movies.count(),"message": "Movie liked successfully."}
    else:
        user.like_movie.remove(movie)
        response_data = {"like_count": movie.users_like_movies.count(), "message": "Movie unliked successfully."}

    return Response(response_data)

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

