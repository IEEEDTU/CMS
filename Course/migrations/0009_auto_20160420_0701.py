# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0008_auto_20160418_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegroup',
            name='instructor',
            field=models.ForeignKey(to='Profiler.Faculty'),
        ),
    ]
