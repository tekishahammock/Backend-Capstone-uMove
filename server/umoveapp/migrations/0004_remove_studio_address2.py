# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umoveapp', '0003_auto_20160919_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studio',
            name='address2',
        ),
    ]