from django.contrib import admin

from .models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_system",
        "created_at",
    )

    search_fields = (
        "name",
    )

    filter_horizontal = (
        "permissions",
    )