# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0004_auto_20150701_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.BigIntegerField(default=None),
        ),
    ]
