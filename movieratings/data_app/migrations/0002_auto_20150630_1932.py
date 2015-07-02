# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(to='data_app.Movie'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(to='data_app.User'),
        ),
    ]
