from django.urls import path
from . import views
urlpatterns=[
    path('TicketHub/',views.TicketHub,name='TicketHub'),
    path('TicketFootball/',views.Ticketfootball,name='TicketTicketFootball'),
    path('TicketPlanes/',views.Ticketplanes,name='TicketTicketPlanes'),
    path('TicketCinema/',views.Ticketcinema,name='TicketTicketCinema'),
]