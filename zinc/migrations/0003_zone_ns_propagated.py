# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zinc', '0002_auto_20170309_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='ns_propagated',
            field=models.BooleanField(default=False),
        ),
    ]
