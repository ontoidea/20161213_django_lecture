# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('contents', models.TextField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
