# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-03 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swingers', '0011_swinger_bodytypeawaitingdecision'),
    ]

    operations = [
        migrations.AddField(
            model_name='swinger',
            name='bodytypefilteractive',
            field=models.BooleanField(default=False),
        ),
    ]
