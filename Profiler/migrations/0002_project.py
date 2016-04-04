# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('highlight', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('projectType', models.CharField(max_length=2, default='MJ', choices=[('MJ', 'Major'), ('MN', 'Minor'), ('SD', 'Side')])),
                ('teamSize', models.PositiveIntegerField()),
                ('student', models.ForeignKey(default=False, to='Profiler.Student')),
            ],
        ),
    ]
