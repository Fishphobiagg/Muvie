from .models import Movie
from rest_framework import serializers

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'  

class MovieSerializer(serializers.ModelSerializer):
#     ost = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
    pass