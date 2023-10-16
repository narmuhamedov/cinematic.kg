from django.urls import path
from . import views

urlpatterns = [
    path('film_list/', views.filmListView, name='filmList'),
    path('film_detail/<int:id>/', views.filmDetailView, name='detail'),
]