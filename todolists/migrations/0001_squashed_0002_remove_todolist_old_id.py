# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-17 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'todolists', '0001_initial'), (b'todolists', '0002_remove_todolist_old_id')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('old_id', models.IntegerField(null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(db_index=True)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('raw', models.TextField(blank=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name=b'created_todolists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='TodolistPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pkgname', models.CharField(max_length=255)),
                ('pkgbase', models.CharField(max_length=255)),
                ('created', models.DateTimeField(editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('removed', models.DateTimeField(blank=True, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, b'Incomplete'), (1, b'Complete'), (2, b'In-progress')], default=0)),
                ('comments', models.TextField(blank=True, null=True)),
                ('arch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Arch')),
                ('pkg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Package')),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Repo')),
                ('todolist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolists.Todolist')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created',
            },
        ),
        migrations.AlterUniqueTogether(
            name='todolistpackage',
            unique_together=set([('todolist', 'pkgname', 'arch')]),
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='old_id',
        ),
    ]
