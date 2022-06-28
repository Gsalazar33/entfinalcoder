from django.db import models

# Create your models here.

class Perro(models.Model):
    name=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    edad=models.IntegerField()
class Gato(models.Model):
    name=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    edad=models.IntegerField()
class Ave(models.Model):
    name=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    edad=models.IntegerField()