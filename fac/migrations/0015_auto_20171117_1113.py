# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 11:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0014_auto_20171117_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teaching',
            old_name='Course_name',
            new_name='user',
        ),
    ]
