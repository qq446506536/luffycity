# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-10 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=64)),
                ('status', models.IntegerField(choices=[(1, '未支付'), (2, '已支付')], default=1)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Goods')),
            ],
        ),
    ]
