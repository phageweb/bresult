# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bresult', '0003_auto_20161007_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='name',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
