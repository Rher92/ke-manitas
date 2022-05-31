from django.contrib import admin

# Register your models here.
from .models import Articulos, TiposGestion, Material, Expediente


@admin.register(Articulos)
class ArticulosAdmin(admin.ModelAdmin):
    pass


@admin.register(TiposGestion)
class TiposGestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(Expediente)
class ExpedienteAdmin(admin.ModelAdmin):
    pass