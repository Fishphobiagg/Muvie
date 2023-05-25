from django.db import models
from musics .models import Music

class Movie(models.Model):
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=30, default='')
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    ost = models.ManyToManyField(Music, related_name='movie_ost')