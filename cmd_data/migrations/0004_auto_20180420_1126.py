# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-20 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmd_data', '0003_auto_20180420_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmd_items',
            name='item_title',
            field=models.TextField(blank=True, verbose_name='Идентификатор ссылки'),
        ),
    ]