# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0007_auto_20151126_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='game',
        ),
    ]
