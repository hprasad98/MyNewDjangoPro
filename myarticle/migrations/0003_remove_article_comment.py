# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-08 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0002_article_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
    ]