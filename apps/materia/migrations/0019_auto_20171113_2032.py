# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 02:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materia', '0018_temaproblema'),
    ]

    operations = [
        migrations.AddField(
            model_name='temaproblema',
            name='usa',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='temaproblema',
            name='respuesta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
