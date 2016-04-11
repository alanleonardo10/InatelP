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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
                ('price', models.CharField(max_length=50)),
                ('featurea', models.CharField(max_length=100)),
                ('featureb', models.CharField(max_length=100)),
                ('featurec', models.CharField(max_length=100)),
            ],
        ),
    ]
