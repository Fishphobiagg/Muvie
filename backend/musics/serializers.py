from .models import Music, MusicComponent
from rest_framework import serializers

class MusicListSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()
    isLiked = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = ['id','title', 'artist', 'uri', 'album_cover', 'like_count', 'movie', 'isLiked']
    
    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('user_pk', None)
        super().__init__(*args, **kwargs)
        self.user_pk = user_pk

    def get_movie(self, instance):
        if instance.movie_ost.all():
            return instance.movie_ost.all()[0].title
        return 0
    
    def get_like_count(self, instance):
        return instance.users_like_musics.count()
    
    def get_isLiked(self, instance):
        return instance.users_like_musics.filter(id=self.user_pk).exists()

class ComponentSerializer(serializers.ModelSerializer):
    energy = serializers.FloatField()
    instrumentalness = serializers.FloatField()
    liveness = serializers.FloatField()
    acousticness = serializers.FloatField()
    speechiness = serializers.FloatField()
    valence = serializers.FloatField()
    tempo = serializers.FloatField()
    loudness = serializers.FloatField()
    danceability = serializers.FloatField()

    def to_internal_value(self, data):
        data["energy"] = float(data.get("energy", 0)) / 100
        data["instrumentalness"] = float(data.get("instrumentalness", 0)) / 100
        data["liveness"] = float(data.get("liveness", 0)) / 100
        data["acousticness"] = float(data.get("acousticness", 0)) / 100
        data["speechiness"] = float(data.get("speechiness", 0)) / 100
        data["valence"] = float(data.get("valence", 0)) / 100
        data["tempo"] = int(data.get("tempo", 0)) * 3 + 50
        data["loudness"] = -int(data.get("loudness", 0)) * 3/5
        data["danceability"] = float(data.get("danceability", 0)) / 100
        return super().to_internal_value(data)

    class Meta:
        model = MusicComponent
        exclude = ('mode',)
