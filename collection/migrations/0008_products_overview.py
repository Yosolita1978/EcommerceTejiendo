# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-05 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_products_main_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='overview',
            field=models.TextField(default='work in progress'),
            preserve_default=False,
        ),
    ]
