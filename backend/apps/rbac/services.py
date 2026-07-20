from .models import Role
from django.contrib.auth.models import Permission


class RoleService:

    @staticmethod
    def get_roles():
        return Role.objects.all()

    @staticmethod
    def create_role(validated_data):
        return Role.objects.create(**validated_data)


class PermissionService:

    @staticmethod
    def get_permissions():
        return Permission.objects.all()

class RolePermissionService:

    @staticmethod
    def assign_permissions(role_id, permission_ids):

        role = Role.objects.get(
            id=role_id
        )

        permissions = Permission.objects.filter(
            id__in=permission_ids
        )

        role.permissions.set(
            permissions
        )

        return role


class RolePermissionQueryService:

    @staticmethod
    def get_role_permissions(role_id):

        role = Role.objects.get(
            id=role_id
        )

        return role.permissions.all()