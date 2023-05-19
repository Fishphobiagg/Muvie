from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from musics.serializers import PlaylistSerializer
from .algorithms.algorithm import recommend_ost, calculate_vector
from .serializers import *
from musics.models import Music
from accounts.models import MusicUserLike, User


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

import numpy as np

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class SignupAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(cls, user)
        # Add custom claims
        token['email'] = user.email
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['nickname'] = self.user.nickname
        data['email'] = self.user.email
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class FollowAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        serializer = FollowSerializer(user)
        return Response(serializer.data)

    def post(self, request, user_pk):
        user = request.user
        opponent = User.objects.get(pk=user_pk)
        if opponent in user.following.all():
            return Response({
                "message" : "already followed"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.following.add(opponent)
            serializer = FollowSerializer(user)
            return Response(serializer.data)
    def delete(self, request, user_pk):
        user = request.user
        opponent = User.objects.get(pk=user_pk)
        if opponent not in user.following.all():
            return Response({
                "message" : "Not followed"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = FollowSerializer(user)
            user.following.remove(opponent)
            return Response(serializer.data)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, user_pk):
        me = request.user
        if user_pk == me.pk:
            print(me)
            serializer = MyProfileSerializer(instance=me, user_pk=me.pk)
            user_serializer = SimpleUserSerializer(me)
            response = {
                "user_profile" : user_serializer.data,
                "detail" : serializer.data
            }
            return Response(response)
        else:
            user = User.objects.get(pk=user_pk)
            serializer = ProfileSerializer(instance=user, user_pk=me.pk)
            user_serializer = SimpleUserSerializer(user)
            print(123412412412342, user_serializer.data)
            response = {
                "user_profile" : user_serializer.data,
                "detail" : serializer.data
            }
        return Response(response)
        
class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        new_password = request.data.get('new_password')
        new_password_confirm = request.data.get('new_password_confirm')
        if new_password == new_password_confirm:
            user.password = new_password
            return Response(SimpleUserSerializer(user).data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class AccountsChangeView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, user_pk):
        print(request.data)
        print(request.user.pk)
        print(user_pk)
        user = User.objects.get(pk=user_pk)
        if request.user != user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserChangeSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print('ㅇㅇㅇ')
            return Response({"message":"Change Success",
                             "changed_data" : UserChangeSerializer(User.objects.get(pk=user_pk)).data
                             })
        ㅔ
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class LikeListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        like_list = user.like_music.all()
        serializer = PlaylistSerializer(like_list, many=True)
        return Response(serializer.data)

class PlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        playlist = user.playlist.all()
        serializer = PlaylistSerializer(playlist, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_components(request):
    user = request.user
    component = user.music_components
    data = {
        'energy': component.energy,
        'instrumentalness': component.instrumentalness,
        'liveness': component.liveness,
        'acousticness': component.acousticness,
        'speechiness': component.speechiness,
        'valence': component.valence,
        'tempo': component.tempo,
        'mode': component.mode,
        'loudness': component.loudness,
        'danceability': component.danceability,
    }
    recommend_list = recommend_ost(data)
    response = {"data":[]}
    for recommend in recommend_list['tracks']:
        title = recommend['name']
        artist = recommend['artists'][0]['name']
        album = recommend['album']['name']
        uri = recommend['uri']
        poster = recommend['album']['images'][0]['url']
        if Music.objects.filter(title=title, artist=artist):
           response['data'].append({"title":title, "artist":artist, 'album':album, "uri":uri, 'poster':poster})
        else:
            new = Music.objects.create(
                title=title, artist=artist, uri=uri, album_cover = poster
            )
            new.save()
            response['data'].append({"title":title, "artist":artist, 'album':album, "uri":uri, 'poster':poster})
    return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_user(request):
    user = request.user
    random_users = User.objects.order_by('?')[:10] # 대규모로 갈 경우 속도가 느려지기 때문에 후에 수정
    user_vector = calculate_vector(user)
    random_user_list = []

    for random_user in random_users:
        random_user_vector = calculate_vector(random_user)
        similarity = cosine_similarity(user_vector, random_user_vector)[0][0]
        random_user_list.append((similarity, random_user))
        
    random_user_list.sort(key=lambda x: x[0], reverse=True)
    topusers = [user[1] for user in random_user_list[:3]]
    user_serializer = SimpleUserSerializer(topusers, many=True)
    return Response({"recommend":user_serializer.data})
    
    # 가장 유사도가 높은 사용자 정보 반환


# 최근접 이웃 협업 필터링 

def collaborative_filtering(user, n=10):
    liked_music_ids = MusicUserLike.objects.filter(user=user).values_list('music_id', flat=True)

    similar_users = User.objects.filter(musicuserlike__music_id__in=liked_music_ids).exclude(id=user.id)

    similarity_scores = {}
    for similar_user in similar_users:
        similar_user_liked_music_ids = MusicUserLike.objects.filter(user=similar_user).values_list('music_id')
        similarity_scores[similar_user.id] = len(set(liked_music_ids) & set(similar_user_liked_music_ids))
    sorted_similar_users = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    top_similar_users = [item[0] for item in sorted_similar_users[:n]]
    recommend_music = Music.objects.filter(musicuserlike__user__id__in=top_similar_users).annotate(like_count=Count('musicuserlike')).order_by('-like_count')

    return recommend_music, top_similar_users

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_like(request):
    user = request.user
    recommend_music, top_similar_user = collaborative_filtering(user, n=10)
    print(top_similar_user)
    serialized_music = []
    for music in recommend_music[:5]:
        serialized_music.append(
            {
                "id":music.id,
                "title":music.title,
                "artist":music.artist,
            }
        )
    return Response(serialized_music)