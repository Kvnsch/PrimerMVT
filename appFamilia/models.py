from django.db import models

# Create your models here.

class Familiar(models.Model): 
    nombre = models.CharField(max_length=60)
    nacimiento = models.DateField()
    numFavorito = models.IntegerField()

