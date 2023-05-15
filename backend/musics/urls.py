from django.urls import path

from . views import MusicLikeView, MusicPlaylistView

urlpatterns = [
      path('playlist/<int:music_pk>', MusicPlaylistView.as_view()),
      path('like/<int:music_pk>', MusicLikeView.as_view()),
]