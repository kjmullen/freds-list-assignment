# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0007_auto_20160411_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, default='listing_picture/default.jpg', null=True, upload_to='listing_picture/'),
        ),
    ]