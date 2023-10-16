from django.shortcuts import render, get_object_or_404
from . import models

#список фильмов (не полная информация)
def filmListView(request):
    film_value = models.TvShow.objects.all()
    html_name = 'films/films_list.html'
    context = {
        'film_key': film_value,
    }
    return render(request, html_name, context)


#детальная информация
def filmDetailView(request, id):
    film_id = get_object_or_404(models.TvShow, id=id)
    html_name ='films/film_detail.html'
    context = {
        'film_id': film_id,
    }
    return render(request, html_name, context)
