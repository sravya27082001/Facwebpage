# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0023_auto_20171118_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualification',
            name='Intermediate',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='SSC',
        ),
        migrations.AddField(
            model_name='qualification',
            name='Experience',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
