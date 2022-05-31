from rest_framework import serializers

from backend.services.models import Articulos, TiposGestion, Material, Expediente, ExpedientesImagenes
from backend.users.models import Cliente

class ExpedienteSerializer(serializers.Serializer):
    identificador = serializers.CharField()  # expediente
    gestion = serializers.CharField()  # TiposGestion
    material = serializers.CharField(required=False)  # Material
    precio = serializers.CharField(required=False)
    articulos = serializers.CharField(required=False)  # Articulos
    file = serializers.FileField()

    def validate_tipo_gestion(self, data):
        try:
            tipo_gestion = TiposGestion.objects.get(pk=data)
        except TiposGestion.DoesNotExist:
            raise serializers.ValidationError(f'tipo de gestion with pk: {data} does not exists.')
        return tipo_gestion

    def validate_material(self, data):
        try:
            material = Material.objects.get(pk=data)
        except Material.DoesNotExist:
            raise serializers.ValidationError(f'Material with pk: {data} does not exists.')
        return material

    def validate_articulo(self, data):
        articulo = Articulos.objects.filter(pk=data)
        if not articulo:
            raise serializers.ValidationError(f'Articulos with pk: {data} does not exists.')
        return articulo


    def create(self, validated_data, *args, **kwargs):
        file = validated_data.pop('file')
        expediente = Expediente(
            **validated_data,
        )
        expediente.save()

        ExpedientesImagenes(
            file=file,
            expediente=expediente,
        ).save()

        return expediente


class ExpedienteListSerializer(serializers.ModelSerializer):
    pass