# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stapp', '0002_auto_20170410_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
    ]
