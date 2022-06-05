from django.contrib import admin
from django.utils.safestring import mark_safe


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
    readonly_fields = ['archivo']

    def archivo(self, obj):
        for i in obj.expedientesimagenes_set.all():
            image = i.file
            url = image.url
            return mark_safe(f"""
            <img src="{url}" width="150" height="150"/>
            <br>
            <br>
            <br>
            <div class="text-center">
            <ul class="object-tools">
                <li>
                <a href="{url}" class="historylink" target="_blank">Ver completo</a>
                </li>
            </ul>
            </div>""")
