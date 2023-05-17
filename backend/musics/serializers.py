from .models import Music, MusicComponent
from rest_framework import serializers
from accounts.models import User

class ComponentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = MusicComponent
        fields = '__all__'

class MusicListSerializer(serializers.ModelSerializer):
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
    
class PlaylistSerializer(serializers.ModelSerializer):
    album_cover = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()
    class Meta:
        model = Music
        fields = ['title', 'artist', 'uri', 'album_cover', 'like_count', 'movie']
    
    def get_album_cover(self, instance):
        album_cover = instance.movie_ost.all()[0]
        return {"poster_path":album_cover.poster_path}
    def get_movie(self, instance):
        return instance.movie_ost.all()[0].title
    def get_like_count(self, instance):
        return instance.users_like_musics.count()

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicComponent
        fields = '__all__'