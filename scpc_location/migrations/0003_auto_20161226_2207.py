# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scpc_location', '0002_auto_20161226_1941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lastuserlocation',
            options={'verbose_name': 'Last User Location', 'verbose_name_plural': 'Last User Locations'},
        ),
        migrations.AlterField(
            model_name='lastuserlocation',
            name='latitude',
            field=models.DecimalField(decimal_places=9, max_digits=12, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='lastuserlocation',
            name='longitude',
            field=models.DecimalField(decimal_places=9, max_digits=12, verbose_name='longitude'),
        ),
    ]
