from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from musics.serializers import MusicListSerializer
from .algorithms.algorithm import recommend_ost, calculate_vector, collaborative_filtering
from .serializers import *
from musics.models import Music
from accounts.models import MusicUserLike, User

import numpy as np
from numpy import dot
from numpy.linalg import norm

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

import random

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        if 'email' in serializer.errors:
            return Response({"message":"Email is already registered"}, status=status.HTTP_400_BAD_REQUEST)
        elif 'nickname' in serializer.errors:
            return Response({"message":"Nickname is already registered"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        response = {
            "user": {
                "id": self.user.id,
                "nickname": self.user.nickname,
                "email": self.user.email,
                "profile_picture": self.user.profile_picture.url,
            },
            "message": "login success",
            "token": {
                "access": data["access"],
                "refresh": data["refresh"]
            }
        }
        
        return response

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
        user.following.add(opponent)
        serializer = ProfileSerializer(instance=User.objects.get(pk=user_pk), user_pk=user.pk)
        return Response(serializer.data)
        
    def delete(self, request, user_pk):
        user = request.user
        opponent = User.objects.get(pk=user_pk)
        if opponent not in user.following.all():
            return Response({
                "message" : "Not followed"
            }, status=status.HTTP_400_BAD_REQUEST)   
        user.following.remove(opponent)
        serializer = ProfileSerializer(instance=user, user_pk=user.pk)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request, user_pk):
    me = request.user
    user = User.objects.get(pk=user_pk)
    serializer = ProfileSerializer(instance=user, user_pk=me.pk)
    user_serializer = SimpleUserSerializer(user)
    response = {
        "user_profile" : user_serializer.data,
        "detail" : serializer.data
    }
    return Response(response)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def change_accounts(self, request, user_pk):
    user = User.objects.get(pk=user_pk)
    serializer = UserChangeSerializer(user, data=request.data, partial=True)
    
    if 'email' in serializer.errors:
        return Response({"message":"Email is already registered"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif 'nickname' in serializer.errors:
        return Response({"message":"Nickname is already registered"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response({"changed_data" : UserChangeSerializer(User.objects.get(pk=user_pk)).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_like_list(request):
    user = request.user
    like_list = user.like_music.all()
    serializer = MusicListSerializer(like_list, many=True, user_pk=user.pk)
    return Response({"like_list":serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_play_list(request):
    user = request.user
    playlist = user.playlist.all()
    serializer = MusicListSerializer(playlist, many=True, user_pk=user.pk)
    return Response({"play_list":serializer.data})

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
        'loudness': component.loudness,
        'danceability': component.danceability,
    }
    recommend_list = recommend_ost(data)
    response = {"data":[]}
    for recommend in recommend_list['tracks']:
        title = recommend['name']
        artist = recommend['artists'][0]['name']
        album = recommend['album']['name']
        poster = recommend['album']['images'][0]['url']

        if Music.objects.filter(title=title, artist=artist):
           music = Music.objects.filter(title=title, artist=artist)[0]
           response['data'].append({"id":music.pk, "title":title, "artist":artist, 'album':album, 'poster':poster, 'like count':music.users_like_musics.count()})
        else:
            new = Music.objects.create(
                title=title, artist=artist, album_cover = poster
            )
            new.save()
            response['data'].append({"id":new.pk, "title":title, "artist":artist, 'album':album, 'poster':poster, 'like count' : 0})
    return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_user(request):
    user = request.user
    user_vector = calculate_vector(user)
    random_users = random.sample(list(User.objects.exclude(pk=user.pk).exclude(following=user)), (User.objects.all().count() - User.objects.filter(following=user).count())//10) # 대규모로 갈 경우 속도가 느려지기 때문에 후에 수정
    user_vector = np.array(calculate_vector(user))
    random_user_list = []
    for random_user in random_users:
        random_user_vector = np.array(calculate_vector(random_user))
        similarity = dot(user_vector, random_user_vector)/(norm(user_vector)*norm(random_user_vector))        
        random_user_list.append((similarity, random_user))
    
    random_user_list.sort(key=lambda x: x[0], reverse=True)
    topusers = [user[1] for user in random_user_list[:5]]

    user_serializer = SimpleUserSerializer(topusers, many=True)
    return Response({"recommend":user_serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_like(request):
    user = request.user
    recommend_music, top_similar_user = collaborative_filtering(user, n=10)
    serialized_music = []
    for music in recommend_music[:5]:
        serialized_music.append(
            {
                "id":music.id,
                "title":music.title,
                "artist":music.artist,
                "album_cover":music.album_cover,
                "like_count":music.users_like_musics.count()
            }
        )
    return Response(serialized_music)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_user(request, keyword):
    user = request.user
    liked_music_ids = MusicUserLike.objects.filter(user=user).values_list('music_id', flat=True)
    searched_users = User.objects.filter(Q(nickname__icontains=keyword)).exclude(pk=user.pk)
    similarity_scores = {}
    for similar_user in searched_users:
        similar_user_liked_music_ids = MusicUserLike.objects.filter(user=similar_user).values_list('music_id')
        similarity_scores[similar_user.id] = len(set(liked_music_ids) & set(similar_user_liked_music_ids))

    sorted_similar_users = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    responses = []
    for user_id, like in sorted_similar_users:
        searched_user = User.objects.get(pk=user_id)
        responses.append(
        {
            'id':searched_user.id,
            'nickname':searched_user.nickname,
            'email':searched_user.email,
            'profile_picture':searched_user.profile_picture.url,
            'followers_count':searched_user.followers.all().count(),
            'following_count':searched_user.following.all().count(),
            'is_followed': user.following.filter(pk=user_id).exists()
        }
        )
    return Response({"data":responses}, status=status.HTTP_200_OK)