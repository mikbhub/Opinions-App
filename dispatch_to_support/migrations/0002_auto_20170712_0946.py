# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch_to_support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='feedback',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets_issued', to='collect_opinions.Feedback'),
        ),
    ]
