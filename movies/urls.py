from django.urls import path
from . import views

# URL Configuration:
# every app should have a url configuration
# movies/
# movies/1/details

urlpatterns = [
    path('', views.index, name='index')
]
