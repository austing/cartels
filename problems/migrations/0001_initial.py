# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-06 22:17
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cartelisands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('problem', models.CharField(max_length=2500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('cartelisands', models.ManyToManyField(to='cartelisands.Cartelisand')),
            ],
        ),
    ]