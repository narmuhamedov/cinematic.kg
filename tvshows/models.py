from django.db import models

class TvShow(models.Model):
    GENRE = (
        ('Хоррор', 'Хоррор'),
        ('Комедия', 'Комедия'),
        ('Фантастика', 'Фантастика'),
        ('Драмма', 'Драмма'),
        ('Боевик', 'Боевик')
    )
    title = models.CharField('Укажите название фильма', max_length=100)
    description = models.TextField('Укажите описание фильма')
    image = models.ImageField('Загрузите фото', upload_to='cinema/')
    genre = models.CharField('Укажите жанр', max_length=100, choices=GENRE)
    director = models.CharField('Укажите режисера', max_length=100)
    cost = models.PositiveIntegerField('Укажите цену')
    year = models.DateField('Укажите дату выпуска фильма', null=True)
    trailer = models.URLField('Укажите трейлер', blank=True)

    def __str__(self):
        return f'{self.title}.{self.genre}'


class ReviewFilms(models.Model):
    STARS = (
        ('*', '*'),
        ('* *', '* *'),
        ('* * *', '* * *'),
        ('* * * *', '* * * *'),
        ('* * * * *', '* * * * *')
    )
    film_select = models.ForeignKey(TvShow, on_delete=models.CASCADE,
                                    related_name='comment_object')
    text_comment = models.TextField()
    rate_stars = models.CharField(max_length=20, choices=STARS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.film_select} - {self.rate_stars}'