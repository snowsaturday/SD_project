# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-20 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmd_data', '0002_cmd_items_in_group_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmd_items',
            name='cmd_url',
            field=models.URLField(max_length=255, verbose_name='Ссылка на описание cmd сайт'),
        ),
    ]
