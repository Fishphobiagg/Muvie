from django.urls import path
from .views import PlaylistView, LikeListView, SignupAPIView, MyTokenObtainPairView, FollowAPIView, ProfileView, AccountsChangeView, PasswordChangeView, recommend_components, recommend_like, recommend_user, search_user

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view()),
    path('playlist', PlaylistView.as_view()),
    path('like', LikeListView.as_view()),
    path('signup', SignupAPIView.as_view()),
    path('<int:user_pk>/follow', FollowAPIView.as_view()),
    path('<int:user_pk>/profile', ProfileView.as_view()),
    path('edit/<int:user_pk>/', AccountsChangeView.as_view()),
    path('edit/<int:user_pk>/password', PasswordChangeView.as_view()),
    path('recommend/components', recommend_components),
    path('recommend/user', recommend_user),
    path('recommend/like', recommend_like),
    path('search/<keyword>',search_user )
]
