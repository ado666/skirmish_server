# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20151125_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='step',
        ),
        migrations.RemoveField(
            model_name='game',
            name='total',
        ),
        migrations.RemoveField(
            model_name='game',
            name='turn',
        ),
    ]
