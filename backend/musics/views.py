from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . models import Music
from . serializers import *
from rest_framework.views import APIView
from rest_framework import status

class MusicPagenatior(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 100

def music(request):
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_music(request, keyword):
    movie_search_result = Music.objects.filter(Q(content__icontains=keyword)|Q(title__icontains=keyword))
    paginator = MusicPagenatior()
    result_page = paginator.paginate_queryset(movie_search_result, request)
    serializer = MusicListSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

class MusicLikeView(APIView):
    def post(request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.like_music.add(music)
        return Response({'message':'like successfully'}, status=status.HTTP_202_ACCEPTED)
    
    def delete(reqeust, music_pk):
        user = reqeust.user
        music = Music.objects.get(pk=music_pk)
        user.like_music.remove(music)
        return Response({'message':'unlike successfully'}, status=status.HTTP_202_ACCEPTED)

class MusicPlaylistView(APIView):
    def get(request, music_pk):
        user = request.user
        playlist = user.playlist.all()
        paginator = MusicPagenatior()
        result_page = paginator.paginate_queryset(playlist)
        serializers = PlaylistSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializers.data)

    def post(request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.playlist.add(music)
        return Response({"message":"Added to playlist successfully"})

    def delete(request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.playlist.remove(music)
        return Response({"message":"Deleted to playlist successfully"})

class MusicComponentView(APIView):
    def get(self, request):
        user = request.user
        component = user.music_components
        serializer = ComponentSerializer(component)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ComponentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(serializer.errors, status=400)
