# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-18 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0002_auto_20160418_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='documentType',
            field=models.PositiveIntegerField(choices=[(0, 'Word Document'), (1, 'Text File'), (2, 'Presentation'), (3, 'PDF'), (4, 'Image'), (5, 'Other')]),
        ),
    ]
