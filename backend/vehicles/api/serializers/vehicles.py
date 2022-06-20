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
    km_tolerance_up = serializers.SerializerMethodField()
    km_tolerance_down = serializers.SerializerMethodField()
    class Meta:
        model = VehicleLoginSerializer.Meta.model
        fields =  VehicleLoginSerializer.Meta.fields + [
            'plate',
            'brand',
            'color',
            'km',
            'is_being_used_by',
            'tolerancia_km',
            'km_tolerance_up',
            'km_tolerance_down'
        ]

    def get_is_being_used_by(self, obj):
        _return = None
        if instance := obj.vehicleworkday_set.last():
            if not instance.close:
                _return = obj.vehicleworkday_set.last().worker.name
        return _return

    def get_km_tolerance_up(self, obj):
        _return = None
        if (obj.tolerancia_km and obj.km):
            _return = obj.tolerancia_km + obj.km
        return _return

    def get_km_tolerance_down(self, obj):
        _return = None
        if (obj.tolerancia_km and obj.km):
            _return = obj.km - obj.tolerancia_km
        return _return