# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-20 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmd_data', '0008_auto_20180420_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmd_items',
            name='cmd_url',
            field=models.CharField(max_length=255, verbose_name='Ссылка на описание cmd сайт'),
        ),
    ]
