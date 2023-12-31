# Generated by Django 4.2.6 on 2023-10-26 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0002_tvshow_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField()),
                ('rate_stars', models.CharField(choices=[('*', '*'), ('* *', '* *'), ('* * *', '* * *'), ('* * * *', '* * * *'), ('* * * * *', '* * * * *')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('film_select', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='tvshows.tvshow')),
            ],
        ),
    ]
