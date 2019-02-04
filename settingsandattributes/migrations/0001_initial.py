# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-04 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('long', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('long', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SexType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('long', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settingsandattributes.Country')),
            ],
        ),
        migrations.CreateModel(
            name='SwingerEthnicgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SwingPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('couple', models.BooleanField(default=False)),
                ('sex1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sex1', to='settingsandattributes.SexType')),
                ('sex2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sex2', to='settingsandattributes.SexType')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settingsandattributes.State'),
        ),
    ]