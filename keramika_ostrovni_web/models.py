from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.


class Aktuality(models.Model):
    TYPE_CHOICES = (('adults', 'dospeli'), ('children', 'deti'))
    COLOR_CHOICES = (('black', 'černá'), ('crimson', 'červená'), ('darkblue', 'modrá'))
    text_zpravy_cs = models.CharField(max_length=1000, blank=False)
    text_zpravy_en = models.CharField(max_length=1000, default='Sorry, no translation available yet')
    barva_textu = models.CharField(max_length=16, choices=COLOR_CHOICES, default='black')
    datum = models.DateField(auto_now=True)
    typ_aktualit = models.CharField(max_length=16, choices=TYPE_CHOICES, default='children')


class Krouzek(models.Model):
    DAY_CHOICES = (
        ('mon', 'pondělí'), ('tue', 'úterý'), ('wed', 'středa'), ('thu', 'čtvrtek'), ('fri', 'pátek'),
        ('sat', 'sobota'),
        ('sun', 'neděle'))
    cislo_krouzku = models.IntegerField(default=100)
    den = models.CharField(max_length=16, choices=DAY_CHOICES, default='mon')
    od = models.CharField(max_length=5, default='00:00')
    do = models.CharField(max_length=5, default='00:00')
    zaci_trida = models.CharField(max_length=20, default='1-2')
    ucitel = models.CharField(max_length=30, default='Eva Lukášová')
    max_kapacita_krouzku = models.IntegerField(default=10)
    cena = models.IntegerField(default=2000)

    start_fronty = models.IntegerField(default=0)
    konec_fronty = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.cislo_krouzku}:{self.den} {self.od}-{self.do}; fronta({self.start_fronty},{self.konec_fronty})"


class LekceDospeli(models.Model):
    DAY_CHOICES = (
        ('mon', 'pondělí'), ('tue', 'úterý'), ('wed', 'středa'), ('thu', 'čtvrtek'), ('fri', 'pátek'),
        ('sat', 'sobota'),
        ('sun', 'neděle'))
    cislo_krouzku = models.IntegerField(default=9000)
    den = models.CharField(max_length=16, choices=DAY_CHOICES, default='thu')
    datum = models.DateField()
    od = models.CharField(max_length=5, default='16:00')
    do = models.CharField(max_length=5, default='19:00')
    ucitel = models.CharField(max_length=30, default='Eva Lukášová')
    max_kapacita_krouzku = models.IntegerField(default=10)
    cena = models.IntegerField(default=100)


class Dite(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="deti"
    )
    jmeno = models.CharField(max_length=20, blank=False)
    prijmeni = models.CharField(max_length=20, blank=False)
    # 3.A
    rocnik = models.IntegerField(blank=False)
    paralelka = models.CharField(max_length=1, blank=False)
    # 2020/2021
    ve_skolnim_roce = models.CharField(max_length=9, blank=False)

    zapsany_krouzek = models.ManyToManyField(Krouzek, blank=True, related_name='zaci_krouzku')
    zapsany_JN_krouzek = models.ManyToManyField(Krouzek, blank=True,
                                                related_name='nahradnici_krouzku')  # jako nahradnik
    poradi_nahradnika = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.rocnik}.{self.paralelka}"


"""
class FrontaNahradniku(models.Model):

    krouzek = models.ForeignKey(Krouzek,
                                on_delete=models.CASCADE,
                                related_name="fronta"
                                )
    start_fronty = models.IntegerField(max_length=9,default=0)
    konec_fronty = models.IntegerField(max_length=9,default=0)
    def __str__(self):
        return f"Fronta ke krouzku {self.krouzek}, {self.start_fronty}-{self.konec_fronty}"
"""


class Dospely(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="dospeli"
    )
    jmeno = models.CharField(max_length=20, blank=False)
    prijmeni = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"


class KontaktInfo(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="kontakt_info"
    )
    jmeno = models.CharField(max_length=20, blank=True)
    prijmeni = models.CharField(max_length=20, blank=True)
    telefoni_cislo = models.IntegerField(null=True, blank=True, default=None)
    email = models.EmailField(max_length=254)  # ,default=User.username)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} {self.telefoni_cislo} {self.email}"


class PlatebniInfo(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="platebni_info"
    )
    cislo_uctu = models.CharField(max_length=50, default="0800/7625489755")
    var_symbol = models.IntegerField(default=120)
    suma_k_zaplaceni = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.cislo_uctu} {self.var_symbol}  {self.suma_k_zaplaceni}kc"
