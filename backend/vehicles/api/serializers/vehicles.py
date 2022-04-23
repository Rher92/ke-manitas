from vehicles.models.vehicles import Vehicle

from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'id',
            'plate',
            'brand',
            'color',
            'km'
        ]
