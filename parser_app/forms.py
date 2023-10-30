from django import forms
from . import models, parser

class ParserTvForm(forms.Form):
    MEDIA_CHOISCES = (
        ('manas.kg', 'manas.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'manas.kg':
            manas_parser = parser.parser()
            for i in manas_parser:
                models.ManasFilm.objects.create(**i)

