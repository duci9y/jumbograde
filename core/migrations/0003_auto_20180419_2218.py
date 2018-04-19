# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-19 22:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180224_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorecard',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='student',
        ),
        migrations.AddField(
            model_name='scorecard',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scorecard',
            name='submission',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='scorecard', to='core.Submission'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyz0123456789', min_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
