# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='word',
            field=models.CharField(default='_', max_length=500),
            preserve_default=False,
        ),
    ]