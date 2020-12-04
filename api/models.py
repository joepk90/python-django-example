from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()  #  lazy object
        resource_name = 'movies'
