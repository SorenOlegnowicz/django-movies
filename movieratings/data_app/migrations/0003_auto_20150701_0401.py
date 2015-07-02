# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0002_auto_20150630_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='m_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='occupation',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(default=0),
        ),
    ]
