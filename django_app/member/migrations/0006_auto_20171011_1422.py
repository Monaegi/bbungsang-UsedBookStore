# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20171010_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(blank=True, max_length=54, unique=True),
        ),
    ]
