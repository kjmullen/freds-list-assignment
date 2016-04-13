# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 20:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0009_auto_20160412_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
