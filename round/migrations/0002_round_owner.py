# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('round', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='owner',
            field=models.ForeignKey(default=None, related_name='round_owner', to='player.Player'),
            preserve_default=False,
        ),
    ]
