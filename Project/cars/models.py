from django.db import models

# Create your models here.
class cars(models.Model):
    name=models.CharField(max_length=50)
    model=models.CharField(max_length=15)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    description=models.TextField(null=True,blank=True)
    boolean=models.BooleanField(default=True)
    date=models.DateTimeField()
    def __str__(self):
        return self.name
class person(models.Model):
    person=models.CharField(max_length=20)
    object=models.OneToOneField(cars,on_delete=models.CASCADE)    
    def __str__(self):
        return self.person

