# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20170130_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='program_picture',
        ),
        migrations.AddField(
            model_name='event',
            name='program',
            field=models.URLField(blank=True, null=True, verbose_name='Program URL'),
        ),
    ]