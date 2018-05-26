from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from imdb.models import *
# Create your views here.
def index(request):
	return render(request, 'imdb/index.html')

def movieDetails(request):
	return redirect('/admin/imdb/movies/')	

def addMovie(request):
	return redirect('/admin/imdb/movies/add/')

def moviesEdit(request):
	if request.method == 'POST':
		start_name=request.POST['movieName']
		movieNum=Movies.objects.get(name__iexact=start_name).pk
		return redirect('/admin/imdb/movies/%s/change/' %movieNum)

def editMovie(request):
	movieList=Movies.objects.all().values_list('name',flat=True)
	return render(request, 'imdb/movieEdit.html',{'movieList':movieList})
