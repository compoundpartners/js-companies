# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 05:22
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('js_companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File', verbose_name='image'),
        ),
    ]