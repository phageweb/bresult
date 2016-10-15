# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bresult', '0002_auto_20161007_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('round', models.IntegerField()),
                ('pairNS', models.IntegerField()),
                ('PairEW', models.IntegerField()),
                ('gameNumber', models.IntegerField()),
                ('table', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='PairEW',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='gameNumber',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='name',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='pairNS',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='round',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='table',
        ),
        migrations.AddField(
            model_name='schedule',
            name='scheduleItem',
            field=models.ForeignKey(to='bresult.ScheduleItem', default=1),
            preserve_default=False,
        ),
    ]
