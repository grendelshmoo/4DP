# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condominium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Island',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='LandRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_date', models.DateField(blank=True, null=True)),
                ('recording_date', models.DateField(blank=True, null=True)),
                ('document_type', models.CharField(blank=True, max_length=128, null=True)),
                ('instrument_number', models.CharField(blank=True, max_length=32, null=True)),
                ('fy_number', models.CharField(blank=True, max_length=64, null=True)),
                ('land_registry', models.CharField(blank=True, max_length=32, null=True)),
                ('lcdn', models.IntegerField(default=0)),
                ('book', models.PositiveSmallIntegerField(default=0)),
                ('page', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('airport_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_description', models.CharField(max_length=256)),
                ('lot', models.CharField(blank=True, max_length=64, null=True)),
                ('block', models.CharField(blank=True, max_length=32, null=True)),
                ('unit', models.CharField(blank=True, max_length=32, null=True)),
                ('area', models.FloatField(default=0.0)),
                ('phase', models.CharField(blank=True, max_length=32, null=True)),
                ('tract', models.IntegerField(default=0)),
                ('increment', models.PositiveSmallIntegerField(default=0)),
                ('lot_sf', models.FloatField(default=0.0)),
                ('building_sf', models.FloatField(default=0.0)),
                ('map_document', models.IntegerField(default=0)),
                ('building_type', models.CharField(blank=True, max_length=32, null=True)),
                ('year_built', models.PositiveSmallIntegerField(default=0)),
                ('construction_type', models.CharField(blank=True, max_length=32, null=True)),
                ('building_condition', models.CharField(blank=True, max_length=32, null=True)),
                ('condominium', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='C4D.Condominium')),
                ('island', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='C4D.Island')),
                ('municipality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='C4D.Municipality')),
            ],
        ),
        migrations.CreateModel(
            name='TitleCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('recording_fees', models.FloatField(default=0.0)),
                ('land_tax', models.FloatField(default=0.0)),
                ('building_tax', models.FloatField(default=0.0)),
                ('land_appraised_value', models.FloatField(default=0.0)),
                ('building_appraised_value', models.FloatField(default=0.0)),
                ('record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='C4D.LandRecord')),
            ],
        ),
        migrations.AddField(
            model_name='landrecord',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C4D.Office'),
        ),
        migrations.AddField(
            model_name='landrecord',
            name='properties',
            field=models.ManyToManyField(to='C4D.Property'),
        ),
        migrations.AddField(
            model_name='landrecord',
            name='title_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='C4D.TitleCompany'),
        ),
    ]
