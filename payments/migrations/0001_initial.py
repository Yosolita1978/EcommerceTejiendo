# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-16 16:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255, verbose_name='State/Province/Region')),
                ('postal_code', models.CharField(max_length=16, verbose_name='Postal Code')),
                ('country', models.CharField(choices=[('CAN', 'Canada'), ('MEX', 'Mexico'), ('USA', 'United States')], max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]