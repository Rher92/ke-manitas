from backend.vehicles.models.workdays import VehicleWorkDay, VehicleWorkDayFiles
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
        
        file = VehicleWorkDayFiles(
            file=file,
            vehicle_workday=vehicle_workday,
            type=VehicleWorkDayFiles.TypeFile.INIT
        )
        file.save()
        
        return vehicle_workday


class VehicleWorkDayListSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    class Meta:
        model = VehicleWorkDay
        fields = [
            "id", 
            "km_init",
            "km_finish",
            "close",
            "vehicle"
        ]
