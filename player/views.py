from django.shortcuts import render
from player.models import Player as Model
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import Context, loader
import json
import hashlib

from skirmish.settings import *

# Create your views here.

# data format
resp = {
    "result": 'ok',
    "data": {},
    "payload": {
        "player": {"id": 1},
        "game": {"id": 1},
    }
}

class Player:

    def get(request):
        push_id = request.POST.get('push_id', None)

        players = Model.objects.filter(push_id=push_id)

        if not len(players):
            return

        player = players[0]

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                "player": player.json()
            }
        })

    def login(request):
        login = request.POST['user']
        pas  = request.POST['pass']
        push_id = request.POST.get('push_id', None)

        if (not login or not pas or not push_id):
            return JsonResponse({'status': 'invalid_params'})

        player = Model.objects.filter(login=login)

        if (not player):
            return JsonResponse({'status': 'user_not_found'})

        player = player[0]

        if (player.password != pas):
            return  JsonResponse({'status': 'invalid_password'})


        player.push_id = push_id
        player.status = PLAYER_STATUS_ONLINE
        player.save()

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                "player": player.json()
            }
        })

    def logout(request):
        push_id = request.POST.get('push_id', None)

        player = Model.objects.filter(push_id=push_id)

        if (not player):
            return JsonResponse({'status': 'user_not_found'})

        player = player[0]

        player.status = PLAYER_STATUS_OFFLINE

        player.save()

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                "player": player.json()
            }
        })


    def register(request):
        login = request.POST.get('user', None)
        pas  = request.POST.get('pass', None)
        city = request.POST.get('city', None)
        school= request.POST.get('school', None)

        if (not login):
            return JsonResponse({'status': 'user_invalid'})

        if (not pas):
            return JsonResponse({'status': 'password_invalid'})

        player = Model.objects.filter(login=login)
        if (player):
            return JsonResponse({'status': 'exists'})

        player = Model()
        player.login = login
        player.password = pas
        player.status = PLAYER_STATUS_OFFLINE

        player.save()

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                "player": player.json()
            }
        })

    def hello(request):
        push_id     = request.POST.get('push_id', None)

        autorized_final = None
        player = None

        if not push_id:
            autorized_final = False

        if autorized_final == None:
            players = Model.objects.filter(push_id=push_id)

            if not len(players):
                return JsonResponse({
                    'status': 'ok',
                    'result': {},
                    'payload': {
                        "player": {"status": PLAYER_STATUS_OFFLINE}
                    }
                })

            player = players[0]
            if player.status != "logout":
                autorized_final = True

        game = player.game.filter(status=GAME_STATUS_NEW)

        if len(game):
            game = game[0].json()
        else:
            game = None

        games = []
        for game in player.game.all():
            games.append(game.json())

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                "player": player.json(),
                "games": games
            }
        })

    def subscribe(request):
        push_id = request.POST['push_id']

        player = Model.objects.filter(push_id=push_id)

        if (not player):
            return JsonResponse({'status': 'redirect_login'})

        player = player[0]

        player.status = PLAYER_STATUS_LOOKING

        player.save()

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                "player": player.json()
            }
        })

    def unsubscribe(request):
        push_id = request.POST['push_id']

        player = Model.objects.filter(push_id=push_id)

        if (not player):
            return JsonResponse({'status': 'redirect_login'})

        player = player[0]

        player.status = PLAYER_STATUS_ONLINE

        player.save()

        return JsonResponse({
            'status': 'ok',
            'result': {},
            'payload': {
                "player": player.json()
            }
        })

    def temp(request):
        template = loader.get_template("google0db284838011d1e9.html")
        return HttpResponse(template.render())
        # print (request.POST['auth_token'])
        # print(request.user)
        # a = 'asd'
        # a = a.encode('utf-8')
        # m = hashlib.md5()
        # m.update(a)
        # print(m.hexdigest())
