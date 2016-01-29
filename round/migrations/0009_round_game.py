# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_remove_game_rounds'),
        ('round', '0008_remove_round_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='game',
            field=models.ForeignKey(null=True, blank=True, to='game.Game', related_name='rounds'),
        ),
    ]
