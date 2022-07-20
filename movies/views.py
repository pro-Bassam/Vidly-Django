from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()  # SELECT * FROM movies_movie

    # Movie.objects.filter(release_year=1985)# SELECT * FROM movies_movie WHERE release_year= 1985

    # Movie.objects.get(id=1)# SELECT * FROM movies_movie WHERE id= 1

    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)

    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
