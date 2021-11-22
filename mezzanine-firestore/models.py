from django.db import models
from django_countries.fields import CountryField

class Patient(models.Model):    
    GENERO_CHOICES = (
        ('1', 'Masculino'),
        ('2', 'Femenino'),
        ('3', 'Otro'),
    )
    
    firstName = models.CharField(max_length=128)  
    lastName = models.CharField(max_length=128)
    gender = models.CharField(max_length=16, choices=GENERO_CHOICES) #Masculino, Femenino, Otro
    genero_otro = models.CharField(max_length=32,blank=True,null=True) 
    birtday = models.DateField()
    coutry = CountryField()
