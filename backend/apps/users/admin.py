from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "id",
        "username",
        "email",
        "employee_id",
        "is_active",
        "is_staff",
        "display_roles",
    )

    list_filter = (
        "is_active",
        "is_staff",
        "roles",
    )

    search_fields = (
        "username",
        "email",
        "employee_id",
    )

    filter_horizontal = (
        "roles",
        "groups",
        "user_permissions",
    )


    def display_roles(self, obj):

        return ", ".join(
            role.name
            for role in obj.roles.all()
        )

    display_roles.short_description = "Roles"