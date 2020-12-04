from django.http import HttpResponse
from django.shortcuts import render
from . models import Movie

# Create your views here.


def index(request):

    # SELECT * FROM movies_movie
    movies = Movie.objects.all()

    output = ','.join([m.title for m in movies])

    # SELECT * FROM movies_movie WHERE released_year=1984
    # Movie.objects.fitler(released_year=1984)

    # SELECT * FROM movies_movie WHERE id=1
    # Movie.objects.get(id=1)

    return HttpResponse(output)
