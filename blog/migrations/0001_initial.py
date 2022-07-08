# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-06 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('bodytext', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
