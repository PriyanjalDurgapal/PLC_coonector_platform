import django_filters

from .models import User


class UserFilter(django_filters.FilterSet):

    role = django_filters.CharFilter(
        field_name="roles__name",
        lookup_expr="iexact"
    )


    class Meta:
        model = User

        fields = [
            "is_active",
            "is_staff",
            "role",
        ]