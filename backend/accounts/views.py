# views.py
from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from muvie.settings import SECRET_KEY
import jwt

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
    
class AuthAPIView(APIView):
    # 유저 정보 확인
    def get(self, request):
        try:
            # access token을 decode 해서 유저 id 추출 => 유저 식별
            access = request.COOKIES['access']
            payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
            pk = payload.get('user_id')
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(instance=user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except(jwt.exceptions.ExpiredSignatureError):
            # 토큰 만료 시 토큰 갱신
            data = {'refresh': request.COOKIES.get('refresh', None)}
            serializer = TokenRefreshSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                access = serializer.data.get('access', None)
                refresh = serializer.data.get('refresh', None)
                payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(User, pk=pk)
                serializer = UserSerializer(instance=user)
                res = Response(serializer.data, status=status.HTTP_200_OK)
                res.set_cookie('access', access)
                res.set_cookie('refresh', refresh)
                return res
            raise jwt.exceptions.InvalidTokenError

        except(jwt.exceptions.InvalidTokenError):
            # 사용 불가능한 토큰일 때
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # 로그인
    def post(self, request):
    	# 유저 인증
        user = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )
        print(request.data)
        # 이미 회원가입 된 유저일 때
        if user is not None:
            serializer = UserSerializer(user)
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
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
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # 로그아웃
    def delete(self, request):
        # 쿠키에 저장된 토큰 삭제 => 로그아웃 처리
        response = Response({
            "message": "Logout success"
            }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response

class FollowAPIView(APIView):
    def get(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        serializer = FollowSerializer(user)
        return Response(serializer.data)

    def post(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        opponent = get_object_or_404(User, pk=request.data['opponent_id'])
        if opponent in user.following.all():
            return Response({
                "message" : "already followed"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.following.add(opponent)
            return Response({
                "message": "follow success",
            })
    def delete(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        opponent = get_object_or_404(User, pk=request.data['opponent_id'])
        if opponent not in user.following.all():
            return Response({
                "message" : "Not followed"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.following.remove(opponent)
            return Response({
                "message": 'Unfollow success'
            })

class ProfileView(APIView):
    def get(self, request, user_pk):
        me = request.user
        if user_pk == me.pk:
            serializer = MyProfileSerializer(instance=me)
            user_serializer = SimpleUserSerializer(me)
            response = {
                "user_profile" : user_serializer.data,
                "detail" : serializer.data
            }
            return Response(response)
        else:
            user = User.objects.get(pk=user_pk)
            serializer = ProfileSerializer(instance=user)
            user_serializer = SimpleUserSerializer(user)
            response = {
                "user_profile" : user_serializer.data,
                "detail" : serializer.data
            }
            return Response(response)
        
class PasswordChangeView(APIView):
    pass
class AccountsChangeView(APIView):
    def patch(self, request, user_pk):
        user = User.objects.get(pk=request.user)
        user.email = request.email
        user.nickname = request.nickname
        user.profile_picture = request.profile_picture

        user.save()
        return Response({
            "message": "change Success"
        })
        
        
        