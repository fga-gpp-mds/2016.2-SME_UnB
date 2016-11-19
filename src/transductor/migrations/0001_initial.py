# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-16 21:22
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyTransductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie_number', models.IntegerField(default=None)),
                ('ip_address', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_ip_address', message='Incorrect IP address format', regex='^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$')])),
                ('description', models.TextField(max_length=150)),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('broken', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'permissions': (('can_view_transductors', 'Can view Transductors Page'),),
            },
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_date', models.DateField(auto_now=True, verbose_name='date published')),
                ('collection_minute', models.IntegerField(default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransductorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('transport_protocol', models.CharField(max_length=50)),
                ('serial_protocol', models.CharField(max_length=50)),
                ('measurements_type', models.CharField(max_length=50)),
                ('register_addresses', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='EnergyMeasurements',
            fields=[
                ('measurements_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='transductor.Measurements')),
                ('voltage_a', models.FloatField(default=None)),
                ('voltage_b', models.FloatField(default=None)),
                ('voltage_c', models.FloatField(default=None)),
                ('current_a', models.FloatField(default=None)),
                ('current_b', models.FloatField(default=None)),
                ('current_c', models.FloatField(default=None)),
                ('active_power_a', models.FloatField(default=None)),
                ('active_power_b', models.FloatField(default=None)),
                ('active_power_c', models.FloatField(default=None)),
                ('reactive_power_a', models.FloatField(default=None)),
                ('reactive_power_b', models.FloatField(default=None)),
                ('reactive_power_c', models.FloatField(default=None)),
                ('apparent_power_a', models.FloatField(default=None)),
                ('apparent_power_b', models.FloatField(default=None)),
                ('apparent_power_c', models.FloatField(default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('transductor.measurements',),
            managers=[
                ('mng_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='measurements',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_transductor.measurements_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='energytransductor',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transductor.TransductorModel'),
        ),
        migrations.AddField(
            model_name='energytransductor',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_transductor.energytransductor_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='energymeasurements',
            name='transductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transductor.EnergyTransductor'),
        ),
    ]
