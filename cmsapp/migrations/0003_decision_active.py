# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0002_resourcerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='decision',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
