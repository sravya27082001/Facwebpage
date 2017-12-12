# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0019_teaching'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teaching',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='teaching',
            name='start_year',
        ),
        migrations.AddField(
            model_name='teaching',
            name='time',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
