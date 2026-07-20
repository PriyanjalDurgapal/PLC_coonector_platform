from rest_framework import serializers

from .models import PLC, PLCTag, PLCOperationLog


# =====================================================
# PLC
# =====================================================

class PLCListSerializer(serializers.ModelSerializer):

    is_connected = serializers.SerializerMethodField()

    class Meta:

        model = PLC

        fields = (
            "id",
            "name",
            "manufacturer",
            "series",
            "ip_address",
            "port",
            "is_active",
            "is_connected",
        )

    def get_is_connected(self, obj):

        # Will be connected to PLCService later.
        return False


class PLCCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = PLC

        fields = (
            "name",
            "manufacturer",
            "series",
            "ip_address",
            "port",
            "is_active",
        )


class PLCUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = PLC

        fields = (
            "name",
            "manufacturer",
            "series",
            "ip_address",
            "port",
            "is_active",
        )


# =====================================================
# PLC TAG
# =====================================================

class PLCTagListSerializer(serializers.ModelSerializer):

    plc_name = serializers.CharField(
        source="plc.name",
        read_only=True,
    )

    class Meta:

        model = PLCTag

        fields = (
            "id",
            "plc",
            "plc_name",
            "name",
            "address",
            "data_type",

            # Visualization Colors
            "on_color",
            "off_color",
            "low_color",
            "medium_color",
            "high_color",

            "unit",
            "description",
            "is_writable",
            "is_active",
            "created_at",
            "updated_at",
        )


class PLCTagCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = PLCTag

        fields = (
            "plc",
            "name",
            "address",
            "data_type",

            # Visualization Colors
            "on_color",
            "off_color",
            "low_color",
            "medium_color",
            "high_color",

            "unit",
            "description",
            "is_writable",
            "is_active",
        )


class PLCTagUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = PLCTag

        fields = (
            "plc",
            "name",
            "address",
            "data_type",

            # Visualization Colors
            "on_color",
            "off_color",
            "low_color",
            "medium_color",
            "high_color",

            "unit",
            "description",
            "is_writable",
            "is_active",
        )


# =====================================================
# PLC OPERATION LOG
# =====================================================

class PLCOperationLogSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    plc_name = serializers.CharField(
        source="plc.name",
        read_only=True,
    )

    tag_name = serializers.CharField(
        source="tag.name",
        read_only=True,
    )

    class Meta:

        model = PLCOperationLog

        fields = (
            "id",
            "user_name",
            "plc_name",
            "tag_name",
            "operation",
            "old_value",
            "new_value",
            "created_at",
        )