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

from .serializers.serializers import UserSerializer, UserLoginSerializer, UserModelSerializer
from backend.vehicles.api.serializers.workdays import VehicleWorkDayListSerializer

from backend.users.models import Prestamos
from backend.users.api.paginations import PrestamosPagination
from backend.users.api.serializers.serializers import PrestamosSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    
    def get_serializer_class(self):
        """Return serializer based on action."""
        action_mappings = {
            'login': UserLoginSerializer,
        }
        return action_mappings.get(self.action, UserModelSerializer)

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User login."""
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token,
            'vehicle_workday': None
        }
        vehicle = user.vehicleworkday_set.all().filter(close=False).last()
        if vehicle:
            data['vehicle_workday'] = VehicleWorkDayListSerializer(vehicle).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def logout(self, request, *args, **kwargs):
        """User logout."""
        user = self.request.user
        Token.objects.filter(user=user).delete()
        data = {
            'response': 'User logout success.',
        }
        return Response(data, status=status.HTTP_200_OK)
    


class LentsViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    
    permission_classes = [AllowAny]
    queryset = Prestamos.objects.all()
    lookup_field = "pk"
    pagination_class = PrestamosPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('user__username', "id")

    def get_permissions(self):
        """Assign permissions for each action"""
        permissions = [IsAuthenticated]
        return [permision() for permision in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        action_mappings = {
            'list': PrestamosSerializer,
            'retrieve': PrestamosSerializer,
        }
        return action_mappings.get(self.action, VehicleWorkDayListSerializer)