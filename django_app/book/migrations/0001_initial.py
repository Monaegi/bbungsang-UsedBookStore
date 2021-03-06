# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 07:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_img', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('publication_date', models.CharField(max_length=15)),
                ('isbn', models.CharField(max_length=50)),
                ('normal_price', models.CharField(blank=True, max_length=25)),
                ('used_price', models.CharField(blank=True, max_length=25)),
                ('category', models.CharField(choices=[('lang', '언어'), ('os', '운영체제'), ('algorithm', '자료구조/알고리즘'), ('network', '네트워크'), ('db', '데이터베이스'), ('etc', 'etc(소프트웨어공학 등)')], max_length=50)),
                ('buyer', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('seller', models.ManyToManyField(to='member.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BuyBookRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_price', models.CharField(max_length=50)),
                ('etc_requirements', models.TextField()),
                ('book_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_book_info', to='book.Book')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellBookRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_price', models.CharField(max_length=50)),
                ('book_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_book_info', to='book.Book')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_info', to='member.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='bookstatus',
            name='sell_book_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.SellBookRegister'),
        ),
    ]
