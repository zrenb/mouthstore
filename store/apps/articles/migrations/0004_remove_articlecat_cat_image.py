# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-16 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articlecat_cat_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecat',
            name='cat_image',
        ),
    ]
