from rest_framework.permissions import BasePermission


class HasPermission(BasePermission):
    """
    Generic RBAC permission checker.

    Usage:

    required_permission = "users.read"

    """


    def has_permission(self, request, view):

        user = request.user


        if not user.is_authenticated:
            return False


       

        permission = getattr(
        view,
        "permissions_map",
        {}
    ).get(
        request.method
    )


        if not permission:
            return True


        user_permissions = set()


        for role in user.roles.all():

            permissions = (
                role.permissions
                .values_list(
                    "codename",
                    flat=True
                )
            )

            user_permissions.update(
                permissions
            )


        return permission in user_permissions