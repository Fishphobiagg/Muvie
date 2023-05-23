from django.urls import path
from . views import MusicLikeView, MusicPlaylistView, MusicComponentView, search_music, liked_users

urlpatterns = [
    path('playlist/<int:music_pk>', MusicPlaylistView.as_view()),
    path('like/<int:music_pk>/users', liked_users),
    path('like/<int:music_pk>', MusicLikeView.as_view()),
    path('component', MusicComponentView.as_view()),
    path('search/<keyword>', search_music),
]