# -*- coding: utf-8 -*-
import time
import sys, os
sys.path.append('/home/ado/projects/freebie')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freebie.settings")
from django.conf import settings
from geopy.distance import vincenty
from apns import APNs, Frame, Payload
import re
import django
django.setup()

from fuser.models import User
from faddress.models import Address
import datetime
from foffer.models import Offer, OfferToUser

USER_TIMEOUT = datetime.timedelta(minutes=10) # minutes
OFFER_TIMEOUT = datetime.timedelta(minutes=10)
OFFER_DISTANCE = 1000 # meters

def send_notif(now, user, offers, offertouser):
    offertouser.last_send = now
    token_hex = user.token[1:-1]
    token_hex = re.sub(r'\s', '', token_hex)

    APNS = APNs(use_sandbox=False, cert_file='PushNotifsCert_prod.pem', key_file='PushNotifsKey_prod.pem', enhanced=False)
    print "send notif: "+token_hex

    payload = Payload(alert=u"Рядом "+str(len(offers))+u" выгодная акция: "+offers[0].name, sound="default", badge=1)
    APNS.gateway_server.send_notification(token_hex, payload)

    user.last_send = now

while True:
    all_users = User.objects.all()
    all_addresses = Address.objects.all()
    now = datetime.datetime.now()

    for address in all_addresses:

        offers = address.offer_set.all()
        address_pos = (address.lng, address.lat)

        # no offer
        if (not len(offers)):
            continue

        for user in all_users:
            offertouser, created = OfferToUser.objects.get_or_create(
                user=user,
                offer=offers[0],
                defaults={
                    'user': user,
                    'offer': offers[0],
                    'last_send': '2001-01-01'#datetime.datetime.now()
                }
            )
            if (user.ignore_notifications == True):
                continue

            user_pos = (user.current_lng, user.current_lat)

            # new offertouser?
            if (created is True):
                offertouser.save()
                continue
            # user timeout
            if (now - user.last_send < USER_TIMEOUT):
                continue
            # offer timeout
            if (now - offertouser.last_send < OFFER_TIMEOUT):
                continue
            # no distance
            if (vincenty(user_pos, address_pos).meters > OFFER_DISTANCE):
                continue

            send_notif(now, user, offers, offertouser)

            user.save()
            offertouser.save()


    time.sleep(30)



