# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_value', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=264)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Search')),
            ],
        ),
    ]
