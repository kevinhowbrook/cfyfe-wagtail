# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-05 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_projectpageprojectslideshowimages_slide_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
