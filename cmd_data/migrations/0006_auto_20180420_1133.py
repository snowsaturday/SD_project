# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-20 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmd_data', '0005_auto_20180420_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmd_items',
            name='in_group_service',
            field=models.BooleanField(default=False, verbose_name='Входит в состав комплексной услуги'),
        ),
    ]
