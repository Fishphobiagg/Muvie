from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Music(models.Model):
    tiitle = models.CharField(max_length=50)
    artist = models.CharField(max_length=30)
    uri = models.URLField(blank=False)

class MusicComponent(models.Model):
    energy = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    instrumentalness = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    liveness = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    acousticness = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    speechiness = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    valence = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    tempo = models.FloatField() # 0이상 아무 숫자
    mode = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    loudness = models.FloatField() # 0이상 아무 숫자
    danceability = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])