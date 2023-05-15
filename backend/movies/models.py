from django.db import models
from musics .models import Music

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=30, default='')
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.URLField()
    genres = models.ManyToManyField(Genre)
    ost = models.ManyToManyField(Music, related_name='movie_ost')


