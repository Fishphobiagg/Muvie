from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.URLField()
<<<<<<< HEAD
    genres = models.ManyToManyField(Genre)
    
=======
    genres = models.ManyToManyField(Genre)
>>>>>>> d0d09f5 (feat:movie CRUD)
