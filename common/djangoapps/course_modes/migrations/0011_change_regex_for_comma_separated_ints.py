# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-30 17:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0010_archived_suggested_prices_to_charfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemode',
            name='suggested_prices',
            field=models.CharField(blank=True, default=b'', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\d+(?:\,\d+)*\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='coursemodesarchive',
            name='suggested_prices',
            field=models.CharField(blank=True, default=b'', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\d+(?:\,\d+)*\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
