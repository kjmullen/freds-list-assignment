# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0012_city_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
