# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20151023_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentclassification',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='documentclassification',
            name='ip',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
