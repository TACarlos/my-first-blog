# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0015_auto_20171025_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='usuarios',
            field=models.ManyToManyField(to='materia.Materia'),
        ),
    ]
