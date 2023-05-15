from .models import Music
from rest_framework import serializers

class MusicListSerializers(serializers.ModelSerializer):
    album_cover = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = ['title', 'artist', 'like_count', 'album_cover', 'uri']
    
    def get_album_cover(self, instance):
        album_cover = instance.movie_ost.all()[0]
        return {"poster_path":album_cover.poster_path}
    
    def get_like_count(self, instance):
        return instance.users_like_musics.count()
    
class PlaylistSerializers(serializers.ModelSerializer):
    album_cover = serializers.SerializerMethodField()
    class Meta:
        model = Music
        fields = ['title', 'artist', 'uri', 'album_cover']
    
    def get_album_cover(self, instance):
        album_cover = instance.movie_ost.all()[0]
        return {"poster_path":album_cover.poster_path}

