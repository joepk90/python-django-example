from django.urls import path
from . import views

# URL Configuration:
# every app should have a url configuration
# movies/
# movies/1/details

# url syntax
# <> = url parameters
# prefixing with int: will prevent the page from returing if the paramter provided is not an int

urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
