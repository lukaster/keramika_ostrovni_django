from django.contrib import admin
from .models import Aktuality, RozvrhDeti


class AktualityAdmin(admin.ModelAdmin):
    list_display = ('datum','text_zpravy_cs','typ_aktualit')

class RozvrhDetiAdmin(admin.ModelAdmin):
    list_display = ('cislo_krouzku','den','od','do','zaci_trida','ucitel','max_kapacita_krouzku')


# Register your models here.
admin.site.register(Aktuality, AktualityAdmin)
admin.site.register(RozvrhDeti, RozvrhDetiAdmin)
