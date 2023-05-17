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
            profile_picture = '/users/default.JPG'if len(validated_data) == 3 else validated_data['profile_picture']
        )
        return user

class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'profile_picture']

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

class UserTestSerializer(serializers.ModelSerializer):
    followers = SimpleUserSerializer(many=True)
    class Meta:
            model = User
            fields = ('pk', 'followers')

class MyProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    like_movie_list = serializers.SerializerMethodField()
    like_music_list = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    playlist = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('followers', 'following','followers_count', 'following_count', 'like_movie_list', 'like_music_list', 'playlist')

    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('user_pk', None)
        super().__init__(*args, **kwargs)
        self.user_pk = user_pk

    def get_followers(self, instance):
        user = User.objects.get(pk=self.user_pk)
        followers = instance.followers.all()
        return [{'id':follower.id, 'email':follower.email, 'nickname':follower.nickname, 'profile_picture':follower.profile_picture.url, 
                 'is_followed':True if follower in user.following.all() else "me" if follower == user else False} for follower in followers]
    
    def get_following(self, instance):
        user = User.objects.get(pk=self.user_pk)
        following = instance.following.all()
        return [{'id':follower.id, 'email':follower.email, 'nickname':follower.nickname, 'profile_picture':follower.profile_picture.url, 
                 'is_followed':True if follower in user.following.all() else "me" if follower == user else False} for follower in following]    
    
    def get_like_movie_list(self, instance):
        like_movie_list = instance.like_movie.all()
        return[{'title':movie.title, 'poster_path':movie.poster_path} for movie in like_movie_list]
    
    def get_like_music_list(self, instance):
        like_music_list = instance.like_music.all()
        return[{'title':music.title, 'artist':music.artist, 'uri':music.uri, } for music in like_music_list]
    
    def get_followers_count(self, instance):
        return instance.followers.count()
    
    def get_following_count(self, instance):
        return instance.following.count()
    
    def get_playlist(self, instance):
        playlist = instance.playlist.all()
        return [{'title': music.title, 'artist':music.artist, 'uri':music.uri} for music in playlist]

class ProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    like_movie_list = serializers.SerializerMethodField()
    like_music_list = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('followers', 'following','followers_count', 'following_count', 'like_movie_list', 'like_music_list')

    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('user_pk', None)
        super().__init__(*args, **kwargs)
        self.user_pk = user_pk

    def get_followers(self, instance):
        user = User.objects.get(pk=self.user_pk)
        followers = instance.followers.all()
        return [{'id':follower.id, 'email':follower.email, 'nickname':follower.nickname, 'profile_picture':follower.profile_picture.url, 
                 'is_followed':True if follower in user.following.all() else "me" if follower == user else False} for follower in followers]
    
    def get_following(self, instance):
        user = User.objects.get(pk=self.user_pk)
        following = instance.following.all()
        return [{'id':follower.id, 'email':follower.email, 'nickname':follower.nickname, 'profile_picture':follower.profile_picture.url, 
                 'is_followed':True if follower in user.following.all() else "me" if follower == user else False} for follower in following]    

    def get_like_movie_list(self, instance):
        like_movie_list = instance.like_movie.all()
        return[{'title':movie.title, 'poster_path':movie.poster_path} for movie in like_movie_list]
    
    def get_like_music_list(self, instance):
        like_music_list = instance.like_music.all()
        return[{'title':music.title, 'artist':music.artist, 'uri':music.uri, } for music in like_music_list]
    
    def get_followers_count(self, instance):
        return instance.followers.count()
    
    def get_following_count(self, instance):
        return instance.following.count()