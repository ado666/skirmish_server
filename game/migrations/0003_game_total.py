# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20151115_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
