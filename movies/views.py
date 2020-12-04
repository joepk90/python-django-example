from django.http import HttpResponse
from django.shortcuts import render
from . models import Movie

# Create your views here.


def index(request):

    # SELECT * FROM movies_movie WHERE released_year=1984
    # Movie.objects.fitler(released_year=1984)

    # SELECT * FROM movies_movie WHERE id=1
    # Movie.objects.get(id=1)

    # SELECT * FROM movies_movie
    movies = Movie.objects.all()
    return render(request, "movies/index.html", {'movies': movies})


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
