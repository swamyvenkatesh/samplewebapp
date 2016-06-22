# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 05:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.BooleanField(default=False)),
                ('candidate_name', models.CharField(max_length=250)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('experience', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=3, null=True)),
                ('current_location', models.CharField(max_length=100)),
                ('preferred_location', models.CharField(max_length=100)),
                ('expected_ctc', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=3, null=True)),
                ('currenmt_employer', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
