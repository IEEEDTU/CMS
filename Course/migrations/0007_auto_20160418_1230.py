# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0006_auto_20160410_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegroup',
            name='instructor',
            field=models.ForeignKey(to='Profiler.Faculty', default='None', related_name='instructor'),
        ),
    ]
