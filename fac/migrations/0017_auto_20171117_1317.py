# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0016_auto_20171117_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teaching',
            name='Semester',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
