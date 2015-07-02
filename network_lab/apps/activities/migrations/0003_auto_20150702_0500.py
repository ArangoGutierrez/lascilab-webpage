# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20150620_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='encharged',
            field=models.ForeignKey(to='members.Member'),
        ),
    ]
