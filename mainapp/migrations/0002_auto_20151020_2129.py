# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagewrapper',
            name='source',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='imagewrapper',
            name='image_path',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
