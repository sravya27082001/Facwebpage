# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 18:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fac', '0024_auto_20171118_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institute', models.CharField(default=b'', max_length=100)),
                ('Position', models.CharField(default=b'', max_length=100)),
                ('year', models.IntegerField(default=b'', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]