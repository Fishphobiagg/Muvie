from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . models import Music
from . serializers import *
from rest_framework.views import APIView
from rest_framework import status
from sklearn.preprocessing import StandardScaler


class MusicPagenatior(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 100

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_music(request, keyword):
    music_search_result = Music.objects.filter(Q(artist__icontains=keyword)|Q(title__icontains=keyword))
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
            scaler = StandardScaler()
            user = request.user
            if serializer.is_valid():
                component = user.music_components
                for field, value in serializer.validated_data.items():
                    setattr(component, field, value)
                component.vector = scaler.fit_transform([
                    [user.music_components.energy],
                    [user.music_components.instrumentalness],
                    [user.music_components.liveness],
                    [user.music_components.speechiness],
                    [user.music_components.acousticness],
                    [user.music_components.valence],
                    [user.music_components.tempo*0.1],
                    [user.music_components.mode],
                    [user.music_components.loudness*0.1],
                    [user.music_components.danceability],
                ])
                component.save()
                
                return Response({"vector":user.music_components.vector}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

