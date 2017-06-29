# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afip', '0016_auto_20170529_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='issued_date',
            field=models.DateField(
                help_text=(
                    'Can diverge up to 5 days for good, or 10 days otherwise'
                ),
                verbose_name='issued date',
            ),
        ),
    ]