# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageWrapper',
        ),
        migrations.AddField(
            model_name='document',
            name='day_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='source',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
