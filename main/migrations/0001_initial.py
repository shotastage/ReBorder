# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-29 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameSessionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=100)),
                ('session_passwd', models.CharField(max_length=4)),
                ('members', models.CharField(default='', max_length=900)),
                ('created_by', models.CharField(max_length=100)),
                ('isRevoked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SuperAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('super_session_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name_identification', models.CharField(max_length=100)),
                ('user_student_id', models.CharField(max_length=8)),
                ('user_ethereum_account', models.CharField(max_length=100)),
            ],
        ),
    ]
