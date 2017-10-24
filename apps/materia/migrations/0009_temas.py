# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0008_materia_grado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('materia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materia.Materia')),
            ],
        ),
    ]
