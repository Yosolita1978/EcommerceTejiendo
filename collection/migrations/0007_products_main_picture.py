# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-05 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_remove_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='main_picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.ProductPicture'),
        ),
    ]
