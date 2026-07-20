import django_filters

from .models import PLCTag


class PLCTagFilter(django_filters.FilterSet):

    plc = django_filters.NumberFilter()

    data_type = django_filters.CharFilter(
        lookup_expr="iexact"
    )

    is_active = django_filters.BooleanFilter()

    is_writable = django_filters.BooleanFilter()

    class Meta:

        model = PLCTag

        fields = (
            "plc",
            "data_type",
            "is_active",
            "is_writable",
        )