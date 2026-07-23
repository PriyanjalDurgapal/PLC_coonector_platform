from django.contrib import admin

from .models import (
    PLC,
    PLCTag,
    PLCVisualizationObject,
)


@admin.register(PLC)
class PLCAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "manufacturer",
        "series",
        "ip_address",
        "port",
        "is_active",
    )

    list_filter = (
        "manufacturer",
        "series",
        "is_active",
    )

    search_fields = (
        "name",
        "ip_address",
    )

    ordering = (
        "name",
    )


@admin.register(PLCTag)
class PLCTagAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "plc",
        "name",
        "address",
        "data_type",
        "on_color",
        "off_color",
        "low_color",
        "medium_color",
        "high_color",
        "is_active",
    )

    list_filter = (
        "plc",
        "data_type",
        "is_active",
    )

    search_fields = (
        "name",
        "address",
    )


@admin.register(PLCVisualizationObject)
class PLCVisualizationObjectAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "tag",
        "svg_type",
        "label",
        "x",
        "y",
        "rotation",
        "scale",
        "visible",
    )

    list_filter = (
        "svg_type",
        "visible",
    )

    search_fields = (
        "tag__name",
        "label",
    )

    autocomplete_fields = (
        "tag",
    )