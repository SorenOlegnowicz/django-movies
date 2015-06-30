# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('m_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user_id', models.IntegerField()),
                ('m_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user_id', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('occupation', models.IntegerField()),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]
