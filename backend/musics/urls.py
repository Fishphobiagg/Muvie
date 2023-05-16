from django.urls import path

from . views import MusicLikeView, MusicPlaylistView, MusicComponentView

urlpatterns = [
      path('playlist/<int:music_pk>', MusicPlaylistView.as_view()),
      path('like/<int:music_pk>', MusicLikeView.as_view()),
      path('component', MusicComponentView.as_view()),
]