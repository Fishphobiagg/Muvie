from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . models import Music
from . serializers import *
from rest_framework.views import APIView
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_music(request, keyword):
    music_search_result = Music.objects.filter(Q(artist__icontains=keyword)|Q(title__icontains=keyword)|Q(movie_ost__title__icontains=keyword)|Q(movie_ost__original_title__icontains=keyword))
    serializer = MusicListSerializer(instance=music_search_result, many=True, user_pk=request.user.pk)
    return Response({'data':serializer.data}, status=status.HTTP_206_PARTIAL_CONTENT)
    
class MusicLikeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, **kwargs):
        user = request.user
        like_list = user.like_music.all()
        serializer = MusicListSerializer(like_list, many=True, user_pk=user.pk)
        return Response(serializer.data)

    def post(self, request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.like_music.add(music)
        like_list = user.like_music.all()
        serializer = MusicListSerializer(like_list, many=True, user_pk=user.pk)
        return Response({'message':'like successfully', "like_list":serializer.data}, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, reqeust, music_pk):
        user = reqeust.user
        music = Music.objects.get(pk=music_pk)
        user.like_music.remove(music)
        like_list = user.like_music.all()
        serializer = MusicListSerializer(like_list, many=True, user_pk=user.pk)
        return Response({'message':'unlike successfully', "like_list":serializer.data}, status=status.HTTP_202_ACCEPTED)

class MusicPlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.playlist.add(music)
        serializer = MusicListSerializer(user.playlist.all(), many=True, user_pk=user.pk)
        return Response({"message":"Added to playlist successfully",
                         "play_list":serializer.data
                         })

    def delete(self, request, music_pk):
        user = request.user
        music = Music.objects.get(pk=music_pk)
        user.playlist.remove(music)
        serializer = MusicListSerializer(user.playlist.all(), many=True, user_pk=user.pk)
        return Response({"message":"Deleted to playlist successfully",
                         "play_list":serializer.data
                         })

class MusicComponentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        data = user.music_components
        response_data = {
    "id": user.id,
    "energy": int(float(data.energy) * 100),
    "instrumentalness": int(float(data.instrumentalness) * 100),
    "liveness": int(float(data.liveness) * 100),
    "acousticness": int(float(data.acousticness) * 100),
    "speechiness": int(float(data.speechiness) * 100),
    "valence": int(float(data.valence) * 100),
    "tempo": int((data.tempo-50)/3),
    "loudness": int(-data.loudness*5/3),
    "danceability": int(float(data.danceability) * 100)
}

        return Response(response_data)

    def post(self, request):
        user = request.user
        component_data = request.data

        serializer = ComponentSerializer(user.music_components, data=component_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
