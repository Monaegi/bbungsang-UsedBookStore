# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20171012_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(max_length=54, unique=True),
        ),
    ]
