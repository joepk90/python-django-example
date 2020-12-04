from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    released_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()

    # CASCADING: delete all movies related to genre, if genre is deleted
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
