# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0011_listing_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.CharField(null=True, blank=True, max_length=2),
        ),
    ]
