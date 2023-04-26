from django.db import models

# Create your models here.
class login(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    phone=models.IntegerField(null =True,blank=True)
    def __str__(self):
        return self.Username
class Ticket(models.Model):
    F_name=models.CharField(max_length=20)
    L_name=models.CharField(max_length=20)
    phone=models.IntegerField()
    age=models.IntegerField()
    idd=models.IntegerField()    
