# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия сотрудника')),
                ('name', models.CharField(max_length=20, verbose_name='Имя сотрудника')),
                ('second_name', models.CharField(max_length=20, verbose_name='Отчество сотрудника')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото врача')),
                ('description', models.TextField(verbose_name='Биографические сведения')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='employe_speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=50, verbose_name='Специализация сотрудника')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.AddField(
            model_name='employe',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employe_speciality', verbose_name='Специализация сотрудника'),
        ),
    ]
