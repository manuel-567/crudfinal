# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crudfinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='Fecha_Foto',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
