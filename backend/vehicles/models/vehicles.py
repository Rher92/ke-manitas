from django.db import models
from slugify import slugify


from backend.utils.models import BaseCreatedUpdatedModel
from simple_history.models import HistoricalRecords



class State(BaseCreatedUpdatedModel):
    name = models.CharField(max_length=36)
    slug_name = models.CharField(max_length=36)
    
    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'estado del vehiculo: {self.name}'


class Type(BaseCreatedUpdatedModel):
    name = models.CharField(max_length=36)
    slug_name = models.CharField(max_length=36)
    
    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'tipo de vehiculo: {self.name}'


class Brand(BaseCreatedUpdatedModel):
    name = models.CharField(max_length=36)
    slug_name = models.CharField(max_length=36)
    
    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'marca: {self.name}'


class Vehicle(BaseCreatedUpdatedModel):
    history = HistoricalRecords()
    color = models.CharField(max_length=36)
    model = models.CharField(max_length=36)
    plate = models.CharField(max_length=36)
    available = models.BooleanField(default=True)
    km = models.IntegerField()
    state = models.ForeignKey('State',
        related_query_name='vehicle',
        on_delete=models.DO_NOTHING,
    )
    brand = models.ForeignKey('Brand',
        related_query_name='vehicle',
        on_delete=models.DO_NOTHING,
    )
    type = models.ForeignKey('Type',
        related_query_name='vehicle',
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f'vehiculo: {self.pk} - {self.brand} - {self.model} - {self.plate}'
    
    @property
    def slug_name(self):
        return f'{self.brand} - modelo: {self.model} - matricula: {self.plate}'
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
