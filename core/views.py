from django.shortcuts import render
from .models import Category
from .models import Movie


def home(request):
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'categories': categories})

def all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'core/movies.html', {'movies': movies})