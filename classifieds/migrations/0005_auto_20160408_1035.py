# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 17:35
from __future__ import unicode_literals

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0004_remove_category_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=None, default_currency='USD', max_digits=10, null=True),
        ),
    ]