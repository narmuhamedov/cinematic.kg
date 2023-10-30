from django.urls import path
from . import views

urlpatterns = [
    path('film_list_parser/', views.ParserFilmListView.as_view()),
    path('start_parsing/', views.ParserFormView.as_view()),
]