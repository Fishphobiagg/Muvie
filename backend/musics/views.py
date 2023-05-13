from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . models import Music
from serializers import *

class MusicPagenatior(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 100

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_movie(request, keyword):
    movie_search_result = Music.objects.filter(Q(content__icontains=keyword)|Q(title__icontains=keyword))
    paginator = MusicPagenatior()
    result_page = paginator.paginate_queryset(movie_search_result, request)
    serializer = MusicListSerializers(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)