from .models import Movie
from rest_framework import serializers



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        fields = '__all__'

# music model 구현 이후 구현
# music model 구현 이후 구현
class MovieSerializer(serializers.ModelSerializer):
#     ost = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
    pass