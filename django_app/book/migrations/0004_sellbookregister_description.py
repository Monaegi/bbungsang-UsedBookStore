# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellbookregister',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
