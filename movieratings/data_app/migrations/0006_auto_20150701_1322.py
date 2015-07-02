# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from data_app.models import Movie, Rating, User
import pandas as pd


def load_user_data(apps, schema_editor):
    datum = pd.read_csv('some_data/users.dat', sep='::', engine='python',
                        names=["id", "gender", "age", "occupation", "zipcode"])

    for row in datum.iterrows():
        user_object = row[1]
        User.objects.create(user_id=user_object.id, gender=user_object.gender,
                            age=user_object.age,
                            occupation=user_object.occupation,
                            zipcode=user_object.zipcode)


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0005_auto_20150701_1322'),
    ]

    operations = [
        migrations.RunPython(load_user_data)
    ]
