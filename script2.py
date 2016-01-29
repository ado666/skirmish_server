import sys, os
sys.path.append('/home/ado/projects/freebie')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freebie.settings")
from django.conf import settings

from fcompany.models import Company
from foffer.models import Offer
from faddress.models import Address

for comp in Company.objects.all():
    pass
    #address = new Address()
    #address.lat = 

for offer in Offer.objects.all():
    address = Address()
    address.name = "temp_name"
    address.lat = offer.lat
    address.lng = offer.lng
    address.company = offer.company
    address.save()

    offer.addresses.add(address)
