# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0010_auto_20160412_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
