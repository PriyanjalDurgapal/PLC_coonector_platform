from django.contrib.auth.backends import BaseBackend


class RBACBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        return None

    def has_perm(self, user_obj, perm, obj=None):

        if not user_obj.is_authenticated:
            return False

        if user_obj.is_superuser:
            return True

        app_label, codename = perm.split(".")

        return user_obj.roles.filter(
            permissions__content_type__app_label=app_label,
            permissions__codename=codename,
        ).exists()