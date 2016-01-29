# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingameresults',
            name='game',
        ),
        migrations.RemoveField(
            model_name='game',
            name='questions',
        ),
        migrations.DeleteModel(
            name='IngameResults',
        ),
    ]
