from django.urls import path
from . import views

urlpatterns = [
    path('film_list/', views.FilmListView.as_view(), name='filmList'),
    path('film_detail/<int:id>/', views.FilmDetailView.as_view(), name='detail'),
    path('film_detail/<int:id>/delete/', views.DeleteFilmView.as_view(), name='delete'),
    path('film_detail/<int:id>/update/', views.UpdateFilmView.as_view(), name='update'),
    path('create_film/', views.CreateFilmView.as_view(), name='createFilm'),
    path('search/', views.Search.as_view(), name='search'),
]