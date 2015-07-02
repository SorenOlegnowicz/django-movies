# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from data_app.models import Movie, Rating, User
import pandas as pd


def load_movie_data(apps, schema_editor):
    datus = pd.read_csv('some_data/movies.dat', encoding='windows-1252',
                        sep='::', engine='python',
                        names=["id", "title", 'genres'])

    for row in datus.iterrows():
        movie_object = row[1]
        Movie.objects.create(m_id=movie_object.id,
                             title=movie_object.title,
                             genres=movie_object.genres)


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0003_auto_20150701_0401'),
    ]

    operations = [
        migrations.RunPython(load_movie_data)
    ]
