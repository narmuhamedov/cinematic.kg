from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models, parser, forms

class ParserFilmListView(generic.ListView):
    model = models.ManasFilm
    template_name = 'parser/film_parser_list.html'

    def get_queryset(self):
        return models.ManasFilm.objects.all()


class ParserFormView(generic.FormView):
    template_name = 'parser/start_pars.html'
    form_class = forms.ParserTvForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные успешно взяты......')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
