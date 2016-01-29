# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0008_remove_round_game'),
        ('game', '0005_auto_20151125_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rounds',
            field=models.ForeignKey(to='round.Round', default=None, null=True, blank=True),
        ),
    ]
