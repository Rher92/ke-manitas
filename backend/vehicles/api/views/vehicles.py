from rest_framework import mixins, viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

# Models
from backend.vehicles.models.vehicles import Vehicle

# Serializers
from backend.vehicles.api.serializers.vehicles import VehicleSerializer


class VehicleViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = [AllowAny]
    queryset = Vehicle.objects.all()
    lookup_field = "plate"
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name', 'plate')

    # def get_permissions(self):
    #     """Assign permissions for each action"""
    #     permissions = [IsAuthenticated]
    #     if self.action in ['retrieve', "list"]:
    #         permissions = [IsAuthenticated]
    #     return [permision() for permision in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        action_mappings = {
            'retrieve': VehicleSerializer,
            'list': VehicleSerializer
        }
        return action_mappings.get(self.action, VehicleSerializer)