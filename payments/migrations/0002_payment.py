# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-11 00:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0008_products_overview'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('transaction_id', models.CharField(max_length=512)),
                ('status', models.CharField(choices=[('succesful', 'Succesful'), ('fail', 'Fail')], max_length=2)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
