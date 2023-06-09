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
            profile_picture = '/users/default.jpg'if len(validated_data) == 3 else validated_data['profile_picture']
        )
        return user

class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname','email', 'profile_picture']

class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('following','followers')
    
    def get_following(self, instance):
        followers = instance.following.all()
        return [{"id":following.pk, 'nickname':following.nickname, 'email':following.email, 'profile_picture':following.profile_picture.url } for following in followers]
    
    def get_followers(self, instance):
        followers = instance.followers.all()
        return [{"id":follower.pk, 'nickname':follower.nickname, 'email':follower.email, 'profile_picture':follower.profile_picture.url} for follower in followers]
    
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'nickname', 'profile_picture']


class ProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    like_music_list = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    playlist = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('followers', 'following','followers_count', 'following_count', 'like_music_list', 'playlist')

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