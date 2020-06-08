from django.db import models

# Create your models here.


class Aktuality(models.Model):
    TYPE_CHOICES=(('adults','dospeli'),('children','deti'))
    text_zpravy_cs = models.CharField(max_length=1000, blank=False)
    text_zpravy_en = models.CharField(max_length=1000,default='Sorry, no translation available yet')
    datum = models.DateField(auto_now=True)
    typ_aktualit=models.CharField(max_length=16, choices=TYPE_CHOICES, default='children')


class RozvrhDeti(models.Model):
    DAY_CHOICES = (('mon', 'pondělí'),('tue', 'úterý'),('wed', 'středa'),('thu', 'čtvrtek'),('fri', 'pátek'),('sat', 'sobota'),('sun', 'neděle'))
    cislo_krouzku = models.IntegerField(default=100)
    den = models.CharField(max_length=16, choices=DAY_CHOICES,default='mon')
    od = models.CharField(max_length=5,default='00:00')
    do = models.CharField(max_length=5, default='00:00')
    zaci_trida = models.CharField(max_length=20,default='1-2')
    ucitel = models.CharField(max_length=30, default='Eva Lukášová')
    max_kapacita_krouzku = models.IntegerField(default=10)



class Dite(models.Model):
    jmeno = models.CharField(max_length=20,blank=False)
    prijmeni = models.CharField(max_length=20,blank=False)
    #trida = models.
