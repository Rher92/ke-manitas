from backend.vehicles.models.workdays import VehicleWorkDay, VehicleWorkDayFiles, ExpensesVehicleWorkday
from backend.vehicles.models.vehicles import Vehicle

from backend.vehicles.api.serializers.vehicles import VehicleSerializer

from rest_framework import serializers


class VehicleWorkDaySerializer(serializers.Serializer):
    vehicle = serializers.CharField()
    km = serializers.CharField()
    file = serializers.FileField()

    def validate_vehicle(self, data):
        try:
            vehicle = Vehicle.objects.get(pk=data)
        except Vehicle.DoesNotExist:
            raise serializers.ValidationError(f'Vehicle with pk: {data} does not exists.')
        return vehicle

    def validate_km(self, data):
        try:
            km = int(data)
        except:
            raise serializers.ValidationError(f'Km is not a number.')
        return km

    def create(self, validated_data, *args, **kwargs):
        vehicle = validated_data.pop('vehicle')
        file = validated_data.pop('file')
        km = validated_data.pop('km')
        worker = validated_data.pop('worker')
        vehicle_workday = VehicleWorkDay(
            vehicle=vehicle,
            km_init=km,
            worker=worker
        )
        vehicle_workday.save()
        
        VehicleWorkDayFiles(
            file=file,
            vehicle_workday=vehicle_workday,
            type=VehicleWorkDayFiles.TypeFile.INIT
        ).save()
        
        return vehicle_workday
    
    def update(self, instance, validated_data, *args, **kwargs):
        instance.km_finish = validated_data.pop('km')
        file = validated_data.pop('file')
        instance.worker = validated_data.pop('worker')
        instance.close = True
        instance.save(update_fields=['km_finish',
                                     'worker',
                                     'close'])
        VehicleWorkDayFiles(
            file=file,
            vehicle_workday=instance,
            type=VehicleWorkDayFiles.TypeFile.FINISH
        ).save()
        
        return instance

class VehicleWorkDayListSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    worker = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    class Meta:
        model = VehicleWorkDay
        fields = [
            "id", 
            "date",
            "km_init",
            "km_finish",
            "close",
            "worker",
            "vehicle",
        ]

    def get_worker(self, obj):
        _return = None
        if hasattr(obj, 'worker'):
            _return = obj.worker.username
        return _return

    def get_date(self,obj):
        _return = None
        if hasattr(obj, 'created'):
            _return = f"{obj.created.day}/{obj.created.month}/{obj.created.year}"
        return _return


class ExpensesVehicleWorkdaySerializer(serializers.ModelSerializer):
    vehicle = serializers.SerializerMethodField()
    worker = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    fecha_del_pago = serializers.SerializerMethodField()
    class Meta:
        model = ExpensesVehicleWorkday
        fields = [
            "id",
            "description",
            "value",
            "vehicle_workday",
            "type",
            "worker",
            "vehicle",
            "date",
            "moneda",
            "pagado",
            "fecha_del_pago"
        ]

    def get_vehicle(self, obj):
        _return = None
        if hasattr(obj, 'vehicle_workday'):
            _return = obj.vehicle_workday.vehicle.slug_name
        return _return

    def get_type(self, obj):
        _return = None
        if hasattr(obj, 'type'):
            _return = obj.vehicle_workday.vehicle.slug_name
        return _return

    def get_worker(self, obj):
        _return = None
        if hasattr(obj, 'vehicle_workday'):
            _return = obj.vehicle_workday.worker.username
        return _return

    def get_date(self,obj):
        _return = None
        if hasattr(obj, 'created'):
            _return = f"{obj.created.day}/{obj.created.month}/{obj.created.year}"
        return _return

    def get_fecha_del_pago(self,obj):
        _return = None
        if hasattr(obj, 'fecha_del_pago'):
            try:
                _return = f"{obj.fecha_del_pago.day}/{obj.fecha_del_pago.month}/{obj.fecha_del_pago.year}"
            except:
                _return = None
        return _return