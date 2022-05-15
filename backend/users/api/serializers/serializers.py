from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import (
    authenticate,
)
from backend.users.models import Prestamos

User = get_user_model()


class PrestamosSerializer(serializers.ModelSerializer):
    fecha = serializers.SerializerMethodField()
    worker = serializers.SerializerMethodField()
    fecha_del_pago = serializers.SerializerMethodField()
    pagado = serializers.SerializerMethodField()
    class Meta:
        model = Prestamos
        fields = [
            "id",
            "worker",
            "cantidad",
            "pagado",
            "fecha",
            "fecha_del_pago",
            "moneda"]

    def get_fecha_del_pago(self, obj):
        _return = 'sin pagar'
        if obj.fecha_del_pago:
            _return = f"{obj.created.day}/{obj.created.month}/{obj.created.year}"
        return _return
    
    def get_worker(self, obj):
        _return = None
        if hasattr(obj, 'user'):
            _return = obj.user.username
        return _return
    
    def get_pagado(self, obj):
        _return = 'No'
        if obj.pagado:
            _return = 'Si'
        return _return

    def get_fecha(self,obj):
        _return = None
        if hasattr(obj, 'created'):
            _return = f"{obj.created.day}/{obj.created.month}/{obj.created.year}"
        return _return


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserLoginSerializer(serializers.Serializer):
    """Users login Serializer.

    Handle login request data.
    """

    username = serializers.CharField()
    password = serializers.CharField(min_length=5)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(
            username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credential')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(
            user=self.context.get('user'))
        return self.context['user'], token.key
    
class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    role = serializers.StringRelatedField(read_only=True)
    groups = serializers.SerializerMethodField()
    
    class Meta:
        """Meta serializer."""

        model = User
        fields = (
            'pk',
            'username',
            'email',
            'is_active',
            'is_staff',
            'first_name',
            'last_name',
            'role',
            'groups',
        )
        read_only_fields = ['role', 'is_staff']
        
    def get_groups(self, obj):
        _return = None
        if hasattr(obj, 'groups'):
            _return = [group.name for group in obj.groups.all()]
        return _return