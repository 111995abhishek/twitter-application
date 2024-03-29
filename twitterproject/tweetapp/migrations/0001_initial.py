# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-11 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_tweet', models.TimeField()),
                ('date_of_tweet', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('user_location', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(max_length=200)),
                ('no_of_tweets', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tweets',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweetapp.User'),
        ),
    ]
