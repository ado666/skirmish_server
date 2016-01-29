import sys, os

import django
sys.path.append('/home/ado/projects/skirmish')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skirmish.settings")
from django.conf import settings

from time import sleep
import re

from player.models import Player

from apns import APNS

connection = APNS()
connection.connect()

target = "e941d9b2f296788ed219b6eeebadbabc5043f7c3bbc64f7c2f98a38cfbe6fde4"

connection.send(target, {'apn': {'alert': '11111'}})

