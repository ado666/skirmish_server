# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
        ('question', '0002_question_theme'),
        ('game', '0004_auto_20151125_1118'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('step', models.IntegerField()),
                ('game', models.ForeignKey(to='game.Game')),
                ('questions', models.ManyToManyField(related_name='round', to='question.Question')),
                ('theme', models.ForeignKey(to='theme.Theme')),
                ('turn', models.ForeignKey(to='player.Player')),
            ],
        ),
    ]
