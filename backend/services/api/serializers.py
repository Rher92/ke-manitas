from dataclasses import fields
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

    def validate_gestion(self, data):
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

    def validate_articulos(self, data):
        articulo = Articulos.objects.filter(pk=data)
        if not articulo:
            raise serializers.ValidationError(f'Articulos with pk: {data} does not exists.')
        return articulo


    def create(self, validated_data, *args, **kwargs):
        file = validated_data.pop('file')
        articulos = validated_data.pop('articulos', None)

        expediente = Expediente(
            **validated_data,
        )
        expediente.save()

        if articulos:
            expediente.articulos.add(*articulos)

        ExpedientesImagenes(
            file=file,
            expediente=expediente,
        ).save()

        return expediente


class ExpedienteListSerializer(serializers.ModelSerializer):
    trabajador = serializers.SerializerMethodField()
    cliente = serializers.SerializerMethodField()
    gestion = serializers.SerializerMethodField()
    material = serializers.SerializerMethodField()
    articulos = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Expediente
        fields = [
            'id',
            'identificador',
            'trabajador',
            'cliente',
            'gestion',
            'material',
            'articulos',
            'precio',
            'date'
        ]

    def get_trabajador(self, obj):
        _return = None
        if hasattr(obj, 'trabajador'):
            _return = obj.trabajador.username
        return _return

    def get_cliente(self, obj):
        _return = None
        if hasattr(obj, 'cliente'):
            if obj.cliente:
                _return = obj.cliente.user.username
        return _return

    def get_gestion(self, obj):
        _return = None
        if hasattr(obj, 'gestion'):
            _return = obj.gestion.name
        return _return

    def get_material(self, obj):
        _return = None
        if hasattr(obj, 'material'):
            if obj.material:
                _return = obj.material.name
        return _return

    def get_articulos(self, obj):
        _return = None
        if hasattr(obj, 'articulos'):
            _return = obj.articulos.all().values('id', 'name', 'precio_base')
        return _return

    def get_date(self,obj):
        _return = None
        if hasattr(obj, 'created'):
            _return = f"{obj.created.day}/{obj.created.month}/{obj.created.year}"
        return _return
