# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 23:06
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('publish', models.DateTimeField(default=None)),
                ('file', models.CharField(default=None, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Commits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('publish', models.DateTimeField(default=None)),
                ('file', models.CharField(default=None, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('publish', models.DateTimeField()),
                ('terminate', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('publish', models.DateField()),
                ('terminate', models.DateField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('publish', models.DateTimeField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='modules',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Projects'),
        ),
        migrations.AddField(
            model_name='commits',
            name='module_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Modules'),
        ),
        migrations.AddField(
            model_name='comments',
            name='commit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Commits'),
        ),
    ]