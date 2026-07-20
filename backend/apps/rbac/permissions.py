from rest_framework.permissions import BasePermission


class HasPermission(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user or not user.is_authenticated:
            return False

        # Superuser always has access
        if user.is_superuser:
            return True

        permission = getattr(view, "permissions_map", {}).get(request.method)

        if not permission:
            return True

        return user.has_perm(permission)