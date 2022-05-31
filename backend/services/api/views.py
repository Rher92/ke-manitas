from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import ExpedienteSerializer, ExpedienteListSerializer
from .paginations import CustomPagination

from backend.services.models import Articulos, TiposGestion, Material, Expediente

from backend.services.api import serializers


User = get_user_model()

class ReadFieldsViewset(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        material = Material.objects.values('id', 'name', 'slug_name')
        tipo_conexion = TiposGestion.objects.values('id', 'name', 'slug_name')
        articulos = Articulos.objects.values('id', 'name', 'slug_name', 'precio_base')

        return Response({
            "materiales": material,
            "tipo_conexion": tipo_conexion,
            "articulos": articulos
        })


class ExpedienteViewset(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    parser_classes = (MultiPartParser,)
    permission_classes = [AllowAny]
    queryset = Expediente.objects.all()
    lookup_field = "pk"
    pagination_class = CustomPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('trabajador__username', "id")

    def get_permissions(self):
        """Assign permissions for each action"""
        permissions = [IsAuthenticated]
        return [permision() for permision in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        action_mappings = {
            'create': ExpedienteSerializer,
        }
        return action_mappings.get(self.action, ExpedienteListSerializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        _serializer = self.perform_create(serializer)
        return Response(
            {'expediente': _serializer},
            status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        vehicle_workday = serializer.save(trabajador=self.request.user)
        return ExpedienteListSerializer(vehicle_workday).data

    def perform_update(self, serializer):
        serializer.save(worker=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
