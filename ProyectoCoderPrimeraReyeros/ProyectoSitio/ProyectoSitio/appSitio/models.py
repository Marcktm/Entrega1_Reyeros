from django.db import models

# Create your models here.
class Madre(models.Model):
    
    nombre = models.CharField(max_length = 50)
    edad = models.IntegerField()
    peso = models.FloatField()

class Bebe(models.Model):

    dia = models.IntegerField()
    mes = models.IntegerField()
    year = models.IntegerField()

class Semana(models.Model):

    semana = models.IntegerField()


