# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
