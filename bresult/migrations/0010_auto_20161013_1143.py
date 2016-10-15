# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bresult', '0009_auto_20161013_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='person', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
