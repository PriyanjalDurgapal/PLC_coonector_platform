from rest_framework.permissions import BasePermission


class HasPermission(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        permission = getattr(
            view,
            "permissions_map",
            {},
        ).get(request.method)

        if not permission:
            return True

        return user.has_perm(permission)


class PLCTagPermission(BasePermission):
    """
    Permission rules for PLC Tags

    Admin:
        Full access

    Manager:
        View + Update

    Operator:
        View

    Viewer:
        View only
    """


    def has_permission(self, request, view):

        user = request.user


        # User must be authenticated
        if not user or not user.is_authenticated:
            return False


        # Admin / superuser
        if user.is_superuser:
            return True


        # Get action from ViewSet
        action = getattr(view, "action", None)


        # Read operations
        if action in [
            "list",
            "retrieve",
        ]:
            return self.has_permission_code(
                user,
                "view_plctag"
            )


        # Create
        if action == "create":
            return self.has_permission_code(
                user,
                "add_plctag"
            )


        # Update
        if action in [
            "update",
            "partial_update",
        ]:
            return self.has_permission_code(
                user,
                "change_plctag"
            )


        # Delete
        if action == "destroy":
            return self.has_permission_code(
                user,
                "delete_plctag"
            )


        return False



    def has_permission_code(
        self,
        user,
        permission_code
    ):

        """
        Connect with your existing RBAC system
        """

        return user.has_perm(
            f"plc.{permission_code}"
        )