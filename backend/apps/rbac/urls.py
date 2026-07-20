from django.urls import path

from .views import (
    RoleListCreateView,
    PermissionListView,
    RolePermissionView,
    PermissionTestView,
)


urlpatterns = [

    path(
        "roles/",
        RoleListCreateView.as_view(),
        name="roles"
    ),

    path(
        "permissions/",
        PermissionListView.as_view(),
        name="permissions"
    ),

    path(
        "roles/<int:role_id>/permissions/",
        RolePermissionView.as_view(),
        name="role-permissions"
    ),
     path(
        "test-permission/",
        PermissionTestView.as_view(),
        name="permission-test"
    ),
]