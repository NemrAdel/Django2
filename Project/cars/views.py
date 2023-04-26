from django.shortcuts import render
from .models import cars,person
# Create your views here.
def van(request):
    x=cars.objects.all()
    y={'cars':x.filter(price=200)}
    return render(request,'cars/car.html',y)
