from django.shortcuts import render
from . models import Movie
from . serializers import MovieListSerializer, MovieSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classe
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
# from . . musics import Music

class MoviePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 100

@api_view(['GET'])
def movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializers = MovieSerializer()
    serializers.data()
    
def user_movie_like(request, movie_pk):
    pass

def search_movie_ost(request, movie_pk):
    pass

@api_view(['GET'])
def search_movie(request, keyword):
    movie_search_result = Movie.objects.filter(Q(content__icontains=keyword)|Q(title__icontains=keyword))
    paginator = MoviePagination()
    result_page = paginator.paginate_queryset(movie_search_result, request)
    serializer = MovieListSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)