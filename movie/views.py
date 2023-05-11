from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    count = Movie.objects.count()
    return render(request, 'home.html', {'movies':movies, 'count':count})

def detail(request, id):
    movie = get_object_or_404(Movie, pk = id)
    return render(request, 'detail.html', {'movie': movie})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_movie = Movie()
    new_movie.title = request.POST['title']
    new_movie.percent = request.POST['percent']
    new_movie.body = request.POST['body']
    new_movie.save()
    return redirect('detail', new_movie.id)