# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T83',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t83_num', models.CharField(max_length=2)),
                ('t83_name', models.CharField(max_length=30)),
                ('t83_shart', models.CharField(max_length=4)),
            ],
        ),
    ]
