from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic


# список фильмов (не полная информация)
class FilmListView(generic.ListView):
    template_name = 'films/films_list.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()


# def filmListView(request):
#     film_value = models.TvShow.objects.all()
#     html_name = 'films/films_list.html'
#     context = {
#         'film_key': film_value,
#     }
#     return render(request, html_name, context)


# детальная информация
class FilmDetailView(generic.DetailView):
    template_name = 'films/film_detail.html'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=film_id)

# def filmDetailView(request, id):
#     film_id = get_object_or_404(models.TvShow, id=id)
#     html_name = 'films/film_detail.html'
#     context = {
#         'film_id': film_id,
#     }
#     return render(request, html_name, context)


# CRUD  - CREATE READ UPDATE DELETE

# create
class CreateFilmView(generic.CreateView):
    template_name = 'films/create_film.html'
    form_class = forms.TVShowForm
    queryset = models.TvShow.objects.all()
    success_url = '/film_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateFilmView, self).form_valid(form=form)


# def createFilmView(request):
#     method = request.method
#     if method == "POST":
#         form = forms.TVShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Фильм успешно добавлен')
#     else:
#         form = forms.TVShowForm()
#
#     return render(request, 'films/create_film.html', {'form': form})


# delete
class DeleteFilmView(generic.DeleteView):
    template_name = 'films/confirm_delete.html'
    success_url = '/film_list/'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=film_id)


# def deleteFilmView(request, id):
#     film_id = get_object_or_404(models.TvShow, id=id)
#     film_id.delete()
#     return HttpResponse('Фильм успешно удален')


# # update
class UpdateFilmView(generic.UpdateView):
    template_name = 'films/update_film.html'
    form_class = forms.TVShowForm
    success_url = '/film_list/'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=film_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateFilmView, self).form_valid(form=form)


# def updateFilmView(request, id):
#     film_id = get_object_or_404(models.TvShow, id=id)
#     if request.method == 'POST':
#         form = forms.TVShowForm(instance=film_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Фильм изменен')
#
#     else:
#         form = forms.TVShowForm(instance=film_id)
#     return render(request, 'films/update_film.html',
#                   {
#                       'form': form,
#                       'film_id': film_id
#                   }
#                   )


class Search(generic.ListView):
    template_name = 'films/films_list.html'
    context_object_name = 'film'
    paginate_by = 5

    def get_queryset(self):
        return models.TvShow.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context