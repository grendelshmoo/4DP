# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-17 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C4D', '0003_auto_20160816_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawlandrecord',
            name='document_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rawlandrecord',
            name='recording_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
