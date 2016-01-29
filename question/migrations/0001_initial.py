# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('question', models.CharField(max_length=500)),
                ('answer1', models.CharField(max_length=500)),
                ('answer2', models.CharField(max_length=500)),
                ('answer3', models.CharField(max_length=500)),
                ('answer4', models.CharField(max_length=500)),
                ('right_answer', models.IntegerField()),
            ],
        ),
    ]
