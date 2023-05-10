from django.shortcuts import render
from . models import Movie
from . serializers import MovieListSerializer, MovieSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET'])
def movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializers = 0

def user_movie_like(request, movie_pk):
    pass

def search_movie_ost(request, movie_pk):
    pass

def search_movie(request, keyword):
    movie = Movie.objects.filter()
