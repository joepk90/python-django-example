from django.contrib import admin
from .models import Genre, Movie

# ModelAdmin: representation of a model in the admin interface


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_in_stock', 'daily_rate')
    exclude = ('date_created',)  # comma required to make it a Tuple

    # alternatively you could specify the fields to show
    # fields = ('title', 'genre')

    # Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
