# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-21 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice1',
            new_name='choice',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='vote1',
            new_name='vote',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice2',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice3',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice4',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='vote2',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='vote3',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='vote4',
        ),
    ]
