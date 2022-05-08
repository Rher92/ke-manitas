from django.contrib import admin
import nested_admin

from django.utils.safestring import mark_safe
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
class VehicleWorkDayFilesAdmin(nested_admin.NestedModelAdmin):
    pass


@admin.register(Vehicle)
class VehicleAdmin(nested_admin.NestedModelAdmin):
    list_display = ['model', 'plate', 'km', 'available', 'type']
    list_filter = ['plate', 'km', 'available', 'type']
    search_fields = ['plate']


@admin.register(VehicleWorkDay)
class VehicleWorkDayAdmin(nested_admin.NestedModelAdmin):
    list_display = ['vehicle', 'worker', 'close']
    list_filter = ['vehicle', 'worker', 'close']
    search_fields = ['vehicle', 'worker']
    readonly_fields = ['init_work_day_file', 'finish_work_day_file']

    def init_work_day_file(self, obj):
        for i in obj.workday_file.all():
            if i.type == 'INIT' and i.vehicle_workday:
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

    def finish_work_day_file(self, obj):
        for i in obj.workday_file.all():
            if i.type == 'FINISH' and i.vehicle_workday:
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

@admin.register(ExpensesVehicleWorkday)
class ExpensesVehicleWorkdayAdmin(nested_admin.NestedModelAdmin):
    pass
