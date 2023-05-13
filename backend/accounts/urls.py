from django.urls import path
from .views import SignupAPIView, AuthAPIView, FollowAPIView, ProfileView, AccountsChangeView, PasswordChangeView
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import * 
from rest_framework import viewsets

urlpatterns = [
    path('signup', SignupAPIView.as_view()),
    path('auth', AuthAPIView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view()),
    path('<int:user_pk>/follow', FollowAPIView.as_view()),
    path('<int:user_pk>/profile', ProfileView.as_view()),
    path('edit/<int:user_pk>/', AccountsChangeView.as_view()),
    path('edit/<int:user_pk>/password', PasswordChangeView.as_view()),
    
]
