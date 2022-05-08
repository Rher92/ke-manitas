from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.utils.models import BaseCreatedUpdatedModel
from simple_history.models import HistoricalRecords

from django.db.models.signals import post_save
from django.dispatch import receiver


class VehicleWorkDay(BaseCreatedUpdatedModel):
    history = HistoricalRecords()
    vehicle = models.ForeignKey('vehicles.Vehicle',
        related_query_name='workday',
        on_delete=models.DO_NOTHING,
    )
    worker = models.ForeignKey('users.User',
        related_query_name='workday',
        on_delete=models.DO_NOTHING,
    )
    km_init = models.IntegerField(
        null=True,
        blank=True)
    km_finish = models.IntegerField(
        null=True,
        blank=True)
    close = models.BooleanField(default=False)


@receiver(post_save, sender=VehicleWorkDay)
def save_profile(sender, instance, **kwargs):
    if instance.km_finish and instance.close:
        vehicle = instance.vehicle
        vehicle.km = instance.km_finish
        vehicle.save()


class ExpensesVehicleWorkday(BaseCreatedUpdatedModel):
    class TypeExpenses(models.TextChoices):
        FINE = 'FINE', _('fine/multa')
        SERVICE = 'SERVICE', _('service/servicio/mantenimiento')
        TICKET = 'TICKET', _('parking/estacionamiento')
        OTHER = 'OTHER', _('other/otro')

    history = HistoricalRecords()
    description = models.TextField()
    value = models.IntegerField()
    vehicle_workday = models.ForeignKey('VehicleWorkDay',
        related_query_name='expenses',
        on_delete=models.DO_NOTHING,
    )
    type = models.CharField(
        max_length=7,
        choices=TypeExpenses.choices,
        default=TypeExpenses.OTHER,
    )
    
    def __str__(self) -> str:
        return f'{self.pk} - {self.vehicle_workday} - {self.type} - {self.value}'
    

class VehicleWorkDayFiles(BaseCreatedUpdatedModel):
    
    class TypeFile(models.TextChoices):
        INIT = 'INIT', _('init workday file')
        FINISH = 'FINISH', _('finish workday file')
        EXPENSES = 'EXPENSES', _('expense workday file')
        OTHER = 'OTHER', _('other workday file')

    vehicle_workday = models.ForeignKey('VehicleWorkDay',
        related_name='workday_file',
        related_query_name='workday_file',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True)
    vehicle_workday_expenses = models.ForeignKey('ExpensesVehicleWorkday',
        related_name='workday_file',
        related_query_name='workday_file',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True)
    file = models.FileField(upload_to='workday/vehicle', blank=True, null=True)
    type = models.CharField(
        max_length=8,
        choices=TypeFile.choices,
        default=TypeFile.OTHER,
    )