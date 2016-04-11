# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titulo', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.TextField(verbose_name='Price')),
                ('featurea', models.TextField(verbose_name='Feature 1')),
                ('featureb', models.TextField(verbose_name='Feature 2')),
                ('featurec', models.TextField(verbose_name='Feature 3')),
            ],
        ),
    ]
