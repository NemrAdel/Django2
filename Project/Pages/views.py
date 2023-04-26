from django.shortcuts import render
# from .models import Ticket
from .forms import Ticket
# from django.http import HttpResponse
# Create your views here.
def index(request):
    return render (request,'pages/index.html')
def about(request):
    return render (request,'pages/about.html')
# def loginn(request):
#     x=request.POST.get('Username')
#     y=request.POST.get('Password')
#     data=login(Username=x,Password=y)
#     data.save()
#     return render (request,'pages/login.html',{'lf':loginform})
def loginn(request):
    x=request.POST.get('f_name')
    y=request.POST.get('l_name')
    p=request.POST.get('phone')
    a=request.POST.get('age')
    i=request.POST.get('idd')
    data=Ticket(l_name=y,f_name=x,phone=p,idd=i,age=a)
    data.save()
    return render (request,'pages/about.html',{'Ti':Ticket})