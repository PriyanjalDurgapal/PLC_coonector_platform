from rest_framework import serializers
from django.contrib.auth.models import Permission

from .models import Role
from django.contrib.auth.models import Permission

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            "id",
            "name",
            "description",
            "is_system",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = (
            "id",
            "name",
            "codename",
        )

class RolePermissionSerializer(serializers.Serializer):

    permissions = serializers.ListField(
        child=serializers.IntegerField()
    )