import sys, os

import django
from django.core import serializers
sys.path.append('/home/ado/projects/skirmish')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skirmish.settings")
from django.conf import settings
from skirmish.settings import *

import random

from time import sleep
import re

from player.models import Player
from game.models import Game
from round.models import Round

from apns import APNS

django.setup()

connection = APNS()
connection.connect()

def match(first, second):
    first_push_id = first.push_id[1:-1]
    first_push_id = re.sub(r'\s', '', first_push_id)
    second_push_id = second.push_id[1:-1]
    second_push_id = re.sub(r'\s', '', second_push_id)

    first.status = PLAYER_STATUS_ONLINE
    second.status = PLAYER_STATUS_ONLINE

    first.save()
    second.save()

    game = Game()
    game.status = settings.GAME_STATUS_NEW
    game.save()

    game.players.add(first)
    game.players.add(second)

    r       = Round()
    r.game  = game
    r.owner = random.choice((first, second))
    r.turn  = r.owner
    r.current = 1
    r.save()

    if len(first_push_id) == 64:
        print ('--- sending notifications for ', first.login)
        connection.send(first_push_id, {
            'changed': [{'entity': 'user', 'entity_id': first.id}],
            'new': [{'entity': 'game', 'entity_id': game.id}],
        })
    if len(second_push_id) == 64:
        print ('--- sending notifications for ', second.login)
        connection.send(second_push_id, {
            'changed': [{'entity': 'user', 'entity_id': second.id}],
            'new': [{'entity': 'game', 'entity_id': game.id}],
        })


while True:
    all = Player.objects.all()

    _debug_looking   = 0

    first = None
    second = None

    for player in all:

        if (player.status == PLAYER_STATUS_LOOKING):
            _debug_looking += 1
            if not first:
                first = player
            elif not second:
                second = player

    if first and second:
        match(first, second)


    sleep(10)



