# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bot_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy_enable', models.BooleanField(default=False)),
                ('proxy_ip', models.GenericIPAddressField(null=True)),
                ('proxy_port', models.CharField(max_length=5, null=True)),
            ],
            options={
                'verbose_name': 'Прокси сервер',
                'verbose_name_plural': 'Прокси серверы',
            },
        ),
    ]