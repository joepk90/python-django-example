from django.db import models
from django.utils import timezone
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    # diaplay the name of the genre, instead of the genre object
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    released_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()

    # CASCADING: delete all movies related to genre, if genre is deleted
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    # use django datetime so that django is aware of the timezone (otherwise we will need to handle timezone discrepencies manually)
    # only pass a reference to the timezone.now method, otherwise the date will be hardcoded in the migration
    date_created = models.DateTimeField(default=timezone.now)
