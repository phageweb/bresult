# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bresult', '0007_auto_20161013_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='uid',
        ),
        migrations.AddField(
            model_name='result',
            name='user_id',
            field=models.OneToOneField(related_name='person', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
