# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('step', models.IntegerField()),
                ('players', models.ManyToManyField(to='player.Player', related_name='game')),
                ('questions', models.ManyToManyField(to='question.Question', related_name='game')),
            ],
        ),
        migrations.CreateModel(
            name='IngameResults',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('question_id', models.IntegerField()),
                ('answer_id', models.IntegerField()),
                ('player_id', models.IntegerField()),
                ('game', models.ForeignKey(to='game.Game')),
            ],
        ),
    ]
