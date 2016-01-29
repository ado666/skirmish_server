# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0006_auto_20151126_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='theme',
            field=models.ForeignKey(null=True, to='theme.Theme', blank=True),
        ),
    ]
