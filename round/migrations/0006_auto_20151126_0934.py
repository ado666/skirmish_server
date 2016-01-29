# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0005_auto_20151126_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='step',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
