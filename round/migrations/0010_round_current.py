# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0009_round_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='current',
            field=models.IntegerField(default=0),
        ),
    ]
