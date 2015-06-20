# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('owner', models.TextField(max_length=100)),
                ('description', models.TextField()),
                ('initial_date', models.DateField()),
                ('final_date', models.DateField()),
            ],
        ),
    ]