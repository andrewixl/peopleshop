# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180217_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='apparel_product',
            name='paypal_button',
            field=models.CharField(default='helo', max_length=750, verbose_name='Real Brand Price'),
            preserve_default=False,
        ),
    ]
