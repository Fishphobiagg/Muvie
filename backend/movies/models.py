from django.db import models
from . . accounts .models import User
class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=30)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.URLField()
    genres = models.ManyToManyField(Genre)
    like_movie = models.ManyToManyField(User, related_name='users_like_movies', through='MusicUserLike')

class MusicUserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
