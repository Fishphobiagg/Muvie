from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'nickname', 'email', 'profile_picture']
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            nickname = validated_data['nickname'],
            profile_picture = '/users/민지.JPEG'if len(validated_data) == 3 else validated_data['profile_picture']
        )
        return user

class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'profile_picture']

class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'profile_picture']

class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'profile_picture']

class FollowSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    following = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'followers', 'following')

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'nickname', 'profile_picture']

class MyProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    # like_movie_list = serializers.SerializerMethodField()
    # like_music_list = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    # playlist = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('followers', 'following','followers_count', 'following_count')
    
    def get_followers(self, instance):
        followers = instance.followers.all()
        return [{'id':follower.id, 'email':follower.email, 'nickname':follower.nickname, 'profile_picture':follower.profile_picture} for follower in followers]
    
    def get_following(self, instance):
        following = instance.following.all()
        return [{'id':follower.id, 'email':follower.email, 'nickname':follower.nickname, 'profile_picture':follower.profile_picture} for follower in following]
    
    # def get_like_movie_list(self, instance):
    #     like_movie_list = instance.users_like_movies.all()
    #     return[{'title':movie.title, 'poster_path':movie.poster_path} for movie in like_movie_list]
    
    def get_followers_count(self, instance):
        return instance.followers.count()
    
    def get_following_count(self, instance):
        return instance.following.count()

class ProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    # like_movie_list = serializers.SerializerMethodField()
    # like_music_list = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('followers', 'following', 'followers_count', 'following_count')

    def get_followers(self, instance):
        followers = instance.followers.all()
        return [{'id':follower.id, 'email':follower.email, 'nickname':follower.nickname, 'profile_picture':follower.profile_picture} for follower in followers]
    
    def get_following(self, instance):
        following = instance.following.all()
        return [{'id':follower.id, 'email':follower.email, 'nickname':follower.nickname, 'profile_picture':follower.profile_picture} for follower in following]
    
    # def get_like_movie_list(self, instance):
    #     like_movie_list = instance.users_like_movies.all()
    #     return[{'title':movie.title, 'poster_path':movie.poster_path} for movie in like_movie_list]
    
    def get_followers_count(self, instance):
        return instance.followers.count()
    
    def get_following_count(self, instance):
        return instance.following.count()
