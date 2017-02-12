# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 04:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20170212_0315'),
        ('event', '0007_remove_event_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSpeaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Person')),
                ('topics', models.ManyToManyField(to='event.Topic')),
            ],
        ),
    ]