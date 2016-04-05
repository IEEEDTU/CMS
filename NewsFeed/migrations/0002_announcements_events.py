# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiler', '0002_project'),
        ('Course', '0001_initial'),
        ('NewsFeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('dateAndTime', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(to='Course.Branch', default=False)),
                ('course', models.ForeignKey(to='Course.Course', default=False)),
                ('degree', models.ForeignKey(to='Course.Degree', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=50)),
                ('startDateAndTime', models.DateTimeField(default=False)),
                ('endDateAndTime', models.DateTimeField(default=False)),
                ('description', models.CharField(max_length=500)),
                ('organisedBy', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, default=False)),
                ('fbEvent', models.CharField(max_length=500)),
                ('website', models.CharField(max_length=75)),
                ('image', models.BinaryField(null=True)),
                ('alternativeMobile', models.ForeignKey(default=False, to='Profiler.Mobile', related_name='events_alternative_mobile')),
                ('personalMobile', models.ForeignKey(default=False, to='Profiler.Mobile', related_name='events_personal_mobile')),
            ],
        ),
    ]
