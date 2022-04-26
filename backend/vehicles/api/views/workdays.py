from rest_framework import mixins, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser


# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

# Models
from backend.vehicles.models.workdays import VehicleWorkDay

# Serializers
from backend.vehicles.api.serializers.workdays import VehicleWorkDaySerializer, VehicleWorkDayListSerializer

class VehicleWorkDayViewSet(mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):

    parser_classes = (MultiPartParser,)
    permission_classes = [AllowAny]
    queryset = VehicleWorkDay.objects.all()
    lookup_field = "vehicle__plate"
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('vehicle__name', 'vehicle__plate')

    def get_permissions(self):
        """Assign permissions for each action"""
        permissions = [IsAuthenticated]
        return [permision() for permision in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        action_mappings = {
            'create': VehicleWorkDaySerializer,
        }
        return action_mappings.get(self.action, VehicleWorkDaySerializer)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        _serializer = self.perform_create(serializer)
        return Response(
            {'vehicle_workday': _serializer},
            status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        vehicle_workday = serializer.save(worker=self.request.user)
        return VehicleWorkDayListSerializer(vehicle_workday).data
