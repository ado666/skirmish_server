# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0003_auto_20151126_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='step',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='round',
            name='turn',
            field=models.ForeignKey(to='player.Player'),
        ),
    ]
