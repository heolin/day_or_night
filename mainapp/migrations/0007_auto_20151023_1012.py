# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20151021_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentclassification',
            old_name='day_score',
            new_name='score',
        ),
    ]
