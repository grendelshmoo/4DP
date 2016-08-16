# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-16 22:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('C4D', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_ts', models.DateTimeField(auto_now=True)),
                ('end_ts', models.DateTimeField(blank=True, null=True)),
                ('file_name', models.CharField(max_length=256)),
                ('imported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RawLandRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=3)),
                ('document_date', models.CharField(blank=True, max_length=128, null=True)),
                ('recording_date', models.CharField(blank=True, max_length=128, null=True)),
                ('document_type', models.CharField(blank=True, max_length=128, null=True)),
                ('grantor', models.CharField(blank=True, db_index=True, max_length=512, null=True)),
                ('grantee', models.CharField(blank=True, db_index=True, max_length=512, null=True)),
                ('title_company', models.CharField(blank=True, max_length=512, null=True)),
                ('legal_description', models.CharField(blank=True, db_index=True, max_length=1024, null=True)),
                ('lot', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('block', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('tract', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('unit', models.CharField(blank=True, max_length=128, null=True)),
                ('area', models.CharField(blank=True, max_length=128, null=True)),
                ('phase', models.CharField(blank=True, max_length=128, null=True)),
                ('increment', models.CharField(blank=True, max_length=128, null=True)),
                ('lot_sf', models.CharField(blank=True, max_length=128, null=True)),
                ('building_sf', models.CharField(blank=True, max_length=128, null=True)),
                ('map_document', models.CharField(blank=True, max_length=128, null=True)),
                ('building_type', models.CharField(blank=True, max_length=128, null=True)),
                ('year_built', models.CharField(blank=True, max_length=128, null=True)),
                ('construction_type', models.CharField(blank=True, max_length=128, null=True)),
                ('building_condition', models.CharField(blank=True, max_length=128, null=True)),
                ('island', models.CharField(blank=True, max_length=256, null=True)),
                ('municipality', models.CharField(blank=True, max_length=512, null=True)),
                ('condominium', models.CharField(blank=True, max_length=512, null=True)),
                ('instrument_number', models.CharField(blank=True, max_length=128, null=True)),
                ('fy_number', models.CharField(blank=True, max_length=128, null=True)),
                ('cnmi_file_number', models.CharField(blank=True, max_length=128, null=True)),
                ('lcdn', models.CharField(blank=True, max_length=128, null=True)),
                ('book', models.CharField(blank=True, max_length=128, null=True)),
                ('page', models.CharField(blank=True, max_length=128, null=True)),
                ('amount', models.CharField(blank=True, max_length=128, null=True)),
                ('recording_fees', models.CharField(blank=True, max_length=128, null=True)),
                ('land_tax', models.CharField(blank=True, max_length=128, null=True)),
                ('building_tax', models.CharField(blank=True, max_length=128, null=True)),
                ('land_appraised_value', models.CharField(blank=True, max_length=128, null=True)),
                ('building_appraised_value', models.CharField(blank=True, max_length=128, null=True)),
                ('remarks', models.CharField(blank=True, max_length=1024, null=True)),
                ('import_log', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='C4D.ImportLog')),
            ],
        ),
        migrations.RenameModel(
            old_name='Property',
            new_name='Plot',
        ),
        migrations.RenameField(
            model_name='landrecord',
            old_name='property',
            new_name='plot',
        ),
    ]
