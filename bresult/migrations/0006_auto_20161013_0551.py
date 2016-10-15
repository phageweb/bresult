# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bresult', '0005_auto_20161012_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='person',
            new_name='uid',
        ),
    ]
