# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0025_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='year',
            field=models.IntegerField(default=b''),
        ),
    ]
