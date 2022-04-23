from vehicles.models.vehicles import Vehicle

from rest_framework import serializers


class VehicleLoginSerializer(serializers.ModelSerializer):
    slug_name = serializers.SerializerMethodField()
    class Meta:
        model = Vehicle
        fields = [
            'id',
            'slug_name',
            'available'
        ]
        
    def get_slug_name(self, obj):
        return obj.slug_name


class VehicleSerializer(VehicleLoginSerializer):
    class Meta:
        model = VehicleLoginSerializer.Meta.model
        fields =  VehicleLoginSerializer.Meta.fields + [
            'plate',
            'brand',
            'color',
            'km'
        ]
