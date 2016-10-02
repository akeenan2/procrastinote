# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-10-02 11:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import noted.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('upload_date', models.DateTimeField(verbose_name=datetime.datetime(2016, 10, 2, 11, 13, 14, 660872, tzinfo=utc))),
                ('file_contents', models.FileField(upload_to=noted.models.file_path)),
                ('stored_name', models.CharField(max_length=300)),
                ('file_path', models.CharField(max_length=400)),
            ],
        ),
    ]
