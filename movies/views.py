from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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

    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

    # use the get_object_or_404 function to handle 404. the below statement will be very repetitive
    # try:
    #     movie = Movie.objects.get(id=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
