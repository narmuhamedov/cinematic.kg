from django import forms
from . import models

class TVShowForm(forms.ModelForm):
    class Meta:
        model = models.TvShow
        fields = "__all__"
