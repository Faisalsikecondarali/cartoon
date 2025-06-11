from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('movies/', views.all_movies, name='movies'),
]
