# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
