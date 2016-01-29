# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0002_round_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='turn',
            field=models.ForeignKey(default=None, to='player.Player'),
        ),
    ]
