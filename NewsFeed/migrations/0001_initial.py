# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiler', '0002_project'),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=4000)),
                ('image', models.URLField(null=True, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('publishedBy', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('issuingAuthority', models.CharField(max_length=150)),
                ('issueDate', models.DateTimeField(auto_now_add=True)),
                ('fileLink', models.URLField(null=True, blank=True)),
                ('branch', models.ForeignKey(default=False, to='Course.Department')),
                ('degree', models.ForeignKey(default=False, to='Course.Degree')),
                ('department', models.ForeignKey(default=False, to='Profiler.Student')),
            ],
        ),
    ]
