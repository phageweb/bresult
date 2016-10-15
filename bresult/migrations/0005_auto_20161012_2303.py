# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bresult', '0004_schedule_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('number', models.IntegerField()),
                ('result', models.IntegerField()),
                ('person', models.ForeignKey(to='bresult.Person')),
            ],
        ),
        migrations.RemoveField(
            model_name='pair',
            name='author',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='scheduleItem',
        ),
        migrations.DeleteModel(
            name='Pair',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='ScheduleItem',
        ),
    ]
