# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mithun', '0002_auto_20160406_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web', models.CharField(max_length=50)),
                ('ma', models.CharField(max_length=50)),
                ('na', models.CharField(max_length=50)),
                ('ph', models.IntegerField()),
            ],
            options={
                'db_table': 'dream',
            },
        ),
    ]
