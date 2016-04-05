# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appClinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='level',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hospital',
            name='level',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='lab',
            name='level',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='wtf',
            field=models.TimeField(verbose_name='working time from'),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='wtt',
            field=models.TimeField(verbose_name='working time to'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='wtf',
            field=models.TimeField(verbose_name='working time from'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='wtt',
            field=models.TimeField(verbose_name='working time to'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='wtf',
            field=models.TimeField(verbose_name='working time from'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='wtt',
            field=models.TimeField(verbose_name='working time to'),
        ),
    ]