# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-01-28 15:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20240128_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 28, 15, 9, 0, 260157, tzinfo=utc)),
        ),
    ]
