# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_document_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentClassification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_score', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.ImageField(upload_to=b'documents/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='documentclassification',
            name='document',
            field=models.ForeignKey(to='mainapp.Document'),
        ),
    ]
