# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-01 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20170201_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupes',
            name='nom_groupes',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterUniqueTogether(
            name='groupes',
            unique_together=set([('nom_utilisateur', 'nom_groupes')]),
        ),
    ]