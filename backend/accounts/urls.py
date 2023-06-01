from django.urls import path
from .views import get_like_list, get_play_list, signup, MyTokenObtainPairView, FollowAPIView, profile_view, change_accounts, recommend_components, recommend_like, recommend_user, search_user

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view()),
    path('<int:user_pk>/follow', FollowAPIView.as_view()),
    path('playlist', get_play_list),
    path('like', get_like_list),
    path('signup', signup),
    path('<int:user_pk>/profile', profile_view),
    path('edit/<int:user_pk>/',change_accounts),
    path('recommend/components', recommend_components),
    path('recommend/user', recommend_user),
    path('recommend/like', recommend_like),
    path('search/<keyword>',search_user )
]
