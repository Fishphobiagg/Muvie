from django.urls import path
from .views import SignupAPIView, AuthAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import * 
from rest_framework import viewsets

urlpatterns = [
    path('signup', SignupAPIView.as_view()),
    path('auth', AuthAPIView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view())
]
