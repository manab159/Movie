from django.urls import path

from . import views


app_name='imdb'
urlpatterns = [
    path('', views.index, name='index'),
    path('movieDetails', views.movieDetails, name='movieDetails'),
    path('addMovie', views.addMovie, name='addMovie'),
    path('editMovie', views.editMovie, name='editMovie'),
    path('moviesEdit', views.moviesEdit, name='moviesEdit'),
]