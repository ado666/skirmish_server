"""skirmish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from player.views import Player as player_views
from game.views import  Game as game_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^player/register', player_views.register),#user=(str),pass=(str),
    url(r'^player/hello', player_views.hello),#user=(str),pass=(str),
    url(r'^player/login', player_views.login),#user=(str),pass=(str)
    url(r'^player/logout', player_views.logout),#user=(str),pass=(str)
    url(r'^player/subscribe', player_views.subscribe),#auth_token(str),
    url(r'^player/unsubscribe', player_views.unsubscribe),#auth_token=(str),
    url(r'^player/get', player_views.get),#auth_token=(str),

    url(r'^game/get', game_views.get),#auth_token=(str),
    url(r'^game/all_active', game_views.all_active),#auth_token=(str),
    url(r'^game/answer', game_views.answer),#auth_token=(str),
    url(r'^game/all_active', game_views.all_active),#auth_token=(str),
    url(r'^game/theme_select', game_views.theme_select),#auth_token=(str),
    url(r'^game/aswer', game_views.answer),#auth_token=(str),

    url(r'', player_views.temp),
]
