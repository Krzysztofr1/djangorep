from django.db import models
from django.db.models import Model


class Sklep(models.Model):
    nazwa = models.CharField(max_length=100)
    lokalizacja = models.CharField(max_length=100)

class Pracownik(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    idd = models.ForeignKey(Sklep,on_delete=models.CASCADE)