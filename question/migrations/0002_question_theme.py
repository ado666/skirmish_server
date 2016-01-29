# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(default=1, to='theme.Theme'),
            preserve_default=False,
        ),
    ]
