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
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from urllib.parse import urlencode

class MoviePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 100
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializers = MovieSerializer()
    serializers.data()

def save_ost(request):
    client_id = '150e34294220415f8bc1337af12adb58'
    client_secret = '257cf688a26f4c8181c2b3b5447ac4e1'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print(1111)
    youtube_api = 'AIzaSyB2G6svQ9t_FExTdVKew7buIlbG24rYOS4'
    youtube = build('youtube', 'v3', developerKey=youtube_api)

    movies = Movie.objects.all()
    for movie in movies:
        print(movie)
        album = sp.search(q=movie.original_title, type='album', limit=5)['albums']['items']
        print(1)
        print(album)
        if not album:
            print(1)
            continue
        for track in sp.album_tracks(album[0]['id'])['items']:
            try:
                search_response = youtube.search().list(
                    q=track['name'] + ' ' + track['artists'][0]['name'],
                    part = 'snippet',
                    maxResults=1,
                    type = 'video'
                ).execute()
                if 'items' in search_response:
                    video_id = search_response['items'][0]['id']['videoId']
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
            except HttpError as e:
                continue
            music = Music(title=track['name'], artist=track['artists'][0]['name'], uri=track['uri'], youtube_uri=video_url)
            music.save()
            movie.ost.add(music)
            print(movie, music, video_url)
    return Response({"message":"save success"})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    if movie not in user.users_movie_like.all():
        user.like_movie.add(movie)
        response_data = {"status": "success", "message": "Movie liked successfully."}
    else:
        user.like_movie.remove(movie)
        response_data = {"status": "success", "message": "Movie unliked successfully."}

    return Response(response_data)

def search_movie_ost(request, movie_pk):
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_movie(request, keyword):
    movie_search_result = Movie.objects.filter(Q(content__icontains=keyword)|Q(title__icontains=keyword))
    paginator = MoviePagination()
    result_page = paginator.paginate_queryset(movie_search_result, request)
    serializer = MovieListSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
