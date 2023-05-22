from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . models import Music
from . serializers import *
from rest_framework.views import APIView
from rest_framework import status
from decimal import Decimal


class MusicPagenatior(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 100

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_music(request, keyword):
    music_search_result = Music.objects.filter(Q(artist__icontains=keyword)|Q(title__icontains=keyword)|Q(movie_ost__title__icontains=keyword)|Q(movie_ost__original_title__icontains=keyword))
    serializer = MusicListSerializer(music_search_result, many=True)
    return Response({'data':serializer.data})

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
        like_list = user.like_music.all()
        serializer = PlaylistSerializer(like_list, many=True)
        return Response({'message':'like successfully', "like_list":serializer.data}, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, reqeust, music_pk):
        user = reqeust.user
        music = Music.objects.get(pk=music_pk)
        user.like_music.remove(music)
        like_list = user.like_music.all()
        serializer = PlaylistSerializer(like_list, many=True)
        return Response({'message':'unlike successfully', "like_list":serializer.data}, status=status.HTTP_202_ACCEPTED)

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
        data = user.music_components
        response_data = {
    "id": 5,
    "energy": int(float(data.energy) * 100),
    "instrumentalness": int(float(data.instrumentalness) * 100),
    "liveness": int(float(data.liveness) * 100),
    "acousticness": int(float(data.acousticness) * 100),
    "speechiness": int(float(data.speechiness) * 100),
    "valence": int(float(data.valence) * 100),
    "tempo": int((data.tempo-50)/3),
    "mode": int(float(data.mode) * 100),
    "loudness": int(-data.loudness*5/3),
    "danceability": int(float(data.danceability) * 100)
}

        return Response(response_data)
    
    # def post(self, request):
    #         serializer = ComponentSerializer(data=request.data)
    #         user = request.user
    #         if serializer.is_valid():
    #             component = user.music_components
    #             for field, value in serializer.validated_data.items():
    #                 setattr(component, field, value)
    #             component.save()
    #             return Response({"component":user.music_components}, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


    def post(self, request):
        serializer = ComponentSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            component = user.music_components
            for field, value in serializer.validated_data.items():
                if field == 'tempo':
                    if 0 <= value <= 100:
                        value = (value / 100) * 300 + 50  # 비율에 맞게 50부터 350 사이 값으로 변환
                    else:
                        value = min(max(value, 50), 350)  # 범위 조정: 50부터 350 사이 값으로
                elif field == 'loudness':
                    if 0 <= value <= 100:
                        value = (value / 100) * -60  # 비율에 맞게 -60부터 0 사이 값으로 변환
                    else:
                        value = min(max(value, -60), 0)  # 범위 조정: -60부터 0 사이 값으로
                else:
                    if 0 <= value <= 100:
                        value = float(value/100)  # 문자열을 실수형으로 변환
                    else:
                        value = float(value)
                      # 범위 조정: 0부터 1 사이로 조정

                setattr(component, field, value)
            component.save()
            
            # 직렬화 시에 0부터 100 사이 값으로 변환하여 응답 데이터 생성
            serialized_data = {
        field: int(Decimal(value) * 100) if field not in ['tempo', 'loudness'] else int((value-50)/3) if field == 'tempo' else int(-value*5/3)
                for field, value in serializer.validated_data.items()
            }
            
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

