from django.db import models
from slugify import slugify

from backend.utils.models import BaseCreatedUpdatedModel


class Articulos(BaseCreatedUpdatedModel):
    name = models.CharField(max_length=36)
    slug_name = models.CharField(max_length=36)
    
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
