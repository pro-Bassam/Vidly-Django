from django.contrib import admin
from movies.models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_in_stock', 'daily_rate')
    exclude = ('date_created',)


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
