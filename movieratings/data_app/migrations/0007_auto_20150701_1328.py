# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from data_app.models import Movie, Rating, User
import pandas as pd


def load_rating_data(apps, schema_editor):
    daticus = pd.read_csv('some_data/tester.dat', sep='::', engine='python',
                          names=["uid", "mid", "rating", "timestamp"])

    for row in daticus.iterrows():
        rating_object = row[1]
        uid = User.objects.get(id=rating_object.uid)
        mid = Movie.objects.get(id=rating_object.mid)
        Rating.objects.create(user=uid, movie=mid, rating=rating_object.rating,
                              timestamp=rating_object.timestamp)

class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0006_auto_20150701_1322'),
    ]

    operations = [
        migrations.RunPython(load_rating_data)
    ]
