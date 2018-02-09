# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-09 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('user_assets', '0002_assetgroup_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Сайт'),
        ),
    ]
