from django.db import models

# Create your models here.
class TicketCinema(models.Model):
    F_name=models.CharField(max_length=10)
    L_name=models.CharField(max_length=10)
    age=models.IntegerField()
    id=models.IntegerField(primary_key=True)
    phone=models.IntegerField()
    def __str__(self):
        return self.F_name
class TicketPlane(models.Model):
    F_name=models.CharField(max_length=10)
    L_name=models.CharField(max_length=10)
    age=models.IntegerField()
    id=models.IntegerField(primary_key=True)
    phone=models.IntegerField()
    def __str__(self):
        return self.F_name
class TicketFootball(models.Model):
    F_name=models.CharField(max_length=10)
    L_name=models.CharField(max_length=10)
    age=models.IntegerField()
    id=models.IntegerField(primary_key=True)
    phone=models.IntegerField()
    def __str__(self):
        return self.F_name    