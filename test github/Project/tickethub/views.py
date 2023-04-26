from django.shortcuts import render
from .models import TicketCinema,TicketFootball,TicketPlane
# Create your views here.
def TicketHub(request):
    return render (request,'tickethub/TicketHub.html')
def Ticketfootball(request):
    if request.method=='POST':
        f=request.POST.get('F_name')
        l=request.POST.get('L_name')
        p=request.POST.get('phone')
        i=request.POST.get('id')
        a=request.POST.get('age')
        data=TicketFootball(F_name=f,L_name=l,age=a,id=i,phone=p)
        data.save()
    return render(request,'tickethub/TicketFootball.html',{'tf':TicketFootball})
def Ticketplanes(request):
    if request.method=='POST':
        f=request.POST.get('F_name')
        l=request.POST.get('L_name')
        p=request.POST.get('phone')
        i=request.POST.get('id')
        a=request.POST.get('age')
        data=TicketPlane(F_name=f,L_name=l,age=a,id=i,phone=p)
        data.save()
    return render (request,'tickethub/TicketPlanes.html')
def Ticketcinema(request):
    if request.method=='POST':
        f=request.POST.get('F_name')
        l=request.POST.get('L_name')
        p=request.POST.get('phone')
        i=request.POST.get('id')
        a=request.POST.get('age')
        data=TicketCinema(F_name=f,L_name=l,age=a,id=i,phone=p)
        data.save()
    return render (request,'tickethub/TicketCinema.html')