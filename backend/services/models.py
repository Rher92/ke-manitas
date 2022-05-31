from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

from backend.utils.models import BaseCreatedUpdatedModel

User = get_user_model()


class Articulos(BaseCreatedUpdatedModel):
    name = models.CharField(max_length=36)
    slug_name = models.CharField(max_length=36)
    precio_base = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)


class TiposGestion(BaseCreatedUpdatedModel):
    name = models.CharField(max_length=36)
    slug_name = models.CharField(max_length=36)
    
    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)


class Material(BaseCreatedUpdatedModel):
    name = models.CharField(max_length=36)
    slug_name = models.CharField(max_length=36)
    
    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)


class Expediente(BaseCreatedUpdatedModel):
    identificador = models.CharField(max_length=36)
    trabajador = models.ForeignKey(
                User,
                on_delete=models.DO_NOTHING,
                null=True,
                blank=True)
    cliente = models.ForeignKey('users.Cliente',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True)
    gestion = models.ForeignKey('TiposGestion',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True)
    material = models.ForeignKey('Material',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True)
    articulos = models.ManyToManyField('Articulos',
        null=True,
        blank=True)
    precio = models.IntegerField(null=True, blank=True)


class ExpedientesImagenes(BaseCreatedUpdatedModel):
    expediente = models.ForeignKey('Expediente',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True)
