from django.contrib import admin

from simple_history import register
from simple_history.admin import SimpleHistoryAdmin


# Register your models here.
from .models.vehicles import (
    State,
    Type,
    Brand,
    Vehicle
)

from .models.workdays import (
    VehicleWorkDay,
    ExpensesVehicleWorkday,
    VehicleWorkDayFiles
)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(VehicleWorkDayFiles)
class VehicleWorkDayFilesAdmin(admin.ModelAdmin):
    pass


#  Tracker
admin.site.register(Vehicle, SimpleHistoryAdmin)
admin.site.register(ExpensesVehicleWorkday, SimpleHistoryAdmin)
admin.site.register(VehicleWorkDay, SimpleHistoryAdmin)
