from django.contrib import admin

from .models import Automobile
from .models import Client
from .models import Club_card
from .models import Contract

admin.site.register(Automobile)
admin.site.register(Client)
admin.site.register(Club_card)
admin.site.register(Contract)