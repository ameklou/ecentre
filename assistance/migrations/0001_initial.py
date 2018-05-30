# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 18:53
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
            name='Assistence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('Medecin', 'Medecin'), ('Gynecologue', 'Gynecologue'), ('Conseiller Psychosocial', 'Conseiller Psychosocial'), ('Sociologue', 'Sociologue'), ('Sage-femme', 'Sage-femme'), ('Pair-Educateur', 'Pair-Educateur')], max_length=250)),
                ('message', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
