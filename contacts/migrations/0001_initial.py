# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название организации')),
                ('map', models.TextField(verbose_name='Код карты')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('phone_number_additional_1', models.CharField(max_length=10, verbose_name='Номер телефона дополнительный')),
                ('phone_number_additional_2', models.CharField(max_length=10, verbose_name='Номер телефона дополнительный')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]
