# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('hash', models.CharField(max_length=50)),
                ('push_id', models.CharField(max_length=100)),
            ],
        ),
    ]
