from .models import Movie
from rest_framework import serializers

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'  

class MovieSerializer(serializers.ModelSerializer):
    ost = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['title','ost']
    
    def get_ost(self, instance):
        all_ost = instance.ost.all()
        return [{"title": ost.title, "artist":ost.artist, 'uri':ost.uri, 'like':ost.users_like_musics.count()} for ost in all_ost]
    