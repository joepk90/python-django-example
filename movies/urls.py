from django.urls import path
from . import views

# URL Configuration:
# every app should have a url configuration
# movies/
# movies/1/details

# url syntax
# <> = url parameters
# prefixing with int: will prevent the page from returing if the paramter provided is not an int

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
