# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_auto_20170602_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='man',
            field=models.BooleanField(default=False, verbose_name='Мужчина?'),
        ),
    ]
