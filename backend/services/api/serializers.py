from rest_framework import serializers

from backend.services.models import Articulos, TiposGestion, Material, Expediente


class ReadFields(serializers.Serializer):
    tipo_conexion = serializers.ListField()
    materiales = serializers.ListField()
    articulos = serializers.ListField()