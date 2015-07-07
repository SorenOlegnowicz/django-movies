# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_app', '0007_auto_20150701_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rater',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.CharField(max_length=100),
        ),
    ]
