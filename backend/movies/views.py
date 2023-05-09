from django.shortcuts import render
from . models import Movie
from . serializers import MovieListSerializer, MovieSerializer
from django.db.models import Q

def all_movies(request):
    movies = Movie.objects.all()
    serializers = 0

def movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializers = 0

def user_movie_like(request, movie_pk):
    pass

def search_movie_ost(request, movie_pk):
    pass

def search_movie(request, keyword):
    movie = Movie.objects.filter(Q(title__icontains=keyword)|Q(original_title__icontains=keyword))
    serializers = 0