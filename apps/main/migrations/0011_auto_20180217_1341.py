# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-17 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180216_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparel_product',
            name='product_gender_type',
            field=models.CharField(choices=[('men', 'Male'), ('women', 'Female'), ('unisex', 'Unisex')], max_length=256, verbose_name='Gender'),
        ),
    ]
