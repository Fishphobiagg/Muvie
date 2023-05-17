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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_music(request, keyword):
    music_search_result = Music.objects.filter(Q(content__icontains=keyword)|Q(title__icontains=keyword))
    paginator = MusicPagenatior()
    result_page = paginator.paginate_queryset(music_search_result, request)
    serializer = MusicListSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

class MusicLikeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, **kwargs):
        user = request.user
        like_list = user.like_music.all()
        paginator = MusicPagenatior()
        result_page = paginator.paginate_queryset(like_list, request)
        serializer = PlaylistSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


    def post(self, request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.like_music.add(music)
        return Response({'message':'like successfully'}, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, reqeust, music_pk):
        user = reqeust.user
        music = Music.objects.get(pk=music_pk)
        user.like_music.remove(music)
        return Response({'message':'unlike successfully'}, status=status.HTTP_202_ACCEPTED)

class MusicPlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, **kwargs):
        user = request.user
        playlist = user.playlist.all()
        paginator = MusicPagenatior()
        result_page = paginator.paginate_queryset(playlist, request)
        serializer = PlaylistSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.playlist.add(music)
        return Response({"message":"Added to playlist successfully"})

    def delete(self, request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.playlist.remove(music)
        return Response({"message":"Deleted to playlist successfully"})

class MusicComponentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        component = user.music_components
        serializer = ComponentSerializer(component)
        return Response(serializer.data)
    
    def post(self, request):
            serializer = ComponentSerializer(data=request.data)
            if serializer.is_valid():
                component = serializer.save(user=request.user)  # 1대1 관계 설정
                print(request.user.music_components)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

