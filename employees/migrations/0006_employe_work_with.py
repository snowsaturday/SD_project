# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20170528_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='work_with',
            field=models.DateField(null=True, verbose_name='Поступил на работу'),
        ),
    ]