# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-14 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_apparel_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apparel_Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_price', models.CharField(max_length=255, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('master_apparel_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Apparel_Product', verbose_name='Apparel Product')),
            ],
            options={
                'verbose_name': 'Shipping Price',
                'verbose_name_plural': 'Shipping Prices',
            },
        ),
    ]
