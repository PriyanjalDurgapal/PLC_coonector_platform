from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    RoleSerializer,
    PermissionSerializer,
    RolePermissionSerializer,
)
from .services import (
    RoleService,
    PermissionService,
    RolePermissionService,
    RolePermissionQueryService,
)
from .permissions import HasPermission


class RoleListCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]

    permissions_map = {
        "GET": "rbac.view_role",
        "POST": "rbac.add_role",
    }

    def get(self, request):

        roles = RoleService.get_roles()

        serializer = RoleSerializer(
            roles,
            many=True,
        )

        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )

    def post(self, request):

        serializer = RoleSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        role = RoleService.create_role(
            serializer.validated_data
        )

        return Response(
            {
                "success": True,
                "message": "Role created successfully.",
                "data": RoleSerializer(role).data,
            },
            status=status.HTTP_201_CREATED,
        )


class PermissionListView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]

    permissions_map = {
        "GET": "rbac.view_permission",
    }

    def get(self, request):

        permissions = PermissionService.get_permissions()

        serializer = PermissionSerializer(
            permissions,
            many=True,
        )

        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )


class RolePermissionView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]

    permissions_map = {
        "GET": "rbac.view_role",
        "POST": "rbac.change_role",
    }

    def get(self, request, role_id):

        permissions = (
            RolePermissionQueryService
            .get_role_permissions(role_id)
        )

        serializer = PermissionSerializer(
            permissions,
            many=True,
        )

        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )

    def post(self, request, role_id):

        serializer = RolePermissionSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        role = RolePermissionService.assign_permissions(
            role_id,
            serializer.validated_data["permissions"],
        )

        return Response(
            {
                "success": True,
                "message": "Permissions assigned successfully.",
                "role_id": role.id,
            }
        )


class PermissionTestView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]

    permissions_map = {
        "GET": "rbac.view_user",
    }

    def get(self, request):

        return Response(
            {
                "success": True,
                "message": "You have user view permission",
            }
        )