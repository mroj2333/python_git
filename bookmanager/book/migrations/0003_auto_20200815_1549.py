# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-08-15 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200815_1547'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookinfo',
            table='BookInfo',
        ),
    ]
