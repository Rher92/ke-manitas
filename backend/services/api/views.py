from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import ReadFields

from backend.services.models import Articulos, TiposGestion, Material, Expediente

from backend.services.api import serializers


User = get_user_model()


class ReadFieldsViewset(viewsets.ViewSet):
    serializer_class = ReadFields
    # queryset = Expediente.objects.all()
    
    def list(self, request, *args, **kwargs):
        material = Material.objects.values('id', 'name', 'slug_name')
        tipo_conexion = TiposGestion.objects.values('id', 'name', 'slug_name')
        articulos = Articulos.objects.values('id', 'name', 'slug_name', 'precio_base')

        # serializer = ReadFields(
        #     tipo_conexion=tipo_conexion,
        #     material=material,
        #     articulos=articulos
        # )
        return Response({
            "materiales": material,
            "tipo_conexion": tipo_conexion,
            "articulos": articulos
        })
    