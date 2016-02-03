from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from game.models import Game as Model
from player.models import Player
from theme.models import Theme
from question.models import Question
# from game.models import IngameResults

from skirmish.settings import *

from django.core import serializers

import re
import random

from apns import APNS

# Create your views here.


class Game:

    def all_active(request):
        push_id = request.POST.get('push_id', None)
        players  = Player.objects.all()

        if (not len(players)):
            return

        player = players[0]

        games = player.game

        print (player, games.all())

        return JsonResponse({'status': 'ok',
            'data': {
                # 'games':
                # 'username': player.login,
                # 'status': player.status,
                # 'username': player.login,
                # 'userId': str(player.id),
                # 'status': player.status,
                # 'entity': game.json(),
            }
        })

    def get(request):
        push_id = request.POST.get('push_id', None)
        gid     = request.POST.get('entityId', None)

        # player  = Player.objects.filter(push_id=push_id)[0]

        game    = Model.objects.get(pk=gid)

        # return JsonResponse({
        #     'status': 'ok',
        #     'result': {
        #         "game": game.json()
        #     },
        #     'payload': {
        #     }
        # })

        return JsonResponse({'status': 'ok',
            'data': {
                # 'username': player.login,
                # 'status': player.status,
                # 'username': player.login,
                # 'userId': str(player.id),
                # 'status': player.status,
                'entity': game.json(),
            }
        })

    def answer(request):
        qid     = request.POST.get('question_id', None)
        aid     = request.POST.get('answer_id', None)
        gid     = request.POST.get('game_id', None)
        push_id = request.POST.get('push_id', None)

        game    = Model.objects.get(pk=gid)
        player  = Player.objects.filter(push_id=push_id)[0]

        if not Game:
            return

        if game.total >= 9:
            game.status = settings.GA
            game.save()
            connection = APNS()
            connection.connect()
            for p in game.players.all():
                p.status = 'online'
                p.save()

                push_id = p.push_id[1:-1]
                push_id = re.sub(r'\s', '', push_id)

                connection.send(push_id, {'apn': {'action': 'show_result'}})

            return JsonResponse({'status': 'ok',
                'data': {
                }
            })

        if game.step >= 4:
            game.step = 0

            p1 = game.players.all()[0]
            p2 = game.players.all()[1]

            p1.status = 'enemy_turn'
            p2.status = 'ingame'

            p1.save()
            p2.save()

            game.turn = p2.id

            p1_push_id = p1.push_id[1:-1]
            p1_push_id = re.sub(r'\s', '', p1_push_id)
            p2_push_id = p2.push_id[1:-1]
            p2_push_id = re.sub(r'\s', '', p2_push_id)
            connection = APNS()
            connection.connect()
            print(p1_push_id, p2_push_id)
            connection.send(p1_push_id, {'apn': {'action': 'enemy_turn'}})
            connection.send(p2_push_id, {'apn': {'action': 'ingame'}})

        else:
            game.step += 1

        game.total += 1
        game.save()

        res = IngameResults()
        res.player_id = player.id
        res.game = game
        res.question_id = qid
        res.answer_id = aid
        res.save()

        return JsonResponse({'status': 'ok',
            'data': {
                # 'username': player.login,
                # 'status': player.status,
                'username': player.login,
                'userId': str(player.id),
                'status': player.status,
                'game': game.json()
            }
        })

    def theme_select(request):
        tid     = request.POST.get('theme_id', None)
        gid     = request.POST.get('game_id', None)

        game    = Model.objects.get(pk=gid)

        current_round = None
        for r in game.rounds.all():
            if r.current == 1:
                current_round = r

        theme = Theme.objects.get(pk=tid)

        current_round.theme = theme

        all_theme_questions = theme.questions.all()

        if (len(all_theme_questions) < 5):
            return JsonResponse({})
        questions           = random.sample(set(all_theme_questions), 5)

        current_round.questions = questions
        current_round.step = 1
        current_round.save()
        theme.save()
        game.save()

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                'game': game.json()
            }
        })


    def answer(request):
        gid     = request.POST.get('game_id', None)
        ch      = request.POST.get('choice', None)
        push_id = request.POST.get('push_id', None)

        game    = Model.objects.get(pk=gid)
        player  = Player.objects.filter(push_id=push_id)[0]

        if not Game:
            return

        cr = None
        for r in game.rounds.all():
            if r.current == 1:
                cr = r

        if cr.step == 5:
            if game.players.all()[0].id == player.id:
                cr.turn = game.players.all()[1]
            else:
                cr.turn = game.players.all()[0]
            cr.step = 1

            connection = APNS()
            connection.connect()

            address = cr.turn.push_id[1:-1]
            address = re.sub(r'\s', '', address)
            connection.send(address, {
                'changed': [{'entity': 'game', 'entity_id': game.id}]
            })

            connection.disconnect()
        else:
            cr.step = cr.step + 1

        cr.save()
        game.current_round = cr

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                'game': game.json()
            }
        })