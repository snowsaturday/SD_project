# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]