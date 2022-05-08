from backend.vehicles.models.vehicles import Vehicle

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
    is_being_used_by = serializers.SerializerMethodField()
    class Meta:
        model = VehicleLoginSerializer.Meta.model
        fields =  VehicleLoginSerializer.Meta.fields + [
            'plate',
            'brand',
            'color',
            'km',
            'is_being_used_by'
        ]

    def get_is_being_used_by(self, obj):
        _return = None
        if not obj.vehicleworkday_set.last().close:
            _return = obj.vehicleworkday_set.last().worker.name
        return _return
