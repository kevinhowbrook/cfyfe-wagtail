# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20171227_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='cateogry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='project.ProjectCategory'),
        ),
    ]
