from django.contrib import admin
from .models import TicketCinema,TicketFootball,TicketPlane
# Register your models here.
admin.site.register(TicketCinema)
admin.site.register(TicketFootball)
admin.site.register(TicketPlane)