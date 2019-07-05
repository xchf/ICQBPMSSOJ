# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 09:42
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import myutils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ACMContestRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_number', models.IntegerField(default=0)),
                ('accepted_number', models.IntegerField(default=0)),
                ('total_time', models.IntegerField(default=0)),
                ('submission_info', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
            options={
                'db_table': 'acm_contest_rank',
            },
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', myutils.models.RichTextField()),
                ('real_time_rank', models.BooleanField()),
                ('password', models.TextField(null=True)),
                ('rule_type', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('visible', models.BooleanField(default=True)),
                ('allowed_ip_ranges', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'contest',
                'ordering': ('-start_time',),
            },
        ),
        migrations.CreateModel(
            name='ContestAnnouncement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', myutils.models.RichTextField()),
                ('visible', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'contest_announcement',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='OIContestRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_number', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
                ('submission_info', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'oi_contest_rank',
            },
        ),
        migrations.AddField(
            model_name='acmcontestrank',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest'),
        ),
        migrations.AddField(
            model_name='acmcontestrank',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]